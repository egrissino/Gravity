## Evan Grissino
## 3d surface plot
## 02/11/16
## 2.x and 3.x

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

class plot:
    def __init__(self):
        self.start_x = -3
        self.stop_x = 3

        #
        self.start_y = -1
        self.stop_y = 15e6
        #
        
        self. step = 0.05

        self.G = 6.674e-11
        
        self.x = np.arange(self.start_x, self.stop_x, self.step)
        self.y = self.x #np.arange(self.start_y, self.stop_y, self.step)

        self.points = {
            "Point 1" : [1, 0],
            "Point 2" : [0, 1],
            "Point 3" : [1, 1],
            "Point 4" : [0, 2]
            }

    def run(self):
        self.Z = []
        for i in self.x:
            row = []
            for j in self.y:
                item = self.distance(i, j)
                row.append(item**2)
            self.Z.append(row)
        self.X, self.Y = np.meshgrid(self.x, self.y)


    def distance(self, x, y):
        # distance sum from three points
        dist = 0
        for point in self.points:
            dist += np.sqrt((x - self.points[point][0])**2 + (y - self.points[point][1])**2)
            
        return dist

    
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
