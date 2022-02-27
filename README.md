# icon-resizer
Image resizer for making iOS and macOS icons. In addition to resizing, the
program is capable of removing alpha channel from an icon.

## Usage
usage: `resize.py [-h] [--i INPUT] [--o OUTPUT] [--b BACKGROUND]`

optional arguments:
```
  -h, --help      show this help message and exit
  --i INPUT       The original icon.
  --o OUTPUT      Directory in which to save resized icons.
  --b BACKGROUND  Colour with which to replace the alpha channel. Use hex
                  value, e.g. 0xffffff for white.
