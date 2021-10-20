import numpy as np
from PIL import Image as PILImage

def get_pseudo_color_map(pred):
    pred_mask = PILImage.fromarray(pred.astype(np.uint8), mode='P')
    color_map = get_color_map_list(256)
    pred_mask.putpalette(color_map)
    return pred_mask


def get_color_map_list(num_classes):
    """
    Returns the color map for visualizing the segmentation mask,
    which can support arbitrary number of classes.
    Args:
        num_classes (int): Number of classes.
    Returns:
        (list). The color map.
    """

    num_classes += 1
    color_map = num_classes * [0, 0, 0]
    for i in range(0, num_classes):
        j = 0
        lab = i
        while lab:
            color_map[i * 3] |= (((lab >> 0) & 1) << (7 - j))
            color_map[i * 3 + 1] |= (((lab >> 1) & 1) << (7 - j))
            color_map[i * 3 + 2] |= (((lab >> 2) & 1) << (7 - j))
            j += 1
            lab >>= 3
    # color_map = [color_map[i:i + 3] for i in range(0, len(color_map), 3)]
    color_map = color_map[3:]
    return color_map