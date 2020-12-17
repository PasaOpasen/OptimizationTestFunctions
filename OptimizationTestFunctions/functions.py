#
#
# See also https://www.sfu.ca/~ssurjano/optimization.html
#
#



import math
import numpy as np


def easy_bounds(bound):
    return (-bound, bound, -bound, bound)

def check_dim(dim, min = 1):
    assert (type(dim) == int and dim >=min), f"Dimension should be int and not less than {min} for this function (got {dim})"


class Sphere:

    b = 5.12

    def __init__(self, dim, degree = 2):

        check_dim(dim, 1)

        self.deg = degree
        self.x_best = np.zeros(dim) if degree % 2 == 0 else None
        self.f_best = 0 if not (self.x_best is None) else None

        self.bounds = easy_bounds(Sphere.b)
    
    def __call__(self, vec):
        return sum((x**self.deg for x in vec))


class Ackley:
    
    b = 3

    def __init__(self, dim):

        check_dim(dim, 1)

        self.x_best = np.zeros(dim)
        self.f_best = 0

        self.bounds = easy_bounds(Ackley.b)

        self.bias = 20 + math.e
        self.pi2 = 2 * math.pi
    
    def __call__(self, vec):

        s1 = sum((x*x for x in vec))/vec.size
        s2 = sum((math.cos(self.pi2 * x) for x in vec))/vec.size


        return self.bias - 20*math.exp(-0.2*s1) - math.exp(s2)


class AckleyTest:
    
    b = 30

    def __init__(self, dim):

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

    def __init__(self, dim):

        check_dim(dim, 2)

        self.x_best = np.ones(dim)
        self.f_best = 0

        self.bounds = easy_bounds(Rosenbrock.b)

    
    def __call__(self, vec):

        s = sum(( 100 * (vec[i+1] - vec[i]**2) ** 2 + (vec[i] - 1)**2 for i in range(vec.size-1)))

        return s

class Fletcher:
    
    b = math.pi

    def __init__(self, dim, seed = None):

        if seed != None:
            np.random.seed(seed)

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
        return  sum((a-b)**2 for a, b in zip(self.A, B))


class Griewank:
    
    b = 600

    def __init__(self, dim):

        check_dim(dim, 1)

        self.x_best = np.zeros(dim)
        self.f_best = 0

        self.bounds = easy_bounds(Griewank.b)

    
    def __call__(self, vec):

        s = sum(( x*x for x in vec))/4000
        p = math.prod((math.cos(x/math.sqrt(i+1)) for i, x in enumerate(vec)))

        return 1 + s - p



class Penalty2:
    
    b = 50

    def __init__(self, dim, a=5, k=100, m=4):

        check_dim(dim, 2)

        self.x_best = np.ones(dim)
        self.f_best = 0

        self.bounds = easy_bounds(Penalty2.b)

        self.a, self.k, self.m = a, k, m
        self.pi2 = 2 * math.pi
        self.pi3 = 3 * math.pi

    
    def __call__(self, vec):

        a, k, m = self.a, self.k, self.m

        u = np.sum((vec[vec>a]-a)**m) + np.sum((-vec[vec<-a]-a)**m)

        s1 = 10 * math.sin(self.pi3*vec[0])**2 + (vec[-1]-1)**2 * (1 + math.sin(self.pi2 * vec[-1]**2))

        s2 = sum(((vec[i]-1)**2 * (1 + math.sin(self.pi3 * vec[i+1]**2)) for i in range(vec.size-1)))

        return k*u + 0.1 * (s1 + s2)


class Quartic:
    
    b = 1.28

    def __init__(self, dim):

        check_dim(dim, 1)

        self.x_best = np.zeros(dim)
        self.f_best = 0

        self.bounds = easy_bounds(Quartic.b)

    
    def __call__(self, vec):

        s = sum(( (i+1)*x**4 for i, x in enumerate(vec)))

        return s



class Rastrigin:
    
    b = 5.12

    def __init__(self, dim):

        check_dim(dim, 1)

        self.x_best = np.zeros(dim)
        self.f_best = 0

        self.bounds = easy_bounds(Rastrigin.b)


        self.pi2 = math.pi*2
        self.bias = 10*dim

    
    def __call__(self, vec):

        s = sum(( x*x - math.cos(self.pi2*x)*10 for x in vec))

        return self.bias + s


class SchwefelDouble:
    
    b = 65.536

    def __init__(self, dim):
        check_dim(dim)

        self.x_best = np.zeros(dim)
        self.f_best = 0

        self.bounds = easy_bounds(SchwefelDouble.b)


    
    def __call__(self, vec):

        cs = np.cumsum(vec)

        s = sum((cs[i]**2 for i in range(vec.size)))

        return s


class SchwefelMax:
    
    b = 100

    def __init__(self, dim):
        check_dim(dim)

        self.x_best = np.zeros(dim)
        self.f_best = 0

        self.bounds = easy_bounds(SchwefelMax.b)

    def __call__(self, vec):

        return np.abs(vec).max()

class SchwefelAbs:
    
    b = 10

    def __init__(self, dim):

        check_dim(dim)

        self.x_best = np.zeros(dim)
        self.f_best = 0

        self.bounds = easy_bounds(SchwefelAbs.b)

    def __call__(self, vec):

        mod = np.abs(vec)

        return np.sum(mod) + np.prod(mod)


class SchwefelSin:
    
    b = 500

    def __init__(self, dim):

        check_dim(dim, 1)

        self.x_best = np.full(dim, 420.9687)
        self.f_best = -12965.5

        self.bounds = easy_bounds(SchwefelSin.b)

    def __call__(self, vec):

        return -sum((x*math.sin(math.sqrt(abs(x))) for x in vec))


class Stairs:
    
    b = 6

    def __init__(self, dim):

        check_dim(dim)

        self.x_best = np.zeros(dim)
        self.f_best = 0

        self.bounds = easy_bounds(Stairs.b)

    def __call__(self, vec):

        return sum(( math.floor(x + 0.5)**2 for x in vec))


class Abs:
    
    b = 10

    def __init__(self, dim):

        check_dim(dim)

        self.x_best = np.zeros(dim)
        self.f_best = 0

        self.bounds = easy_bounds(Abs.b)

    def __call__(self, vec):

        return sum(( abs(x) for x in vec))


class Michalewicz:
    

    def __init__(self, m = 10):

        self.x_best = None
        self.f_best = None

        self.bounds = (0, math.pi, 0, math.pi)

        self.m = m*2

    def __call__(self, vec):

        return -sum(( math.sin(x)*math.sin((i+1)*x**2/math.pi)**self.m for i, x in enumerate(vec)))


class Scheffer:
    
    b = 7

    def __init__(self, dim):

        check_dim(dim, 2)

        self.x_best = np.zeros(dim)
        self.f_best = 0

        self.bounds = easy_bounds(Scheffer.b)


    def __call__(self, vec):

        return 0.5 + sum((  (math.sin( vec[i]**2 - vec[i+1]**2 )**2 - 0.5) / (1 + 0.001*(vec[i]**2 + vec[i+1]**2) )**2  for i in range(vec.size-1)))


class Eggholder:
    
    b = 512

    def __init__(self, dim):

        check_dim(dim, 2)

        self.x_best = None
        self.f_best = None

        self.bounds = easy_bounds(Eggholder.b)


    def __call__(self, vec):

        return -sum(( (vec[i+1] + 47) * math.sin(math.sqrt(abs(vec[i+1] + vec[i]/2 + 47))) + vec[i] * math.sin(math.sqrt(abs(vec[i]-vec[i+1] - 47))) for i in range(vec.size-1)))


class Weierstrass:
    
    b = 0.5

    def __init__(self, dim, a = 0.5, b = 3, kmax = 20):

        check_dim(dim, 1)

        self.x_best = np.zeros(dim)
        self.f_best = 0

        self.bounds = easy_bounds(Weierstrass.b)

        self.ak = np.array([a**k for k in range(kmax+1)])
        self.pibk = np.pi * np.array([b**k for k in range(kmax+1)])

        self.bias = -dim*np.sum(self.ak*np.cos(self.pibk))


    def __call__(self, vec):
    
        return self.bias + sum(( sum((ak * math.cos(x*pibk)  for ak, pibk in zip(self.ak, self.pibk) )) for x in vec*2 + 1 ))




if __name__ == '__main__':
    
    arr = np.array([0.1, 0.2, 0.3])
    
    dim = arr.size
    
    funcs = [
        Sphere(dim, degree = 2),
        Ackley(dim),
        AckleyTest(dim),
        Rosenbrock(dim),
        Fletcher(dim, seed = None),
        Griewank(dim),
        Penalty2(dim, a=5, k=100, m=4),
        Quartic(dim),
        Rastrigin(dim),
        SchwefelDouble(dim),
        SchwefelMax(dim),
        SchwefelAbs(dim),
        SchwefelSin(dim),
        Stairs(dim),
        Abs(dim),
        Michalewicz(m = 10),
        Scheffer(dim),
        Eggholder(dim),
        Weierstrass(dim, a = 0.5, b = 3, kmax = 20)
    ]

    

    for f in funcs:
        print(f(arr))

















