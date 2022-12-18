"""
Сравнение траектории движения Земли вокруг Солнца с траекторией движения тела, обладающего вначале массой Земли и сдувающегося на половину
"""
import numpy as np
from numpy import sqrt
from matplotlib import pyplot as pp

MODEL_DT = 3600
MODEL_G = 6.67*(10**(-11))
SUN_MASS = 1.988*(10**30)
SUN_X = 0
SUN_Y = 152*(10**9)

class Body:
    """
    Движение тела с учетом притяжения со стороны Солнца
    """
    def __init__(self, mass, x, y, vx, vy):

        self.mass = mass
        self.x = float(x)
        self.y = float(y)
        self.vx = float(vx)
        self.vy = float(vy)

        self.trajectory_x = []
        self.trajectory_y = []

    def advance(self):
        """
        Выполнить шаг мат. модели применительно к телу, предварительно записав его координаты
        """
        self.trajectory_x.append(self.x)
        self.trajectory_y.append(self.y)

        attractive_force = - MODEL_G * (self.mass) * SUN_MASS / ((self.x - SUN_X)**2 + (self.y - SUN_Y)**2)

        attractive_cos = (self.x - SUN_X) / sqrt((self.x - SUN_X)**2 + (self.y - SUN_Y)**2)
        attractive_sin = (self.y - SUN_Y) / sqrt((self.x - SUN_X)**2 + (self.y - SUN_Y)**2)

        self.ax = (attractive_force * attractive_cos ) / (self.mass)
        self.ay = (attractive_force * attractive_sin ) / (self.mass)

        self.vx += self.ax * MODEL_DT
        self.vy += self.ay * MODEL_DT
        self.x += self.vx * MODEL_DT
        self.y += self.vy * MODEL_DT

class Rocket(Body):
    """
    Ракеты отличается от тела наличием силы тяги, расчитанной из уравнения Мещерского
    """
    def __init__(self, x, y):
        super().__init__(6*(10**24), x, y, 29.4*(10**3), 0)

    def advance(self):
        super().advance()

        if self.mass >= 3*(10**24):
            gas_vel = 10**4
            fuel_consump = 3.42*(10**20)
        else:
            gas_vel = 0
            fuel_consump = 0

        mesher_force = gas_vel * fuel_consump

        mesher_cos = self.vx / sqrt(self.vx**2 + self.vy**2)
        mesher_sin = self.vy / sqrt(self.vx**2 + self.vy**2)

        self.ax += mesher_force * mesher_cos / (self.mass)
        self.ay += mesher_force * mesher_sin / (self.mass)
        self.mass -= fuel_consump * MODEL_DT

        self.vx += self.ax * MODEL_DT
        self.vy += self.ay * MODEL_DT
        self.x += self.vx * MODEL_DT
        self.y += self.vy * MODEL_DT

r = Rocket(0, 0)
e = Body(6*(10**24), 0, 0, 29.4*(10**3), 0)

bodies = [r, e]

for t in np.arange(0, 64000000, MODEL_DT): # для всех временных отрезков
    for b in bodies: # для всех тел
        b.advance() # выполним шаг


for b in bodies: # для всех тел
    pp.plot(b.trajectory_x, b.trajectory_y) # нарисуем их траектории

pp.show()
