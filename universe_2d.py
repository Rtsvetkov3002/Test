"""
Система движущихся тел, взаимодействующих силами тяготения
"""
import itertools
from matplotlib import pyplot as pp
from numpy import sqrt

MODEL_G = 0.5  # гравитационная постоянная
COLLISION_DISTANCE = 5.0
COLLISION_COEFFICIENT = 50.0
MODEL_DELTA_T = 0.01
TIME_TO_MODEL = 200

class Universe:
    """Невнятная вселенная, основа всех миров"""

    def __init__(self):
        self.bodies = []

    def model_step(self):
        """Итерация решения задачи Коши. Конечно не присуща вселенной, но тут на своём месте"""

        for b1, b2 in itertools.product(self.bodies, self.bodies):
            if b1 != b2:
                force = b1.universe.attractive_force(b1, b2)
                cos, sin = b1.direction_of_attractive_force(b2)
                b1.apply_force(force, cos, sin)
        for b in self.bodies:
            b.advance()

    def add_body(self, body):
        self.bodies.append(body)

class Body:
    """
    Тело с учетом притяжения со стороны других тел
    """
    def __init__(self, universe, mass, x, y, vx, vy):
        self.universe = universe
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        universe.add_body(self)

        self.trajectory_x = []
        self.trajectory_y = []

    def direction_of_attractive_force(self, other):
        """
        Прямая, соединяющая два тела
        """
        cos = (self.x - other.x) / sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
        sin = (self.y - other.y) / sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
        return (cos, sin)

    def advance(self):
        self.trajectory_x.append(self.x)
        self.trajectory_y.append(self.y)
        self.x += self.vx * MODEL_DELTA_T
        self.y += self.vy * MODEL_DELTA_T

    def apply_force(self, force, cos, sin):
        self.vx += (force * cos) / (self.mass) * MODEL_DELTA_T
        self.vy += (force * sin) / (self.mass) * MODEL_DELTA_T

class Universe2D(Universe):
    def __init__(self, G, k, collision_distance):
        super().__init__()
        self.G = G
        self.k = k
        self.collision_distance = collision_distance

    def attractive_force(self, b1, b2):
        """
        Величина силы притяжения между двумя телами, если считать ее пропорциональной 1/
        """
        dist = sqrt((b1.x - b2.x)**2 + (b1.y - b2.y)**2)
        if dist > self.collision_distance:
            force = - self.G * b1.mass * b2.mass / sqrt((b1.x - b2.x)**2 + (b1.y - b2.y)**2)
        else:
            force = - self.k * b1.mass * b2.mass / sqrt((b1.x - b2.x)**2 + (b1.y - b2.y)**2)
        return force

u = Universe2D(MODEL_G, COLLISION_COEFFICIENT, COLLISION_DISTANCE)

bodies = [
    Body(u,  50000.,   0.,   0.,  0.,   0.),
    Body(u,     10., 1000.,   0.,  0., -10.),
    Body(u,     10.,   0., 1000., 15.,   0.)
]

steps = int(TIME_TO_MODEL / MODEL_DELTA_T)
for stepn in range(steps):
    u.model_step()

for b in bodies: # для всех тел
    pp.plot(b.trajectory_x, b.trajectory_y) # нарисуем их траектории

pp.show()

