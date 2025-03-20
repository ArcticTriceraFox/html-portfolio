import numpy as np
import math
import random

def rastrigin(X):
    A = 10
    return A * len(X) + sum(x**2 - A * np.cos(2 * np.pi * x) for x in X)

def simulated_annealing(dim=2, max_iter=5000, T=1000, alpha=0.99, step_size=0.5):
    current_solution = np.random.uniform(-5.12, 5.12, size=dim)
    current_value = rastrigin(current_solution)
    
    for t in range(1, max_iter + 1):
        T *= alpha 
        if T <= 0.0001:
            break
        next_solution = current_solution + np.random.uniform(-step_size, step_size, size=dim)
        next_solution = np.clip(next_solution, -5.12, 5.12)
        next_value = rastrigin(next_solution)
        
        delta_E = next_value - current_value
        if delta_E < 0 or random.random() < math.exp(-delta_E / T):
            current_solution, current_value = next_solution, next_value 

    return current_solution, current_value

best_solution, best_value = simulated_annealing(dim=2)
print("Best solution found:", best_solution)
print("Best value:", best_value)