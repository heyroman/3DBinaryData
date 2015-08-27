from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.cm as cmx
import matplotlib.colors

# function visualizeIt calls prepare_plot() and then just draw plot

def visualizeIt(data):
    prepare_plot(data)
    plt.show()

# createPNG() calls prepare_plot() and then iteratively rotates an image capturing every frame into .png file

def createPNGs(data):
    ax = prepare_plot(data)

    # creating a bunch of *png for gif
    for n in range(0, 100):
        ax.azim = ax.azim + 3.6
        # if n >= 74 and n <= 76:
        #     ax.elev = ax.elev-0.2
        #     ax.azim = ax.azim+0.5 #end by panning/rotating slowly to stopping position
        plt.savefig('../images/images_for_gif/img' + str(n).zfill(3) + '.png',
                    bbox_inches='tight')
        print(n)
    plt.close()

# prepare_plot() receives numpy array 'data' and creates a 3d scatter coloured plot according to that data.
# this function does not actually draw the plot but simply adjust plot's settings, creates corresponding colormap
# and return a subplot object 'ax'

def prepare_plot(data):
    # rearranging data into 4 arrays (just for clarity)
    dataX = list(data[:, 0])
    dataY = list(data[:, 1])
    dataZ = list(data[:, 2])
    dataC = list(data[:, 3])

    # creating colormap according to present data
    cm = plt.get_cmap('brg')
    cNorm = matplotlib.colors.Normalize(vmin=min(dataC), vmax=max(dataC))
    scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=cm)

    # plotting
    fig = plt.figure()
    fig.set_facecolor('black')
    ax = fig.add_subplot(111, projection='3d', axisbg='k')
    ax.axis('off')
    ax.w_xaxis.set_pane_color((0, 0, 0))
    ax.w_yaxis.set_pane_color((0, 0, 0))
    ax.w_zaxis.set_pane_color((0, 0, 0))
    ax.grid(False)
    ax.scatter(dataX, dataY, dataZ, c=scalarMap.to_rgba(dataC), edgecolors=scalarMap.to_rgba(dataC), marker='.', s=5)
    scalarMap.set_array(dataC)
    plt.subplots_adjust(left=0.0, right=1.0, bottom=0.0, top=1.0)
    return ax