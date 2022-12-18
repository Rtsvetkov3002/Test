"""
Сравнение траектории движения Земли вокруг Солнца с траекторией движения тела, обладающего вначале массой Земли и сдувающегося на половину
"""
from typing import List
import numpy as np
from numpy import sqrt
from matplotlib import pyplot as pp # type: ignore

MODEL_DT: int = 3600
MODEL_G: float = 6.67*(10**(-11))
SUN_MASS: float = 1.988*(10**30)
SUN_X: float = 0.
SUN_Y: float = 152.*(10**9)

class Body:
    """
    Движение тела с учетом притяжения со стороны Солнца
    """
    def __init__(self, mass: float, x: float, y: float, vx: float, vy: float) -> None:

        self.mass: float = mass
        self.x: float = float(x)
        self.y: float = float(y)
        self.vx: float = float(vx)
        self.vy: float = float(vy)

        self.trajectory_x: List[float] = []
        self.trajectory_y: List[float] = []

    def advance(self) -> None:
        """
        Выполнить шаг мат. модели применительно к телу, предварительно записав его координаты
        """
        self.trajectory_x.append(self.x)
        self.trajectory_y.append(self.y)

        attractive_force: float = - MODEL_G * self.mass * SUN_MASS / ((self.x - SUN_X)**2 + (self.y - SUN_Y)**2)

        attractive_cos: float = (self.x - SUN_X) / sqrt((self.x - SUN_X)**2 + (self.y - SUN_Y)**2)
        attractive_sin: float = (self.y - SUN_Y) / sqrt((self.x - SUN_X)**2 + (self.y - SUN_Y)**2)

        self.ax: float = (attractive_force * attractive_cos ) / (self.mass)
        self.ay: float = (attractive_force * attractive_sin ) / (self.mass)

        self.vx += self.ax * MODEL_DT
        self.vy += self.ay * MODEL_DT
        self.x += self.vx * MODEL_DT
        self.y += self.vy * MODEL_DT

class Rocket(Body):
    """
    Ракеты отличается от тела наличием силы тяги, расчитанной из уравнения Мещерского
    """
    def __init__(self, x: float, y: float):
        super().__init__(6.*(10**24), x, y, 29.4*(10**3), 0.)

    def advance(self) -> None:
        super().advance()

        if self.mass >= 3*(10**24):
            gas_vel: float = 10.**4
            fuel_consump: float = 3.42*(10**20)
        else:
            gas_vel = 0.
            fuel_consump = 0.

        mesher_force: float = gas_vel * fuel_consump

        mesher_cos: float = self.vx / sqrt(self.vx**2 + self.vy**2)
        mesher_sin: float = self.vy / sqrt(self.vx**2 + self.vy**2)

        self.ax += mesher_force * mesher_cos / (self.mass)
        self.ay += mesher_force * mesher_sin / (self.mass)
        self.mass -= fuel_consump * MODEL_DT

        self.vx += self.ax * MODEL_DT
        self.vy += self.ay * MODEL_DT
        self.x += self.vx * MODEL_DT
        self.y += self.vy * MODEL_DT

r: Rocket = Rocket(0, 0)
e: Body = Body(6*(10**24), 0, 0, 29.4*(10**3), 0)

bodies: List[Rocket] = [r, e]

for t in np.arange(0, 64000000, MODEL_DT): # для всех временных отрезков
    for b in bodies: # для всех тел
        b.advance() # выполним шаг


for b in bodies: # для всех тел
    pp.plot(b.trajectory_x, b.trajectory_y) # нарисуем их траектории

pp.show()
