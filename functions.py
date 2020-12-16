
import math
import numpy as np


def easy_bounds(bound):
    return (-bound, bound, -bound, bound)

def check_dim(dim, min = 1):
    assert (type(dim) == int and dim >=min), f"Dimension should be int and not less than {min} for this function (got {dim})"


class Sphere:

    b = 5.12

    def __init__(self, degree = 2):

        self.deg = degree
        self.x_best = 0 if degree % 2 == 0 else None
        self.f_best = 0 if self.x_best != None else None

        self.bounds = easy_bounds(Sphere.b)
    
    def __call__(self, vec):
        return sum((x**self.deg for x in vec))


class Ackley:
    
    b = 30

    def __init__(self):

        self.x_best = 0
        self.f_best = 0

        self.bounds = easy_bounds(Ackley.b)

        self.bias = 20+np.e
        self.twopi = 2*np.pi
    
    def __call__(self, vec):

        s1 = sum((x*x/(i+1) for i, x in enumerate(vec)))
        s2 = sum((math.cos(self.twopi * x)/(i+1) for i, x in enumerate(vec)))


        return self.bias - 20*math.exp(-0.2*s1) - math.exp(s2)


class AckleyTest:
    
    b = 30

    def __init__(self, dim = 2):

        check_dim(dim, 2)

        self.x_best = None
        self.f_best = None

        self.bounds = easy_bounds(AckleyTest.b)

        self.exp = math.exp(-0.2)
    
    def __call__(self, vec):

        s = sum((3*(math.cos(2*vec[i]) + math.sin(2*vec[i+1])) + self.exp * math.sqrt(vec[i]**2 + vec[i+1]**2) for i in range(vec.size-1)))

        return s


class Rosenbrock:
    
    b = 2.048

    def __init__(self, dim = 2):

        check_dim(dim, 2)

        self.x_best = np.ones(dim)
        self.f_best = 0

        self.bounds = easy_bounds(Rosenbrock.b)

    
    def __call__(self, vec):

        s = sum(( 100 * (vec[i+1] - vec[i]**2) ** 2 + (vec[i] - 1)**2 for i in range(vec.size-1)))

        return s

class Fletcher:
    
    b = math.pi

    def __init__(self, dim = 2):

        check_dim(dim, 1)

        self.x_best = np.random.uniform(-np.pi, np.pi, dim)
        self.f_best = 0
        self.bounds = easy_bounds(Fletcher.b)

        self.a = np.random.uniform(-100, 100, (dim, dim))
        self.b = np.random.uniform(-100, 100, (dim, dim))

        self.A = np.sum(self.a * np.sin(self.x_best) + self.b * np.cos(self.x_best), axis = 0)


        

    
    def __call__(self, vec):

        B = np.sum(self.a * np.sin(vec) + self.b * np.cos(vec) ,axis = 0)
        #raise Exception()
        return np.sum(self.A - B)








if __name__ == '__main__':

    funcs = [
        Sphere(2),
        Ackley(),
        AckleyTest(),
        Rosenbrock(3),
        Fletcher(3)
    ]

    arr = np.array([1, 2, 3])

    for f in funcs:
        print(f(arr))

















