def create_markdown_image(alt_text):
    alt_text = f"![{alt_text}]"

    def create_markdown_image_url(url):
        url = url.replace("(","%28").replace(")","%29")
        image_syntax = alt_text + f"({url})"

        def create_markdown_image_innermost(title=None):
            if title is not None:
                new_image_syntax = image_syntax[:-1]
                return f'{new_image_syntax} "{title}")'
            return image_syntax
        
        return create_markdown_image_innermost

    return create_markdown_image_url
