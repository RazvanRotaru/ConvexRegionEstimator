import os
from os import listdir
from os.path import isfile

from path_helper import Path

images_dir = Path('Data/CCS/Detectie_Regiuni_Poligonale')

advertisements_dir = Path.combine(images_dir, path='Results/Adv')
zones_dir = Path.combine(images_dir, path='Results/Zones')


class DirContent:
    def __init__(self, path: Path):
        self._files = []
        self._length = 0
        self._index = 0

        for image in DirContent.get_content(path.path):
            self._files.append(Path.combine(path, image))
            self._length += 1

    def __len__(self):
        return self._length

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < self._length:
            result = self._files[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration

    def at(self, index: int):
        return self._files[index]

    @staticmethod
    def get_content(directory):
        return [f for f in listdir(directory) if isfile(Path(root_dir=directory, path=f).path)]
