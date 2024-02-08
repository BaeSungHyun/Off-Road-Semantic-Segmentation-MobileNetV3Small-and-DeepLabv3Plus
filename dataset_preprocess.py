import glob
import pdb
import os
import shutil
from collections import OrderedDict

import cv2
import numpy as np


LABEL_TO_COLOR = OrderedDict({
     "background": [255, 255, 255],
     "high_vegetation": [40, 80, 0],
     "traversable_grass": [128, 255, 0],
     "smooth_trail": [178, 176, 153],
     "obstacle": [255, 0, 0],
     "sky": [1, 88, 255],
     "rough_trial": [156, 76, 30],
     "puddle": [255, 0, 128],
     "non_traversable_low_vegetation": [0, 160, 0]
})

PALETTE = list(LABEL_TO_COLOR.values())
CLASSES = list(LABEL_TO_COLOR.keys())


def main():
    print("Palette: ", PALETTE)
    print("Classes: ", CLASSES)
    convert_structure()
    convert_labels()
    print("New label value for class:")
    for idx, cls in enumerate(CLASSES):
        print(f"{cls:<35}{idx}")


def convert_structure():
    for old_split, new_split in zip(["train", "valid"], ["training", "validation"]):
        img_dir = f"yamaha/images/{new_split}"
        ann_dir = f"yamaha/annotations/{new_split}"
        os.makedirs(img_dir, exist_ok=True)
        os.makedirs(ann_dir, exist_ok=True)
        dirs = glob.glob(f"yamaha/{old_split}/*")
        dirs = sorted([d for d in dirs if os.path.isdir(d)])

        for idx, d in enumerate(dirs):
            lp = os.path.join(d, "labels.png")
            imp = os.path.join(d, "rgb.jpg")
            shutil.copy2(imp, os.path.join(img_dir, f"YCOR_{idx:08d}.jpg"))
            shutil.copy2(lp, os.path.join(ann_dir, f"YCOR_{idx:08d}.png"))


def convert_labels():
    for split in ["training", "validation"]:
        path = f"yamaha/annotations/{split}/*"
        names = glob.glob(path)

        for idx, n in enumerate(sorted(names)):
            print(f"Split {split}:{idx}/{len(names)}", end="\r")
            img = cv2.cvtColor(cv2.imread(n), cv2.COLOR_BGR2RGB)
            h, w = img.shape[:2]
            img = img.reshape(-1, 3)

            new_img = np.empty_like(img[:, 0])
            new_img.fill(255)
            for idx, c in enumerate(PALETTE):
                matching = np.all(img == c, axis=1)
                new_img[matching] = idx
            if 255 in np.unique(new_img):
                print("Missing")
                pdb.set_trace()
            cv2.imwrite(n, new_img.reshape(h, w))
        print()


if __name__ == "__main__":
    main()
