import unittest

from directory_helper import DirContent, images_dir
from labeled_image import LabeledImage


class LabeledImageTest(unittest.TestCase):

    def test_categories(self):
        for file in DirContent(images_dir):
            self.assertEqual(7, len(LabeledImage(file).class_prob))


if __name__ == '__main__':
    unittest.main()
