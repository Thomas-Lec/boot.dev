from functions.get_file_content import get_file_content


def test():
    result = get_file_content("calculator", "lorem.txt")
    print("1st test")
    print(result)
    print("")

    result = get_file_content("calculator", "main.py")
    print("2st test")
    print(result)
    print("")

    result = get_file_content("calculator", "pkg/calculator.py")
    print("3st test")
    print(result)
    print("")

    result = get_file_content("calculator", "/bin/cat")
    print("4st test")
    print(result)
    print("")

    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print("5st test")
    print(result)
    print("")

if __name__ == "__main__":
    test()
