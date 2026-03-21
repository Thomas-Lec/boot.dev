def lines_with_sequence(char):
    def with_char(length):
        sequence = char * length
        
        def with_char_with_length(doc):
            counter = 0
            doc_lines = doc.split()
            for docs in doc_lines:
                if sequence in docs:
                    counter += 1
            return counter
        return with_char_with_length
    return with_char
