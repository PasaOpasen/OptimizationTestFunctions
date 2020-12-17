import warnings
import numpy as np

class Noises:
    @staticmethod
    def uniform(low = 0, high = 0.1):
        return lambda value: value + np.random.uniform(low = low, high = high)

    @staticmethod
    def normal(center = 0, sd = 0.1):
        return lambda value: value + np.random.normal(loc = center, scale = sd)



class Transformation:

    def __init__(self, transformed_function, shift_step = None, rotation_matrix = None, noise_generator = None, seed = None):
        """
        Creates Transformation object

        Parameters
        ----------
        transformed_function : function or class callable object
            transformed function.
        shift_step : numpy 1D array/None, optional
            array of shifts by each dimension or None. The default is None.
        rotation_matrix : 2D-array/int/None, optional
            2D ortogonal rotation matrix or dimension for creating random rotation matrix or None if no rotate. The default is None.
        noise_generator : function, optional
            function gets current value and returns value with some noise. The default is None.
        seed : int, optional
            random seed for rotation matrix if needed reproduce. The default is None.

        """
        if not (seed is None):
            np.random.seed(seed)

        self.is_noised = not (noise_generator is None)
        self.is_rotated = not (rotation_matrix is None)
        self.is_shifted = not (shift_step is None)

        self.bounds = transformed_function.bounds
        if self.is_shifted:
            xmin, xmax, ymin, ymax = self.bounds
            self.bounds = xmin + shift_step[0], xmax + shift_step[0], ymin + shift_step[1], ymax + shift_step[1]
        #raise Exception()
        if (shift_step is None) and (rotation_matrix is None) and (noise_generator) is None:
            warnings.warn("No sense of transformation when all preparations are None!")
            self.f = lambda arr: transformed_function(arr)

            return
        
        empty_func = lambda arr: arr

        if self.is_shifted:
            
            assert (type(shift_step) == np.ndarray), "shift_step must be numpy array or None!"

            self.shifter = lambda arr: arr - shift_step
            self.unshifter = lambda arr: arr + shift_step
        else:
            self.shifter = empty_func
            self.unshifter = empty_func
        

        if self.is_rotated:
            if type(rotation_matrix) == np.ndarray:

                assert (np.allclose(rotation_matrix.T, np.linalg.inv(rotation_matrix))), f"Rotation matrix must be ortogonal!"

                # create rotator
                self.rotator = lambda arr: arr.dot(rotation_matrix)
            else:
                assert (type(rotation_matrix) == int), "rotation_matrix is not int dim and not a matrix!"
                # init rotator
                rotation_matrix, _ = np.linalg.qr(np.random.random((rotation_matrix, rotation_matrix)), mode='complete')
                self.rotator = lambda arr: arr.dot(rotation_matrix)
                self.unrotator = lambda arr: arr.dot(rotation_matrix.T)
        else:
            self.rotator = empty_func
            self.unrotator = empty_func
            self.is_rotated = False

        
        self.noiser = (lambda val: val) if noise_generator is None else noise_generator

        self.f = lambda arr: self.noiser(transformed_function(self.rotator(self.shifter(arr))))

        self.x_best = None
        self.f_best = None

        if not self.is_noised and hasattr(transformed_function, 'x_best'):
            if not (transformed_function.x_best is None):
                self.x_best = self.unrotator(self.unshifter(transformed_function.x_best))
                self.f_best = transformed_function(self.x_best)


    def __call__(self, arr):
        return self.f(arr)








