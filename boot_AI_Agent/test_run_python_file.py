from functions.run_python_file import run_python_file


def test(): 
    result = run_python_file("calculator", "main.py" )
    print("1st test")
    print(result)
    print("")

    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print("2st test")
    print(result)
    print("")

    result = run_python_file("calculator", "tests.py")
    print("3st test")
    print(result)
    print("")

    result = run_python_file("calculator", "../main.py")
    print("3st test")
    print(result)
    print("")

    result = run_python_file("calculator", "nonexistent.py")
    print("3st test")
    print(result)
    print("")


    result = run_python_file("calculator", "lorem.txt")
    print("3st test")
    print(result)
    print("")

if __name__ == "__main__":
    test()
