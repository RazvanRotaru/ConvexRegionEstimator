import matplotlib.pyplot as plt
import numpy as np

from file_helper import File
from path_helper import Path


class Image(File):

    def __init__(self, path: Path):
        super().__init__(path)

        if 'tif' in self.extension():
            self._img = Image.read_tiff(self.path)

    @staticmethod
    def normalize(img):
        # return 255*(img - img.min())/(img.max() - img.min())
        return img
        # return cv.normalize(img, None, alpha=0, beta=1, norm_type=cv.NORM_MINMAX, dtype=cv.CV_8UC1) * 255

    @staticmethod
    def read_tiff(path) -> np.array:
        return np.array(Image.normalize(plt.imread(path)))

    def plot(self):
        plt.imshow(self._img)
        plt.show()

    def shape(self):
        return self._img.shape[:2]

    def size(self):
        return self._img.size

    def depth(self):
        return self._img.itemsize * 8

    def __getitem__(self, tup):
        x, y = tup
        return self._img[x, y]

    @property
    def img(self):
        return self._img

# i = Image(DirContent(images_dir).at(0))._img
# print(i)
