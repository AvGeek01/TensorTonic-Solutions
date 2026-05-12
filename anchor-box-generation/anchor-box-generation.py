import numpy as np
def generate_anchors(feature_size, image_size, scales, aspect_ratios):
    """
    Generate anchor boxes for object detection.
    """
    if isinstance(feature_size, int):
        H = W = feature_size
    else:
        H, W = feature_size
    if isinstance(image_size,int):
        img_h=img_w=image_size
    else:
        img_h,img_w=image_size
    stride_h=img_h/H
    stride_w=img_w/W
    anchors=[]
    for y in range(H):
        for x in range(W):
            cx=(x+0.5)*stride_w
            cy=(y+0.5)*stride_h
            for scale in scales:
                for ratio in aspect_ratios:
                    w=scale*np.sqrt(ratio)
                    h=scale/np.sqrt(ratio)
                    x_min=cx-w/2
                    y_min=cy-h/2
                    x_max=cx+w/2
                    y_max=cy+h/2
                    anchors.append([x_min,y_min,x_max,y_max])
    return anchors