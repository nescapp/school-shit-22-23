def addition(a, b):
    return a + b


def some_function():
    global global1
    global1 = 32

def main():
    global global1
    # global1 = 0
    # print(global1)
    # some_function()
    # print(global1)
    print("test")

if __name__ == "__main__":
    main()