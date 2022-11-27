#from cmath import sin
import matplotlib.pyplot as plt
import numpy as np
import time
import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
from random import randint



def fanc1 (x,y):      # Функция Матьяса  -10:10
    return 0.26 * (x*x + y*y) - 0.48*x*y

def dx1(x,y):
    return (0.52*x - 0.48*y)

def dy1(x,y):
    return ((-0.48*x + 0.52*y))

def gradfanc1 (x,y):
    return np.array([(0.52*x - 0.48*y), (-0.48*x + 0.52*y)])

def fanc2 (x,y): # Функция Химмельблау -5:5 
    return (x * x + y - 11)**2 + (x + y * y - 7)**2

def dx2(x,y):
    return (4*x*(x**2 + y -11) + 2*(x + y**2 -7))

def dy2(x,y):
    return (2*(x**2 + y - 11) + 4*y*(x + y**2 - 7))

def fanc3 (x, y):       # Eggholder -512:512
     return (-(y + 47) * np.sin(np.sqrt(np.fabs((x/2) + (y + 47)))) - x * np.sin(np.sqrt(np.fabs(x - (y + 47))))) 

def dx3(x,y):
    return ((x * np.cos(np.sqrt(np.fabs(x - y - 47))))/(2 * np.sqrt(np.abs(x - y - 47)))) + (((-y - 47) * np.cos(np.sqrt(np.abs((x/2) + y + 47))))/(4 * np.sqrt(np.abs((x/2) + y + 47)))) - np.sin(np.sqrt(np.abs(x - y - 47)))

def dy3(x,y):
    return ((x * np.cos(np.sqrt(np.fabs(x - y - 47))))/(2 * np.sqrt(np.abs(x - y - 47)))) + (((-y - 47) * np.cos(np.sqrt(np.abs((x/2) + y + 47))))/(4 * np.sqrt(np.abs((x/2) + y + 47)))) - np.sin(np.sqrt(np.abs((x/2) + y + 47)))



def getplot2d(axissize, func, inlog):

    xgrid, ygrid = np.meshgrid(axissize, axissize)
    zgrid = func(xgrid,ygrid)
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(projection='3d', elev = 47, azim = -43)
    
    ax_3d.contour(xgrid, ygrid, zgrid, cmap='rainbow')
    # ax_3d.plot_surface(xgrid, ygrid, zgrid, cmap='rainbow', alpha=0.5)

    # for i in range(len(inlog) - 1):
    #     ax_3d.plot(np.linspace(inlog[i][0], inlog[i+1][0], 2),np.linspace(inlog[i][1], inlog[i+1][1], 2),np.linspace(inlog[i][2], inlog[i+1][2], 2), c='green', alpha = 1)
    
    # ax_3d.scatter(inlog[(len(inlog))-1][0],inlog[(len(inlog))-1][1],inlog[(len(inlog))-1][2], c='red')
    
    for i in range(len(inlog) - 1):
        ax_3d.plot(np.linspace(inlog[i][0], inlog[i+1][0], 2),np.linspace(inlog[i][1], inlog[i+1][1], 2),np.linspace(inlog[i][2], inlog[i+1][2], 2), c='green', alpha = 1)
    
    ax_3d.scatter(inlog[(len(inlog))-1][0],inlog[(len(inlog))-1][1],inlog[(len(inlog))-1][2], c='red')
    
    plt.show()




xgrid, ygrid = np.meshgrid(a, a)
zgrid = fanc2(xgrid,ygrid)

fig = plt.figure(figsize=(10, 8))
ax_3d = Axes3D(fig, elev = 47, azim = -43)
ax_3d.plot_surface(xgrid, ygrid, zgrid, cmap='rainbow', alpha=0.5)


for i in range(len(gdhim) - 1):
    ax_3d.plot(np.linspace(gdhim[i][0], gdhim[i+1][0], 2),np.linspace(gdhim[i][1], gdhim[i+1][1], 2),np.linspace(gdhim[i][2], gdhim[i+1][2], 2), c='brown', alpha = 1)

for i in range(len(gdmhim) - 1):
    ax_3d.plot(np.linspace(gdmhim[i][0], gdmhim[i+1][0], 2),np.linspace(gdmhim[i][1], gdmhim[i+1][1], 2),np.linspace(gdmhim[i][2], gdmhim[i+1][2], 2), c='blue', alpha = 1)

for i in range(len(agdhim) - 1):
    ax_3d.plot(np.linspace(agdhim[i][0], agdhim[i+1][0], 2),np.linspace(agdhim[i][1], agdhim[i+1][1], 2),np.linspace(agdhim[i][2], agdhim[i+1][2], 2), c='red', alpha = 1)



line1, = ax_3d.plot([], [], [], marker='o', markersize=5, markeredgecolor='black', c='brown', alpha = 1, label = 'GD')
line2, = ax_3d.plot([], [], [], marker='o', markersize=5, markeredgecolor='black', c='blue', alpha = 1, label = 'Momentum')
line3, = ax_3d.plot([], [], [], marker='o', markersize=5, markeredgecolor='black', c='red', alpha = 1, label = 'Adaptive')

ax_3d.legend(fontsize=12)

def inupd():
    line1.set_data_3d([], [], [])
    line2.set_data_3d([], [], [])
    line3.set_data_3d([], [], [])
    return line1, line2, line3

def upd(i):
    x, y, z = gdhim[i][0], gdhim[i][1], gdhim[i][2]
    line1.set_data_3d(x, y, z)
    x, y, z = gdmhim[i][0], gdmhim[i][1], gdmhim[i][2]
    line2.set_data_3d(x, y, z)
    x, y, z = agdhim[i][0], agdhim[i][1], agdhim[i][2]
    line3.set_data_3d(x, y, z)
    return line1, line2, line3

anim = animation.FuncAnimation(fig, upd, np.arange(1,len(gdmhim)-1), init_func=inupd, interval=120, blit=False, repeat_delay=100000)

plt.close()
anim.save('anim.gif')
video = anim.to_html5_video()
html = display.HTML(video)
    
display.display(html)






a = b = np.arange(-5.0,5.0,0.1)

xgrid, ygrid = np.meshgrid(a, b)
zgrid = func2(xgrid,ygrid)

fig = plt.figure(figsize=(10, 8))

ax_3d = Axes3D(fig, elev = 47, azim = -43)
ax_3d.plot_surface(xgrid, ygrid, zgrid, cmap='rainbow', alpha=0.5)

plt.show()


















#a = b = np.arange(-10.0,10.0,1.0)
# # x0 = randint(-10,10)
# # y0 = randint(-10,10)
x0 = 0
y0 = 0

a = b = np.arange(-5.0,5.0,0.1)
# x0 = randint(-5,5)
# y0 = randint(-5,5)

#a = b = np.arange(-512.0,512.0,1.0)
# x0 = randint(-512,512)
# y0 = randint(-512,512)




plt.ion()

xgrid, ygrid = np.meshgrid(a, b)

zgrid = fanc2(xgrid,ygrid)

fig = plt.figure(figsize=(10, 8))

ax_3d = Axes3D(fig, elev = 47, azim = -43)

ax_3d.plot_surface(xgrid, ygrid, zgrid, cmap='rainbow', alpha=0.5)


# обычный спуск

def GD(func, dx, dy, LR, epoh):

    x0 = 0
    y0 = 0
    
    for n in range(epoh):
    
        x0 = x0 - LR * dx(x0,y0)
        y0 = y0 - LR * dy(x0,y0)

        ax_3d.scatter(x0, y0, func(x0, y0), c='green')

        fig.canvas.draw()
        fig.canvas.flush_events()
        time.sleep(0.1)

    return x0, y0, func(x0, y0) 

#моментный метод

def GDM(func, dx, dy, LR, LRM, epoh):
    x0 = 0
    y0 = 0
    vx = 0
    vy = 0

    for n in range(epoh):
    
        vx = LRM * vx + LR * dx(x0,y0)

        vy = LRM * vy + LR * dy(x0,y0)


        x0 = x0 - LR * vx
        y0 = y0 - LR * vy

        ax_3d.scatter(x0, y0, func(x0, y0), c='green')

        fig.canvas.draw()
        fig.canvas.flush_events()
        time.sleep(0.1)
        #plt.savefig(f'foo{n}.png')


    return x0, y0, func(x0, y0) 


def AGD(func, dx, dy, LR, LRC, LRCV, epoh):
    x0 = 0
    y0 = 0


    for n in range(epoh):
        print(n)
        if (((n+1)%LRC) == 0):
            LR = LR*LRCV
        print(LR)

        x0 = x0 - LR * dx(x0,y0)
        y0 = y0 - LR * dy(x0,y0)

        ax_3d.scatter(x0, y0, func(x0, y0), c='green')

        fig.canvas.draw()
        fig.canvas.flush_events()
        time.sleep(0.1)
        print(x0,y0)

    return x0, y0, func(x0, y0) 




#GD(fanc2, dx2, dy2, 0.01, 15)

GDM(fanc2, dx2, dy2, 0.05, 0.9, 200)

#x, y, z = AGD(fanc3, dx3, dy3, 30, 12, 0.8, 100)
#print(x,y,z)

#plt.ioff()
#plt.show()

# print(gradxout)
# print(gradyout)
 


#моментный метод
# vx = 0
# vy = 0

# for n in range(N):
    

#     vx = lrm * vx + lr1 * dx2(x0,y0)
#     vy = lrm * vy + lr1 * dy2(x0,y0)

#     x0 = x0 - lr1 * vx
#     y0 = y0 - lr1 * vy

#     gradxout[n] = x0
#     gradyout[n] = y0

#     ax_3d.scatter(x0, y0, fanc2(x0, y0), c='green')

#     fig.canvas.draw()
#     fig.canvas.flush_events()
#     time.sleep(0.1)

#     print(x0, y0)

plt.ioff()
plt.show()