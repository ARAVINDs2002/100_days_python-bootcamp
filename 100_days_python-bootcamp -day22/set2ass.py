import numpy as np
heights = [1, 2, 3, 4, 5]
l1_norm = np.linalg.norm(heights, ord=1)
l2_norm = np.linalg.norm(heights, ord=2)
dmax_norm = np.linalg.norm(heights, ord=np.inf)
print(f"L1 Norm: {l1_norm}")#x1+x2+....xn
print(f"L2 Norm (Euclidean Norm): {l2_norm}")#rootofx1sq+x2sq+x3sq+....xnsq
print(f"Maximum (Dmax) Norm: {dmax_norm}")#max value in a list


