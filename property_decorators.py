import functools

# 1. Closure: A function that remembers variables from its outer scope
def power_factory(exponent):
    def calculate(base):
        # exponent is remembered from the outer scope
        return base**exponent

    return calculate

# 2. Decorator: A closure that accepts and alters a function
def log_result(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__}{args} returned {result}")
        return result

    return wrapper

# --- Execution ---
print("--- Group 1: Closures & Decorators ---")

# Using the closure
square = power_factory(2)
print(f"Closure square(5): {square(5)}")

# Applying the decorator manually to a closure instance
decorated_square = log_result(square)
_ = decorated_square(10)


# Applying the decorator using @ syntax
@log_result
def add(a, b):
    return a + b

_ = add(3, 7)
print()