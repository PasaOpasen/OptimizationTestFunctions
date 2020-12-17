
from mpl_toolkits.mplot3d import Axes3D  
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator, LinearLocator, FormatStrFormatter

from matplotlib import cm

from OppOpPopInit import OppositionOperators


def get_good_arrow_place(optimum, bounds):
    opt = np.array(optimum)
    minimums = np.array([bounds[0], bounds[2]])
    maximums = np.array([bounds[1], bounds[3]])

    t1 = OppositionOperators.Continual.over(minimums, maximums)(opt)
    t2 = OppositionOperators.Continual.quasi_reflect(minimums, maximums)(t1)

    return tuple(t2)



def plot_3d(func, points_by_dim = 50, title = '', bounds = None, show_best_if_exists = True, save_as = None, cmap = 'twilight', plot_surface = True, plot_heatmap = True):
    """
    Plots function surface and/or heatmap

    Parameters
    ----------
    func : class callable object
        Object which can be called as function.
    points_by_dim : int, optional
        points for each dimension of plotting (50x50, 100x100...). The default is 50.
    title : str, optional
        title of plot with LaTeX notation. The default is ''.
    bounds : tuple, optional
        space bounds with structure (xmin, xmax, ymin, ymax). The default is None.
    show_best_if_exists : boolean, optional
        point best solution by arrow if x_best exists. The default is True.
    save_as : str/None, optional
        file path to save image (None if not needed). The default is None.
    cmap : str, optional
        color map of plot. The default is 'twilight'.
    plot_surface : boolean, optional
        plot 3D surface. The default is True.
    plot_heatmap : boolean, optional
        plot 2D heatmap. The default is True.
    """
    
    assert (plot_surface or plot_heatmap), "should be plotted at least surface or heatmap!"

    if bounds is None:
        bounds = func.bounds
    
    xmin, xmax, ymin, ymax = bounds

    x = np.linspace(xmin, xmax, points_by_dim)
    y = np.linspace(ymin, ymax, points_by_dim)


    a, b = np.meshgrid(x, y)
    
    data = np.empty((points_by_dim, points_by_dim))
    for i in range(points_by_dim):
        for j in range(points_by_dim):
            data[i,j] = func(np.array([x[i], y[j]]))
    
    a = a.T
    b = b.T

    l_a, r_a, l_b, r_b = xmin, xmax, ymin, ymax
    
    l_c, r_c = data.min(), data.max()

    levels = MaxNLocator(nbins=15).tick_values(l_c,r_c)

    if plot_heatmap and plot_surface:

        fig = plt.figure(figsize=(16, 6))
        ax1 = fig.add_subplot(1,2,1)
        ax2 = fig.add_subplot(1,2,2, projection='3d')
    else:
        fig = plt.figure()
        if plot_heatmap:
            ax1 = fig.gca()
        else:
            ax2 = fig.gca(projection='3d')

    title = r"$\bf{" + title+ r"}$"
    min_title = title[::]

    def base_plot():
        c = ax1.contourf(a, b, data , cmap=cmap, levels = levels, vmin=l_c, vmax=r_c)       
        name = title
        ax1.set_title( name, fontsize = 15)
        ax1.axis([l_a, r_a, l_b, r_b])
        fig.colorbar(c)

    if plot_surface:
        # Plot the surface.
        surf = ax2.plot_surface(a, b, data, cmap =  cmap,  linewidth=0, antialiased=False)

        # Customize the z axis.
        ax2.set_xlabel('first dim', fontsize=10)
        ax2.set_ylabel('second dim', fontsize=10)
        ax2.set_zlim(l_c, r_c)
        
        ax2.zaxis.set_major_locator(LinearLocator(4))
        #ax2.zaxis.set_major_formatter(FormatStrFormatter('%.2f'))

        # Add a color bar which maps values to colors.
        if not plot_heatmap: fig.colorbar(surf)#, shrink=0.5, aspect=5)
        
        ax2.contour(a, b, data, zdir='z', offset=0, cmap =  cmap)
        ax2.view_init(60, 35)
        ax2.set_title( min_title , fontsize = 15, loc = 'right')
    

    if not (func.x_best) is None:
        title += f"\n best solution: f{func.x_best} = {round(func(func.x_best))}"

        if show_best_if_exists and plot_heatmap:
            #xytext = tuple(np.array([(xmax+xmin)/2, (ymax+ymin)/2]) + np.random.uniform(-func.x_best/2, func.x_best/2, 2)) #tuple(np.random.uniform(0, min((xmax+xmin)/2, (ymax+ymin)/2), 2))

            xytext = get_good_arrow_place(func.x_best, bounds)

            bbox = dict(boxstyle ="round", fc ="0.8") 
            arrowprops = dict( 
                arrowstyle = "->", 
                connectionstyle = "angle, angleA = 0, angleB = 90, rad = 10")
    
            ax1.annotate(f'global minimum', xy= tuple(func.x_best), xytext = xytext,
                arrowprops=dict(facecolor='red', shrink=0.05), 
                #color = 'red',
                bbox = bbox#, arrowprops = arrowprops
                )

    if plot_heatmap: base_plot()


    fig.tight_layout()

    if save_as != None:
        plt.savefig(save_as, dpi = 250)
    
    plt.show()

    plt.close()





