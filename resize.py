#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from PIL import Image
import argparse
import os
import PIL
import glob


def parse_hex(arg: str) -> tuple:
    arg = int(arg, base=16)
    blue = int(arg % 256)
    remainder = (arg - blue) / 256
    green = int(remainder % 256)
    remainder = (arg - green) / 256
    red = int(remainder / 256)
    return red, green, blue


def mix_channels(bottom: tuple, top: tuple) -> int:
    vb, ab = (x/255 for x in bottom)
    vt, at = (x/255 for x in top)
    return int(vb*ab + vt*at*(255-ab))


def mix_colours(bottom: tuple, top: tuple) -> tuple:
    rb, gb, bb, ab = bottom
    rt, gt, bt, at = top
    r = mix_channels((rb, ab), (rt, at))
    g = mix_channels((gb, ab), (gt, at))
    b = mix_channels((bb, ab), (bt, at))
    a = int(ab + at*(255-ab))
    return r, g, b, a


def main():
    program_description = """Image resizer for making iOS and macOS icons.
    In addition to resizing, the program is capable of removing alpha channel from an icon."""
    parser = argparse.ArgumentParser(description=program_description)
    parser.add_argument("--i", dest='input', default="icon.png", type=str, help="The original icon.")
    parser.add_argument("--o", dest='output', default="./scaled", type=str, help="Directory in which to save resized icons.")
    parser.add_argument("--b", dest='background', type=str, required=False, help="Colour with which to replace the alpha \
    channel. Use hex value, e.g. 0xffffff for white.")

    args = parser.parse_args()

    print(f"Will try to resize {args.input} and save the output to {args.output}.")
    if args.b is not None:
        print(f"Will replace the background with {args.background}")

    scalesList = [
        (20, [2, 3]),
        (29, [2, 3]),
        (40, [2, 3]),
        (60, [2, 3]),
        (20, [1, 2]),
        (29, [1, 2]),
        (40, [1, 2]),
        (76, [1, 2]),
        (83.5, [2]),
        (1024, [1]),
        (16, [1, 2]),
        (32, [1, 2]),
        (128, [1, 2]),
        (256, [1, 2]),
        (512, [1, 2]),
    ]

    image = Image.open(args.input)
    filename, ext = os.path.splitext(os.path.split(args.input)[1])

    for size, scales in scalesList:
        for scale in scales:
            print(f"{size} pt, {scale}x")
            pxSize = int(size*scale)
            resized_image = image.resize((pxSize, pxSize), PIL.Image.NEAREST)
            try:
                resized_image.save(os.path.join(args.output, f"{filename}-{size}pt-{scale}x{ext}"))
            except FileNotFoundError:
                print("Utputt-mappa finst ikkje. Du må opprette ho fyrst.")
                exit(1)


if __name__ == "__main__":
    main()
