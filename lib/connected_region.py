from collections import namedtuple
from typing import Any, Callable

import matplotlib.colors
import matplotlib.pyplot
import numpy as np


class ConnectedRegionDetector:
    min_region_size = 20

    def __init__(self, image):
        self._regions = {}
        self._colors = {}
        self._L = 0
        self._EQ = {}

        self._image = image
        self._aux = np.zeros(image.shape)
        self._detect_regions()

    def __len__(self):
        return len(self._regions.keys())

    def regions(self):
        return self._regions.keys()

    def is_empty(self):
        return self._L == 0

    def get_regions(self):
        return self._regions.values()

    def _detect_regions(self):
        for i in range(self._image.shape[0]):
            for j in range(self._image.shape[1]):
                self.assign_regions(i, j)

        self.merge_common_regions()

    def assign_regions(self, x, y):
        Pixel = namedtuple('Pixel', 'index, value, region')
        pixel_at: Callable[[Any], Pixel] = lambda pos: Pixel(pos, self._image[pos], self._aux[pos])

        cur = pixel_at((x, y))

        if cur.value <= 0:
            return

        if x == 0 and y == 0:
            self.__assign_new_region(x, y)
            return

        if y == 0:
            if cur.value == self._aux[x - 1, 0]:
                self._aux[x, 0] = self._aux[x - 1, 0]
            else:
                self.__assign_new_region(x, y)
            return

        if x == 0:
            if cur.value == self._aux[0, y - 1]:
                self._aux[0, y] = self._aux[0, y - 1]
            else:
                self.__assign_new_region(x, y)
            return

        top = pixel_at((x - 1, y))
        left = pixel_at((x, y - 1))

        if cur.value == left.value and cur.value != top.value:
            self._aux[x, y] = left.region
            return

        if cur.value != left.value and cur.value == top.value:
            self._aux[x, y] = top.region
            return

        if cur.value != left.value and cur.value != top.value:
            self.__assign_new_region(x, y)
            return

        if cur.value == left.value and cur.value == top.value:
            if left.region == top.region:
                self._aux[x, y] = left.region
            else:
                label = left.region if left.region in self._EQ.keys() else top.region
                self._aux[x, y] = label

                if label in self._EQ.keys():
                    self._EQ[label].update([left.region, top.region])
                else:
                    self._EQ[label] = {left.region, top.region}

    def __assign_new_region(self, x, y):
        self._L += 1
        # self._regions[self._L] = set()
        self.__append_to_region(x, y)

    def __append_to_region(self, x, y):
        # self._regions[self._L].add((x, y))
        self._aux[x, y] = self._L

    def merge_common_regions(self):
        relabels = self.reverse_labels()

        for x in range(self._aux.shape[0]):
            for y in range(self._aux.shape[1]):
                if self._aux[x, y] in relabels.keys():
                    region_label = relabels[self._aux[x, y]]
                    self._aux[x, y] = region_label

                    if region_label in self._regions.keys():
                        self._regions[region_label].add((x, y))
                    else:
                        self._regions[region_label] = {(x, y)}

    def show_regions(self):
        img = np.zeros((*self._aux.shape, 3))
        self._get_colors()

        for x in range(self._aux.shape[0]):
            for y in range(self._aux.shape[1]):
                if self._aux[x, y] not in self._colors.keys():
                    img[x, y] = ConnectedRegionDetector._get_color(0)
                else:
                    img[x, y] = self._colors[self._aux[x, y]]

        # matplotlib.pyplot.imshow(img)
        # matplotlib.pyplot.show()

        return img

    def _get_colors(self):
        colors_no = len(self)
        colors_dif = 16777215 / (colors_no + 1)
        cur_color = colors_dif

        for region in self._regions.keys():
            self._colors[region] = ConnectedRegionDetector._get_color(cur_color)
            cur_color += colors_dif
        self._colors[0] = ConnectedRegionDetector._get_color(0)

    @staticmethod
    def _get_color(color):
        return matplotlib.colors.to_rgb(ConnectedRegionDetector._get_color_code(color))

    @staticmethod
    def _get_color_code(value: float):
        return format(int(value), '#08x').upper().replace('0X', '#')

    def merge_labels(self):
        merged_labels = {}
        to_ignore = []
        for key in self._EQ.keys():
            if key in to_ignore:
                continue

            merged_labels[key] = set()
            self.insert_key_recursively(key, key, merged_labels, to_ignore)

        self._EQ = merged_labels

    def insert_key_recursively(self, key, insert_at, merged_labels, to_ignore):
        merged_labels[insert_at].add(key)

        values = self._EQ[key]

        for value in values:
            if value in self._EQ.keys() and value not in merged_labels[insert_at]:
                to_ignore.append(value)
                self.insert_key_recursively(value, insert_at, merged_labels, to_ignore)

    def reverse_labels(self):
        self.merge_labels()

        reversed_labels = {}
        for key, values in self._EQ.items():
            for value in values:
                reversed_labels[value] = key

        return reversed_labels

# l = LabeledImage(DirContent(images_dir).at(0))
# c = ConnectedRegionDetector(l.labels)
#
# print(len(c))
# print(c.regions())
#
# c.show_regions()
