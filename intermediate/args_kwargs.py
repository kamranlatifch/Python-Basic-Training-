# args and kwargs are used to pass a variable number of arguments to a function
# type of args is tuple
# type of kwargs is dictionary
# *args and **kwargs OR *vars and **kvars


def function_1(name, age, rollno):
    print(f"The name of student is {name}, age is {age}, rollno is {rollno}")


def function_2(*args):
    # access args as a tuple
    # *args could be named as *vars or *list_of_args etc
    if len(args) == 3:
        print(
            f"The name of student is {args[0]}, age is {args[1]}, rollno is {args[2]}"
        )
    elif len(args) == 2:
        print(f"The name of student is {args[0]}, age is {args[1]}")
    else:
        print("Invalid number of arguments")


def function_3(**kwargs):
    # access kwargs as a dictionary
    # **kwargs could be named as **vars or **dict_of_kwargs etc for key value pairs

    for key, value in kwargs.items():
        print(f"{key} = {value}")


def main():
    function_1("John", 20, 12345)

    print("############ARGS############")
    function_2("John", 20, 12345)
    function_2("John", 20)
    list_of_args = ["Adem List", 20, 12345]
    function_2(*list_of_args)

    print("############KWARGS############")
    function_3(name="John", age=20, rollno=12345)
    function_3(name="John", age=20)
    dict_of_kwargs = {
        "Kamran": 100,
        "Adem": 200,
        "Ahmet": 300,
        "Mehmet": 400,
        "Ali": 500,
        "Veli": 600,
        "Ayse": 700,
        "Fatma": 800,
        "Hayri": 900,
        "Hasan": 1000,
    }
    function_3(**dict_of_kwargs)


if __name__ == "__main__":
    main()
