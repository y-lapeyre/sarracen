import numpy as np

from sarracen.kernels import BaseKernel


class QuarticSplineKernel(BaseKernel):
    """
    An implementation of the Quartic Spline kernel, in 1, 2, and 3 dimensions.
    """

    def __init__(self, ndims):
        norm = 1 / 24 if (ndims == 1) else \
                96 / (1199 * np.pi) if (ndims == 2) else \
                1 / (20 * np.pi)

        super().__init__(2.5, ndims, norm, self._weight)

    @staticmethod
    def _weight(q):
        if q < 0.5:
            return ((5 / 2) - q) ** 4 - 5 * ((3 / 2) - q) ** 4 + 10 * ((1 / 2) - q) ** 4
        elif q < 1.5:
            return ((5 / 2) - q) ** 4 - 5 * ((3 / 2) - q) ** 4
        elif q < 2.5:
            return ((5 / 2) - q) ** 4
        else:
            return 0
