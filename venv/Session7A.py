# print("__name__ is",__name__)

def main():
    a = 10  # J1
    b = [10, 20, 30, 40, 50]  # J2

    print(a)  # J3
    print(b)  # J4

    sum = 0  # J5

    for elm in b:  # J6
        sum = sum + elm  # execution
        print(elm)


if __name__ == "__main__":
    main()