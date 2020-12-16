import warnings
import numpy as np

class Noises:
    @staticmethod
    def uniform(low = 0, high = 0.1):
        return lambda value: np.random.uniform(low = low, high = high)

    @staticmethod
    def normal(center = 0, sd = 0.1):
        return lambda value: np.random.normal(loc = center, scale = sd)



class Transformation:

    def __init__(self, transformed_function, shift_step = None, rotation_matrix = None, noise_generator = None):

        if (shift_step is None) and (rotation_matrix is None) and (noise_generator) is None:
            warnings.warn("No sense of transformation when all preparations are None!")
            self.f = lambda arr: transformed_function(arr)

            return
        
        empty_func = lambda arr: arr

        if not (shift_step is None) and type(shift_step) == np.ndarray:

            self.shifter = lambda arr: arr - shift_step
        else:
            self.shifter = empty_func
        

        if not (rotation_matrix is None):
            if type(rotation_matrix) == np.ndarray:
                # create rotator
                pass
            else:
                assert (type(rotation_matrix) == int), "rotation_matrix is not int dim and not a matrix!"
                # init rotator
                pass
        else:
            self.rotator = empty_func

        
        self.noiser = lambda val:0 if noise_generator is None else noise_generator

        self.f = lambda arr: self.noiser(transformed_function(self.rotator(self.shifter(arr))))


    def __call__(self, arr):
        return self.f(arr)








