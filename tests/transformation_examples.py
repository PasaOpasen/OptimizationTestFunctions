# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 14:09:37 2020

@author: qtckp
"""

import sys
sys.path.append('..')

import numpy as np

from OptimizationTestFunctions import Weierstrass, plot_3d, Transformation, Noises

# dim should be 2 for plotting 3D
dim = 2

# Let's create Weierstrass function

f = Weierstrass(dim, a = 0.5, b = 5, kmax = 20)

# show it

plot_3d(f, 
        points_by_dim = 70, 
        title = f"{type(f).__name__}",
        bounds = None, 
        show_best_if_exists = True, 
        save_as = "Trans1.png",
        cmap = 'hot',
        plot_surface = True,
        plot_heatmap = True)


# transformation with shift

shifted_func = Transformation(f, shift_step=np.array([3, 4]))

# show it

plot_3d(shifted_func, 
        points_by_dim = 70, 
        title = "shifted",
        bounds = None, 
        show_best_if_exists = True, 
        save_as = "Trans2.png",
        cmap = 'hot',
        plot_surface = True,
        plot_heatmap = True)


# transformation with rotation

rotated_func = Transformation(f, rotation_matrix = dim, seed = 2) # random rotation matrix with dim 2

# show it

plot_3d(rotated_func, 
        points_by_dim = 70, 
        title = "rotated",
        bounds = None, 
        show_best_if_exists = True, 
        save_as = "Trans3.png",
        cmap = 'hot',
        plot_surface = True,
        plot_heatmap = True)





# transformation with noise

noised_func = Transformation(f, noise_generator = Noises.normal(center = 0, sd = 0.5)) 

# show it

plot_3d(noised_func, 
        points_by_dim = 70, 
        title = "noised",
        bounds = None, 
        show_best_if_exists = True, 
        save_as = "Trans4.png",
        cmap = 'hot',
        plot_surface = True,
        plot_heatmap = True)


# U can specify your noise behavior

def add_noise(current_val):
    if current_val > 5:
        return 0
    
    return current_val + np.random.random()/10

noised_func = Transformation(f, noise_generator = add_noise) 

plot_3d(noised_func, 
        points_by_dim = 70, 
        title = "noised",
        bounds = None, 
        show_best_if_exists = True, 
        save_as = "Trans5.png",
        cmap = 'hot',
        plot_surface = True,
        plot_heatmap = True)


# Also u can combine all these transformations 

new_func = Transformation(f,
                          shift_step= np.array([10, -10]),
                          rotation_matrix = 2, seed = 3,
                          noise_generator = Noises.uniform(-0.1, 0.5)
                          ) 

plot_3d(new_func, 
        points_by_dim = 70, 
        title = "mixed",
        bounds = None, 
        show_best_if_exists = True, 
        save_as = "Trans6.png",
        cmap = 'hot',
        plot_surface = True,
        plot_heatmap = True)










