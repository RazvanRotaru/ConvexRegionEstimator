import unittest

from directory_helper import DirContent, images_dir
from image_helper import Image


class ImageInformationTest(unittest.TestCase):

    def test_sizes(self):
        for file in DirContent(images_dir):
            self.assertEqual((1421, 1126), Image(file).shape())

    def test_depth(self):
        for file in DirContent(images_dir):
            self.assertEqual(8, Image(file).depth())


if __name__ == '__main__':
    unittest.main()
