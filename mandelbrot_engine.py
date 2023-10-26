import numpy as np
from numba import njit, vectorize, prange, guvectorize, int64, complex128
from time import time

def generate(xmin, xmax, ymin, ymax, xresolution, yresolution, maxDepth):
    # time
    start = time()


    # mandelbrot
    re = np.linspace(xmin, xmax, xresolution)
    im = np.linspace(ymax, ymin, yresolution) * 1j

    x, y = np.meshgrid(re, im)
    input_array = x + y

    @vectorize(nopython=True)
    def scalar_computation(z, maxDepth):
        multiplier = float(256 / (maxDepth+1))
        curr = 0
        for currDepth in range(maxDepth):
            curr = curr**2 + z
            if np.abs(curr) > 2:
                return int(currDepth * multiplier)
        return 0

    @njit(parallel=True)
    def parallel(input_array, maxDepth):
        output = np.empty(input_array.shape[0]*input_array.shape[1]*3, dtype=np.byte)
        for i in prange(input_array.shape[0]):
            for j in prange(input_array.shape[1]):
                pos = 3 * (i*xresolution + j)
                pixel_value = scalar_computation(input_array[i][j], maxDepth)
                output[pos] = pixel_value
                output[pos+1] = pixel_value
                output[pos+2] = pixel_value
        return output

    z = parallel(input_array, maxDepth)


    print("Elapsed: {:.2f}".format(time() - start))
    return z