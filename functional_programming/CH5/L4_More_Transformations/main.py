def doc_format_checker_and_converter(conversion_function, valid_formats):

    def new_func(filename, content):
        new_filename = filename.split('.')
        if new_filename[1] not in valid_formats:
            raise ValueError("invalid file format")
        return conversion_function(content)

    return new_func


# Don't edit below this line


def capitalize_content(content):
    return content.upper()


def reverse_content(content):
    return content[::-1]
