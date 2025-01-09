import numpy
from scipy.optimize import curve_fit

def constant(n, a):  # O(1)
    return a

def logarithmic(n, a, b):  # O(log n)
    return a * numpy.log(n) + b

def linear(n, a, b):  # O(n)
    return a * n + b

def n_log_n(n, a, b):  # O(n log n)
    return a * n * numpy.log(n) + b

def quadratic(n, a, b):  # O(n^2)
    return a * n**2 + b

functions = {
    "O(1)": constant,
    "O(log n)": logarithmic,
    "O(n)": linear,
    "O(n log n)": n_log_n,
    "O(n^2)": quadratic
}

def runtime_approximation(input_sizes, times):
    errors = {}
    for name, func in functions.items():
        try:
            params, _ = curve_fit(func, input_sizes, times)
            predicted_times = func(numpy.array(input_sizes), *params)
            mse = numpy.mean((numpy.array(times) - predicted_times) ** 2)
            errors[name] = mse
        except:
            errors[name] = float('inf')

    best_fit = min(errors, key=errors.get)

    for name, error in errors.items():
        print(f"{name}: Mean Squared Error = {error:.6f}")
    print()
    print("=====================================================")
    print()
    print(f"Estimated Time Complexity: {best_fit}")
