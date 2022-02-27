import unittest
from resize import parse_hex, mix_colours, mix_channels


class HexParsingTestCase(unittest.TestCase):
    def test_correct_patterns(self):
        self.assertEqual((255, 255, 255), parse_hex('0xFFFFFF'))
        self.assertEqual((0x12, 0x34, 0x56), parse_hex('0x123456'))
        self.assertEqual((0, 0, 0), parse_hex('0x000000'))


class ColourMixingTestCase(unittest.TestCase):
    def test_channel_mixing(self):
        self.assertEqual(
            255,
            mix_channels((0, 255), (255, 255)),
            "cover totally with white"
        )
        self.assertEqual(
            0,
            mix_channels((255, 255), (0, 255)),
            "cover totally with black"
        )
        self.assertEqual(
            191,
            mix_channels((255, 127), (255, 128)),
            "two times white at 50 % opacity"
        )

    def test_colour_mixing(self):
        self.assertEqual(
            (255, 255, 255, 255),
            mix_colours((0, 0, 0, 255), (255, 255, 255, 255)),
            "cover totally with white")
        self.assertEqual(
            (0, 0, 0, 255),
            mix_colours((255, 255, 255, 0), (0, 0, 0, 255)),
            "cover totally with black"
        )
        self.assertEqual(
            (255, 255, 255, 191),
            mix_colours((255, 255, 255, 127), (255, 255, 255, 128)),
            "two times white at 50 % opacity"
        )


if __name__ == '__main__':
    unittest.main()
