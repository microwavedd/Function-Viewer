import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def calculate_x_range(func, x):
    """
    parameters:
    func: the function or equation
    x: x

    Returns:
    tuple: a tuple (min_x, max_x)
    """
    # find points by solving the first derivative
    derivative = sp.diff(func, x)
    critical_points = sp.solve(derivative, x)
    critical_values = [cp.evalf() for cp in critical_points if cp.is_real]
    if critical_values:
        min_x = min(critical_values) - 1
        max_x = max(critical_values) + 1
    else:
        # default range if no critical points THIS IS CUSTOMIZABLE
        min_x = -10
        max_x = 10

    return float(min_x), float(max_x)

def plot_function(func_str, num_points=1000, title="Function Plot", xlabel="x", ylabel="y", grid=True, grid_which='both', grid_axis='both'):
    """
    parameters:
    func_str: function to plot as a string
    num_points: nnumber of points to plot
    
    (these are matplotlib aesthetic customizations, they don't affect the solving of the problem)
    title: title of the plot
    xlabel: label for the x-axis
    ylabel: label for the y-axis
    grid: whether to show the grid
    grid_which: grid lines to apply ('both', 'major', 'minor')
    grid_axis: axis to apply grid lines ('both', 'x', 'y')
    """
    try:
        # convert to sympy expression
        x = sp.symbols('x')
        func = sp.sympify(func_str)

        # calculate the x range 
        x_min, x_max = calculate_x_range(func, x)
        x_vals = np.linspace(x_min, x_max, num_points)
        func_np = sp.lambdify(x, func, 'numpy')
        y_vals = func_np(x_vals)

        # plot le function
        plt.figure(figsize=(10, 6))
        plt.plot(x_vals, y_vals, label=func_str)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.legend()
        
        if grid:
            plt.grid(which=grid_which, axis=grid_axis)
        
        plt.show()

    except Exception as e:
        print(f"Oh oh, mistake mistake: {e}")

def plot_equation(equation_str, num_points=1000, title="Equation Plot", xlabel="x", ylabel="y", grid=True, grid_which='both', grid_axis='both'):
    """
    EQUATIONS MUST HAVE BOTH X AND Y, AS FOR FUNCTIONS, THE WHOLE EXPRESSION EQUALS Y, BUT NOT FOR EQUATIONS MY GUYS.

    parameters:
    same for functions
    """
    try:
        x, y = sp.symbols('x y')
        equation = sp.sympify(equation_str)
        solutions = sp.solve(equation, y)
        if not solutions:
            raise ValueError("No solutions found for y in the given equation.")
        func = solutions[0]
        x_min, x_max = calculate_x_range(func, x)
        x_vals = np.linspace(x_min, x_max, num_points)
        func_np = sp.lambdify(x, func, 'numpy')
        y_vals = func_np(x_vals)
        plt.figure(figsize=(10, 6))
        plt.plot(x_vals, y_vals, label=sp.pretty(equation_str))
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.legend()
        
        if grid:
            plt.grid(which=grid_which, axis=grid_axis)
        
        plt.show()

    except Exception as e:
        print(f"Oh oh, mistake mistake: {e}")

if __name__ == "__main__":
    input_type = input("Is the input a function or an equation? (Enter 'function' or 'equation'): ").strip().lower()
    input_str = input("Enter the function or equation: ").strip()
    title = input("Enter the plot title: ").strip()
    xlabel = input("Enter the x-axis label: ").strip()
    ylabel = input("Enter the y-axis label: ").strip()
    grid = input("Show grid? (yes/no): ").strip().lower() == 'yes'
    grid_which = input("Grid lines to apply ('both', 'major', 'minor'): ").strip()
    grid_axis = input("Grid axis ('both', 'x', 'y'): ").strip()

    if input_type == 'function':
        plot_function(input_str, title=title, xlabel=xlabel, ylabel=ylabel, grid=grid, grid_which=grid_which, grid_axis=grid_axis)
    elif input_type == 'equation':
        plot_equation(input_str, title=title, xlabel=xlabel, ylabel=ylabel, grid=grid, grid_which=grid_which, grid_axis=grid_axis)
    else:
        print("mistake mistake, you need to input 'function' or 'equation'")
