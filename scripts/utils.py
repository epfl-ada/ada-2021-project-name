def iterator_from_file(file_name):
    with open(file_name, "r") as file:
        for line in file:
            yield line
