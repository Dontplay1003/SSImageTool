import argparse
import utils

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='image process tools for steam showcase | steam展柜图片处理工具')

    parser.add_argument('input', type=str,
                        help='image path')
    parser.add_argument('--output', '-o', type=str, default='./output/',
                        help='output directory')

    type_parser = parser.add_mutually_exclusive_group()
    type_parser.add_argument('-a', '--artwork', action='store_true',
                             help='convert to artwork showcase')
    type_parser.add_argument('-w', '--workspace', action='store_true',
                             help='convert to workspace showcase')

    args = parser.parse_args()
    utils.init(args)

    if not args.artwork and not args.workspace:
        print('Please specify the type of showcase you want to convert to | 请指定您要转换为的展柜类型:')
        t = input("type('a' for artwork, 'w' for workspace) | 类型('a'代表art, 'w'代表workspace'): ")
        if t == 'a':
            args.artwork = True
        elif t == 'w':
            args.workspace = True
        else:
            print('Invalid input | 无效输入')
            exit()

    # 单张图片处理
    img = utils.read(args)
    utils.set_args(img, args)
    info = img.info
    frames = utils.split(img, args)
    frames = utils.resize(frames, args)
    if args.workspace:
        f1, f2, f3, f4, f5 = utils.cut(frames, args)
        utils.save(f1, args, info, 1)
        utils.save(f2, args, info, 2)
        utils.save(f3, args, info, 3)
        utils.save(f4, args, info, 4)
        utils.save(f5, args, info, 5)
    else:
        utils.save(frames, args, info, 0)
