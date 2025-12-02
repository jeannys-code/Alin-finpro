# utils/background_removal.py
import numpy as np
import cv2

def _rgb_to_bgr(img):
    return cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

def _bgr_to_rgb(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def remove_background(img_np, method="HSV Threshold", hsv_lower=(0,0,0), hsv_upper=(180,255,220)):
    """
    img_np: RGB uint8 ndarray HxWx3
    method: "HSV Threshold" or "GrabCut"
    hsv_lower/upper: tuples (H,S,V) in OpenCV scale (H:0-180, S:0-255, V:0-255)
    Returns RGB image with background replaced by white (or transparent if requested).
    """
    if method == "HSV Threshold":
        bgr = _rgb_to_bgr(img_np)
        hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
        lower = np.array(hsv_lower, dtype=np.uint8)
        upper = np.array(hsv_upper, dtype=np.uint8)
        mask = cv2.inRange(hsv, lower, upper)
        # mask = 255 where inside range; we interpret as foreground if NOT in threshold area
        # typical use: if threshold picks background color, invert
        # We'll assume threshold chosen to pick background, so invert to get foreground
        fg_mask = cv2.bitwise_not(mask)
        fg_mask = cv2.medianBlur(fg_mask, 5)
        # create 3-channel mask
        fg = cv2.bitwise_and(bgr, bgr, mask=fg_mask)
        bg = 255 * np.ones_like(bgr, dtype=np.uint8)
        inv_mask = cv2.bitwise_not(fg_mask)
        bg_part = cv2.bitwise_and(bg, bg, mask=inv_mask)
        res_bgr = cv2.add(fg, bg_part)
        res_rgb = _bgr_to_rgb(res_bgr)
        return res_rgb

    elif method == "GrabCut":
        bgr = _rgb_to_bgr(img_np)
        h, w = bgr.shape[:2]
        mask = np.zeros((h,w), np.uint8)  # 0 = bg, 1=fg probable, 2=bg sure, 3=fg sure
        rect = (int(w*0.05), int(h*0.05), int(w*0.9), int(h*0.9))
        bgdModel = np.zeros((1,65), np.float64)
        fgdModel = np.zeros((1,65), np.float64)
        cv2.grabCut(bgr, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
        # mask==2 or mask==0 -> background
        mask2 = np.where((mask==2)|(mask==0), 0, 1).astype('uint8')
        res_bgr = bgr * mask2[:,:,None]
        # put white background where mask2==0
        white = 255*np.ones_like(bgr, dtype=np.uint8)
        res_bgr = np.where(mask2[:,:,None]==1, res_bgr, white)
        res_rgb = _bgr_to_rgb(res_bgr)
        return res_rgb

    else:
        raise ValueError("Unknown method")
