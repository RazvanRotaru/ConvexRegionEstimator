import os
import unittest

from path_helper import Path


class PathHelperTest(unittest.TestCase):
    def test_project_dir(self):
        expected = os.path.abspath(os.path.join(os.getcwd(), '..'))
        self.assertEqual(expected, Path.project_path())


if __name__ == '__main__':
    unittest.main()
