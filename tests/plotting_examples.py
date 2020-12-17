import sys
sys.path.append('..')


from OptimizationTestFunctions import Fletcher, plot_3d

# dim should be 2 for plotting 3D
dim = 2

# Fletcher is good function depends on random seed!

seed = 1
f1 = Fletcher(dim, seed)

# full available functional of plotting

plot_3d(f1, 
        points_by_dim = 70, 
        title = fr"{type(f1).__name__}\ with\ seed = {seed}", # LaTeX formula notation
        bounds = None, 
        show_best_if_exists = True, 
        save_as = "Fletcher1.png",
        cmap = 'twilight',
        plot_surface = True,
        plot_heatmap = True)


# disable arrow

plot_3d(f1, 
        points_by_dim = 70, 
        title = fr"{type(f1).__name__}\ with\ seed = {seed}",
        bounds = None, 
        show_best_if_exists = False, 
        save_as = "Fletcher2.png",
        cmap = 'twilight',
        plot_surface = True,
        plot_heatmap = True)


# select another bounds

plot_3d(f1, 
        points_by_dim = 70, 
        title = fr"{type(f1).__name__}\ with\ seed = {seed}",
        bounds = (-2, 6, -8, 10), 
        show_best_if_exists = False, 
        save_as = "Fletcher3.png",
        cmap = 'twilight',
        plot_surface = True,
        plot_heatmap = True)



# Create another Fletcher function

seed = 33

f2 = Fletcher(dim, seed)

# use another cmap

plot_3d(f2, 
        points_by_dim = 70, 
        title = fr"{type(f1).__name__}\ with\ seed = {seed}",
        bounds = None, 
        show_best_if_exists = False, 
        save_as = "Fletcher4.png",
        cmap = 'inferno',
        plot_surface = True,
        plot_heatmap = True)


# plot only 3D

plot_3d(f2, 
        points_by_dim = 70, 
        title = fr"{type(f1).__name__}\ with\ seed = {seed}",
        bounds = None, 
        show_best_if_exists = False, 
        save_as = "Fletcher5.png",
        cmap = 'inferno',
        plot_surface = True,
        plot_heatmap = False)


# plot only heatmap

plot_3d(f2, 
        points_by_dim = 70, 
        title = fr"{type(f1).__name__}\ with\ seed = {seed}",
        bounds = None, 
        show_best_if_exists = True, 
        save_as = "Fletcher6.png",
        cmap = 'inferno',
        plot_surface = False,
        plot_heatmap = True)















