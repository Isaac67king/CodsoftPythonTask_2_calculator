def addition(x, y):
    return x+y


def subtract(x, y):
    difference = x-y
    return difference


def divide(x, y):
    if y != 0:
        return x/y
    else:
        return "Undefined"


def multiply(x, y):
    return x*y


def power(x, y):
    return x**y


def modulo(x, y):
    if y != 0:
        return x%y
    return "undefined"


if __name__ == "__main__":
    print("non_runnable")
