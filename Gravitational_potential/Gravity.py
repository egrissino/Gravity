## Evan Grissino
## 02/10/16
## Gravity Model
## 2.x and 3.x

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

class plot:
    def __init__(self):
        self.start_x = -15e6
        self.stop_x = 15e6
        self.start_y = -15e6
        self.stop_y = 15e6
        self. step = 0.5e5

        self.G = 6.674e-11
        
        self.x = np.arange(self.start_x, self.stop_x, self.step)
        self.y = np.arange(self.start_y, self.stop_y, self.step)

        self.planets = {
            # "name" : [x_pos, y_pos, mass, radius]
            "earth" : [0, 0, 5.972e24, 6.371e6],
            #"moon" : [-8e6, -10e6, 7.348e22, 1.737e6]
            }

    def run(self):
        self.Z = []
        for i in self.x:
            row = []
            for j in self.y:
                item = self.func(i, j)
                row.append(item)
            self.Z.append(row)
        self.X, self.Y = np.meshgrid(self.x, self.y)

        
    def func(self, x, y):
        gx = 0
        gy = 0
        
        for planet in self.planets:
            xp = self.planets[planet][0]
            yp = self.planets[planet][1]
            mass = self.planets[planet][2]
            radius = self.planets[planet][3]
            rho = mass / ((4/3) * np.pi * radius**3)
            
            r = np.sqrt((x - xp)**2 + (y - yp)**2)

            # Calculate for outside or inside
            if r < radius:
                grav = self.G * (4/3) * r * np.pi * rho
            else:
                grav = self.G * mass / r**2

            # Get angle from body to point
            if (x-xp) > 0:
                theta = np.arctan(np.fabs(y - yp)/np.fabs(x - xp))
            else:
                theta = 0

            # Breakup gavity vector and add or subtract component
            if (x >= xp):
                gx -= grav * np.cos(theta)
            else:
                gx += grav * np.cos(theta)
                
            if (y >= yp):
                gy -= grav * np.sin(theta)
            else:
                gy += grav * np.sin(theta)

        return -np.sqrt(gx**2 + gy**2)

    
    def plot(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_wireframe(self.X, self.Y, self.Z, rstride=10, cstride=10)
        plt.show()


P = plot()
P.run()
P.plot()
