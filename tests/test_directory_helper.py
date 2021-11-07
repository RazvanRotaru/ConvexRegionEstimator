import unittest

from directory_helper import DirContent, images_dir, advertisements_dir, zones_dir
from file_helper import File


class ImageDirectoryTest(unittest.TestCase):
    expected = ['242_0_2638730_0_5D1327B5',
                '242_10_2638730_19_5D132A6D',
                '242_12_2638730_20_5D132A8C',
                '242_14_2638730_22_5D132AD1',
                '242_16_2638730_24_5D132B0E']

    def test_content(self):
        for i, file in enumerate(DirContent(images_dir)):
            self.assertEqual(self.expected[i], File(file).name())

    def test_images_number(self):
        self.assertEqual(5, len(DirContent(images_dir)))

    def test_advertisements_number(self):
        self.assertEqual(30, len(DirContent(advertisements_dir)))

    def test_zones_number(self):
        self.assertEqual(40, len(DirContent(zones_dir)))

    def test_content_at(self):
        self.assertEqual(self.expected[0], File(DirContent(images_dir).at(0)).name())


if __name__ == '__main__':
    unittest.main()
