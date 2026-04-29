def ask_value(message):
    value = float(input(message))
    return value
def cal_discriminant(a, b, c):
    return b**2 - 4*a*c
def cal_roots(a, b, c):
    d = cal_discriminant(a, b, c)
    if d > 0:
        root1 = (-b + d**0.5) / (2*a)
        root2 = (-b - d**0.5) / (2*a)
        print (root1, root2)
    elif d == 0:
        root = -b / (2*a)
        print (root)
    else:
        print ("No roots")
def solv_square(a, b, c):
    d = cal_discriminant(a, b, c)
    cal_roots(a, b, c)

def main():
    print("Enter coefficients for ax^2 + bx + c = 0")
    a = ask_value("a: ")
    b = ask_value("b: ")
    c = ask_value("c: ")
    solv_square(a, b, c)

main()


