def new_resizer(max_width, max_height):

    def inner_resizer(min_width=0,min_height=0):
        if min_width > max_width or min_height > max_height:
            raise Exception ("minimum size cannot exceed maximum size")

        def innermost_inner_resizer(width, height):
            width = min(width,max_width)
            width = max(width,min_width)
            height = min(height,max_height)
            height = max(height,min_height)
            return width,height
        return innermost_inner_resizer
    return inner_resizer

