from scipy.optimize import minimize_scalar, differential_evolution

def quadratic_function(x):
    return (x - 3) ** 2 + 5

result = minimize_scalar(quadratic_function)
print("Optimal solution : ",result.x)
print("Minimum value : ",result.fun)

'''For global optimization'''

def global_objective(x):
    return x[0] ** 2 + x[1] ** 2

global_result = differential_evolution(global_objective, [(-2,2), (-2,2)])
print(f"Global result : {global_result.x}")
print(f"Global Minimum value : {global_result.fun}")