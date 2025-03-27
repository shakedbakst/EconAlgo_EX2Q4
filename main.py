import cvxpy as cp

# Variables for resource allocation
x = cp.Variable(pos=True)  # Portion of steel received by Ami (must be positive)
t = cp.Parameter(nonneg=True)  # t is a parameter between 0 and 1

# Compute values for each player
V_A = x  # Ami receives value from the steel
V_T = (1 - t) + (1 - x) * t  # Tami receives value from steel and oil

# Objective function - Maximizing the sum of logarithms (to avoid direct multiplication)
objective = cp.Maximize(cp.log(V_A) + cp.log(V_T))

# Small value to ensure positivity
epsilon = 1e-6

# Constraints: Ami receives at least 1/2t of the steel, and values must be positive
constraints = [
    x >= 1 / (2 * t),
    x <= 1,  # Cannot receive more than 1 of the steel
    V_A >= epsilon,  # Ensuring positivity
    V_T >= epsilon   # Ensuring positivity
]

# Solve the problem
problem = cp.Problem(objective, constraints)
t.value = 1  # Example: choose t=1
problem.solve()  # Removed gp=True

# Results
print(f"Ami receives {x.value:.2f} of the steel")
print(f"Tami receives {1 - x.value:.2f} of the steel")