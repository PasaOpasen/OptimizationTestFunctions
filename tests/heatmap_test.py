import sys
sys.path.append('..')
import numpy as np


from OptimizationTestFunctions import Sphere, Ackley, AckleyTest, Rosenbrock, Fletcher, Griewank, Penalty2, Quartic, Rastrigin, SchwefelDouble, SchwefelMax, SchwefelAbs, SchwefelSin, Stairs, Abs, Michalewicz, Scheffer, Eggholder, Weierstrass, plot_3d

dim = 2

funcs = [
        Sphere(dim, 2),
        Ackley(dim),
        AckleyTest(dim),
        Rosenbrock(dim),
        Fletcher(dim, seed = 1488),
        Griewank(dim),
        Penalty2(dim),
        Quartic(dim),
        Rastrigin(dim),
        SchwefelDouble(dim),
        SchwefelMax(dim),
        SchwefelAbs(dim),
        SchwefelSin(dim),
        Stairs(dim),
        Abs(dim),
        Michalewicz(),
        Scheffer(dim),
        Eggholder(dim),
        Weierstrass(dim)
    ]

for f in funcs:
    plot_3d(f, 
                 points_by_dim=70, 
                 title = type(f).__name__, 
                 bounds=None, 
                 show_best_if_exists= False, 
                 save_as = f"heatmap for {type(f).__name__}.png",
                 cmap = 'twilight',
                 plot_surface = True,
                 plot_heatmap = True)



