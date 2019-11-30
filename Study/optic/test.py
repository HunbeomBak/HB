import scipy as sc
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args , **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args , **kwargs)
        self._verts3d = xs, ys, zs
        
    def draw(self, renderer):
        xs3d , ys3d , zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d , ys3d , zs3d , renderer.M)
        self.set_positions((xs[0],ys[0]) ,(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)
        
fig = plt.figure()
fig.set_size_inches(12,7)
ax = fig.add_subplot(1,1,1,projection='3d')


x = sc.linspace(0, 2*sc.pi ,512)
y = sc.sin(x)
z = sc.zeros(x.size)
#plt.hold(True)
ax.plot(x,-y, z, 'k')
ax.plot(x,z,y,'k')

xv = sc.linspace(0,2*sc.pi ,16)
yv = sc.sin(xv)
yv = sc.sin(xv)

for i in range(len(xv)):
    a = Arrow3D([xv[i],xv[i]], [0 ,-yv[i]], [0,0], mutation_scale
                =40, lw=1, arrowstyle="-|>", ls='dashed', color='k')
    ax.add_artist(a)
    
    b = Arrow3D([xv[i], xv[i]], [0,0], [0,yv[i]], mutation_scale=20,
                lw=1, arrowstyle="-|>", ls='dotted', color='k')
    ax.add_artist(b)
    
a = Arrow3D([-0.5,2.2*sc.pi], [0,0], [0,0], mutation_scale=10, lw
            =1, arrowstyle="-|>", color="k")
ax.add_artist(a)

ax.set_xlim(0,7.5)
ax.set_ylim(-1.2, 1.2)
ax.set_zlim(-1.2, 1.2)
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_zticklabels([])
plt.axis('off')

ax.elev=40
ax.azim=-30

ax.text(2.3*sc.pi, 0,-0.2,r'$\vec{k}$')
ax.text(sc.pi/2, -1.2,0, r'$\vec{B}$')
ax.text(sc.pi/2, 0, 1.1, r'$\vec{E}$')


plt.show()


