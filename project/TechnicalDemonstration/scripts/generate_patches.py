from os.path import basename
from pathlib import Path
from PIL import Image
import random
import traceback

from openslide import OpenSlide
import cv2

'''
This script is to generate test patches for the tcga slides.
'''



def is_tissue(img):
    """Checking if it's purple crop.
    """
    color = img.convert('RGB').resize((1, 1), Image.ANTIALIAS).getpixel((0, 0))
    r = color[0] / 255
    g = color[1] / 255
    b = color[2] / 255
    return r > g*1.1 and b > g*1.1 and (r+b)/2 > 0.5


def extract_patches(image_path, output_path, target_level=0, output_size=[256, 256], stride=128,exist_ok=True):
    """ Extract tissue patches from a slide image (.tif) and put them
    in /pos and /neg directories based on overlap with annotation masks.

    Args:
        exist_ok: overwrite if output folder already exists. (For resuming task, set False (default).)
    """
    img = OpenSlide(image_path)
    size_original = img.level_dimensions[0]
    size = img.level_dimensions[target_level]
    ds_factor = img.level_downsamples[target_level]
    stride_adjusted = int(stride*ds_factor)

    op = img.properties.get('openslide.objective-power')
    if op == '20':
        stride_adjusted = int(stride_adjusted//2)
        output_size = [int(s//2) for s in output_size]
    elif op == '40':
        pass
    else:
        print(f"Warning: Irregular objective-power {op} in {image_path}")

    output_size_at_0 = [s*ds_factor for s in output_size]
    image_basename = basename(image_path).split('.')[0].lower()
    num_cols = int(size_original[0] // (stride_adjusted))  # X
    num_rows = int(size_original[1] // (stride_adjusted))  # Y

    for r in range(num_rows):
        for c in range(num_cols):
            top_left = (c*stride_adjusted, r*stride_adjusted)
            patch = img.read_region(top_left, target_level, output_size).convert('RGB')
            if is_tissue(patch):
                patch.save('{}/{}_{}_{}.png'.format(output_path,image_basename, *top_left))


if __name__ == '__main__':
    """Extract patches using OpenSlide
    """

    #TODO: Set Paths
    #Assumption: wsi/<partition>/<class>/<images>.svs
    wsi_dir = Path(
        "REPLACE_WITH_ACTUAL_VALUE")
    output_path_root = Path(
        "REPLACE_WITH_ACTUAL_VALUE")

    #TODO: Set Parameters
    target_level = "REPLACE_WITH_ACTUAL_VALUE"
    output_size = "REPLACE_WITH_ACTUAL_VALUE"
    stride = "REPLACE_WITH_ACTUAL_VALUE"

    for slide_path in wsi_dir.rglob("*.svs"):
        class_name = slide_path.parent.name
        partition = slide_path.parents[1].name
        slide_name = slide_path.stem.split('.')[0]

        output_path = output_path_root / partition / class_name / slide_name
        output_path.mkdir(parents=True, exist_ok=True)

        print("Processing: {}".format(slide_path))
        try:
            extract_patches(
                image_path=slide_path,
                output_path=str(output_path.absolute()),
                target_level=target_level,
                output_size=output_size,
                stride=stride,
                exist_ok=False)
        except OSError:
            print("Folder exists: already processed")
        except Exception as e:
            print(traceback.print_exc())
