
import geatpy as ea
import numpy as np
import math

# objective functions
def residual_square(pred_arr, gt_arr):
    return np.sum(np.square(pred_arr-gt_arr))

