def doc_format_checker_and_converter(conversion_function, valid_formats):
    def new_func(filename, content):

        print(f"test2::: {conversion_function}, {valid_formats}")


# Don't edit below this line


def capitalize_content(content):
    return content.upper()


def reverse_content(content):
    return content[::-1]
