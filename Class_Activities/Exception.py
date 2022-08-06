list = [1, 2, 3, 4, 5, 6,7]
try:
    s = list[9]
    print("i did well")
except IndexError as e:
    print(f"Error occured: {e}")
except(TypeError | ValueError) as e:
    print(f"Error of no type: (e)")
finally:
    print("I am from finally")