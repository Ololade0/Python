def max_num(x, i, y):
    if(x > i and y):
        return  x

    if i > x and y:
        return  i

    if y > i and x:
        return y
    else:
        return "No max number"

int_x = 10
int_i = 40
int_y = 50
print("The max is ", max_num(int_x, int_y, int_i))


