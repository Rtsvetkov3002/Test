"""
Trying to make SLE calculator using evolution
"""
import pygad
import numpy
from numpy import array
from numpy.linalg import solve as solve_out_of_the_box


system_coefs = array([
        [1.5, 2.0, 1.5],
        [3.0, 2.0, 4.0],
        [1.0, 6.0, 0.0],
        ], dtype=float)

system_bees = array([5, 6, 7], dtype=float)
Size = len(system_coefs)

def fitness_func(ga_instance, solution, solution_idx):
    metrika = 0
    for i in range(Size):
        output = numpy.sum(solution*system_coefs[i]) - system_bees[i]
        metrika = max(metrika, numpy.abs(output))
    fitness = 1.0 / (metrika)
    return fitness

fitness_function = fitness_func

num_generations = 10000
num_parents_mating = 10
sol_per_pop = 20
num_genes = len(system_coefs)

last_fitness = 0
def callback_generation(bga_instance):
    global last_fitness
    print("Generation = {generation}".format(generation=ga_instance.generations_completed))
#    print("Fitness    = {fitness}".format(fitness=ga_instance.best_solution()[1]))
#    print("Change    = {change}".format(change=ga_instance.best_solution()[1] - last_fitness))
    last_fitness = ga_instance.best_solution()[1]

ga_instance = pygad.GA(num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_function,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       on_generation=callback_generation,
                       )

ga_instance.run()

ga_instance.plot_fitness()

solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
print("Index of the best solution : {solution_idx}".format(solution_idx=solution_idx))

if ga_instance.best_solution_generation != -1:
    print("Best fitness value reached after {best_solution_generation} generations.".format(best_solution_generation=ga_instance.best_solution_generation))
    oob_solution = solve_out_of_the_box(system_coefs, system_bees)
    print("Out of the box solution:", oob_solution)
    deviation=[]
    for i in range(Size):
        deviation.append(abs(solution[i] - oob_solution[i]))
    print("Макс отклонение компоненты решения:", numpy.max(deviation))
