import time

import matplotlib.pyplot
import numpy as np

from connected_region import ConnectedRegionDetector
from directory_helper import advertisements_dir, zones_dir, DirContent, images_dir
from file_helper import File
from image_helper import Image
from path_helper import Path


class LabeledImage(Image):
    class_prob = [None]
    thresh = 100

    def __init__(self, path: Path):
        super().__init__(path)

        self.labels = np.ones(self._img.shape) * LabeledImage.thresh
        self.probabilities = []

        self._extract_class_probabilities(advertisements_dir)
        self._extract_class_probabilities(zones_dir)

        self.labels = np.array(self.probabilities).argmax(axis=0)
        self.x = np.dstack(self.probabilities)

    def _extract_class_probabilities(self, directory):

        for filename in DirContent(directory):
            file = File(filename)
            if self.name() in file.name() and 'tif' in file.extension():
                prob = file.name().split('_')[-1]
                self.class_prob.append(prob)
                blue_channel = 255 - Image.read_tiff(file.path)[:, :, 1]
                blue_channel[blue_channel < LabeledImage.thresh] = 0
                self.probabilities.append(blue_channel)


t0 = time.time()
l = LabeledImage(DirContent(images_dir).at(3))
print(l.labels)
print(l.shape())
c = ConnectedRegionDetector(l.labels)
regions = c.show_regions()

img = l.img

# overlay = cv2.addWeighted(img, regions)

matplotlib.pyplot.imshow(img)
matplotlib.pyplot.imshow(regions, alpha=0.6)
matplotlib.pyplot.show()
t = time.time() - t0

print(f'took: {t}ms')
# TODO add mask visualization
# TODO convex area
