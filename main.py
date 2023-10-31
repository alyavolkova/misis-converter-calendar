from utils import convert_int2float


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def sum_x(a, b):
    return a * b


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    result = sum_x(5, 7)
    print(result)
    float_number = convert_int2float(result)
    print(f"This is number was change on {float_number}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
