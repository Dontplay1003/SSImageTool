import os
from PIL import Image

w_width = 126
a_width = 630


def init(args):
    if not os.path.exists(args.output):
        try:
            os.makedirs(args.output)
        except OSError:
            print("Failed to create the output directory.")
            exit(1)

def read(args):
    if not os.path.exists(args.input):
        print("The input image does not exist.")
        exit(1)

    img = Image.open(args.input)
    args.format = img.format.lower()

    p_type = 'artwork' if args.artwork else 'workspace'
    args.file_name = os.path.basename(args.input)
    args.out = os.path.join(args.output, p_type + '_' + args.file_name)
    if not os.path.exists(args.out):
        try:
            os.makedirs(args.out)
        except OSError:
            print("Failed to create the output directory.")
            exit(1)

    return img


def set_args(img, args):
    args.src_width, args.src_height = img.size
    if args.artwork:
        if args.src_width < a_width:
            args.dest_width = a_width
            args.dest_height = int(args.src_height * args.dest_width / args.src_width)
        else:
            args.dest_width = args.src_width
            args.dest_height = args.src_height
    else:
        if args.src_width < w_width * 5:
            args.dest_width = w_width * 5
            args.dest_height = int(args.src_height * args.dest_width / args.src_width)
        else:
            args.dest_width = args.src_width
            args.dest_height = args.src_height


def split(img, args):
    frames = []
    if args.format.lower() in ['gif']:
        for index in range(img.n_frames):
            img.seek(index)
            frames.append(img.copy())
    else:
        frames.append(img)
    return frames


def resize(frames, args):
    for index, frame in enumerate(frames):
        frames[index] = frame.resize((args.dest_width, args.dest_height))
    return frames


def cut(frames, args):
    f1, f2, f3, f4, f5 = [], [], [], [], []
    for frame in frames:
        f1.append(frame.crop((w_width * 0, 0, w_width * 1, args.dest_height)))
        f2.append(frame.crop((w_width * 1, 0, w_width * 2, args.dest_height)))
        f3.append(frame.crop((w_width * 2, 0, w_width * 3, args.dest_height)))
        f4.append(frame.crop((w_width * 3, 0, w_width * 4, args.dest_height)))
        f5.append(frame.crop((w_width * 4, 0, w_width * 5, args.dest_height)))
    return f1, f2, f3, f4, f5


def save(frames, args, info, num):
    file_name = args.file_name.split('.')[0] + '.' + ('gif' if args.format.lower() in ['gif'] else 'png')
    if num == 0:
        file_path = os.path.join(args.out, file_name)
    else:
        file_path = os.path.join(args.out, str(num) + '_' + file_name)

    if args.format.lower() not in ['gif']:
        frames[0].save(file_path, format='png', optimize=True, quality=100)
    else:
        frames[0].save(file_path, format='gif', optimize=True, quality=100,
                       append_images=frames[1:], save_all=True, loop=info['loop'], duration=info['duration'])

    # 以二进制读写方式打开文件
    with open(file_path, 'rb') as f:
        # 读取文件内容
        data = f.read()
    if args.format.lower() in ['gif']:
        # 如果文件结尾为3B, 改为21
        data = data[:-1] + b'\x21'
    else:
        # 找到最后一个0x00的位置
        last_index = data.rfind(b'\x00')
        data = data[:last_index] + b'\x01\x49\x45\x4E\x44\x00\xD1\x1A\x4F\xE1'

    # 以二进制写方式打开文件
    with open(file_path, 'wb') as f:
        # 写入文件内容
        f.write(data)
