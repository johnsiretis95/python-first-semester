def zero():
    return 0


def one():
    return 1


def two():
    return 2


def three():
    return 3


def four():
    return 4


def five():
    return 5


def six():
    return 6


def seven():
    return 7


def eight():
    return 8


def nine():
    return 9


def convertion(n):
    if "zero" in n:
        x = zero()

    elif "one" in n:
        x = one()
    elif "two" in n:
        x = two()
    elif "three" in n:
        x = three()
    elif "four" in n:
        x = four()
    elif "five" in n:
        x = five()
    elif "six" in n:
        x = six()
    elif "seven" in n:
        x = seven()
    elif "eight" in n:
        x = eight()
    elif "nine" in n:
        x = nine()
    else:
        print("Fail input!")

    return x;


def calculator(n):

    if 'times' in n:
        y = n.split("times")
        x = convertion(y[0]) * convertion(y[1])

    elif 'plus' in n:
        y = n.split("plus")
        x = convertion(y[0]) + convertion(y[1])
    elif 'minus' in n:
        y = n.split("minus")
        x = convertion(y[0]) - convertion(y[1])

    else:
        x = 0
    return x


a = raw_input("Type the numeric expression \n")
print (calculator(a))