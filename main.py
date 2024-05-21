import argparse
import os
from PIL import Image
import utils
import numpy as np

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='image process tools for steam showcase | steam展柜图片处理工具')

    # parser.add_argument('input', type=str,
    #                     help='input image path')
    parser.add_argument('--input', type=str, default='./input/02.jpeg',
                        help='input image path, image and directory are supported')
    parser.add_argument('--output', '-o', type=str, default='./output/',
                        help='output directory')

    # type_parser = parser.add_mutually_exclusive_group(required=True)
    # type_parser.add_argument('-a', '--art', action='store_true',
    #                          help='convert to artwork showcase')
    # type_parser.add_argument('-w', '--workspace', action='store_true',
    #                          help='convert to workspace showcase')

    args = parser.parse_args()
    temp = True
    args.art = temp
    args.workspace = not temp
    utils.init(args)

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

    print(args)
