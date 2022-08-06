def sub(a: int = 0, b: int = 0)-> int:
    return b - a
print(sub(b = 10, a = 15))
print(sub.__annotations__)
print(sub.__doc__)