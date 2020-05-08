import os.path


class SolutionParser:

    def __init__(self, file_path: str, days: int, libraries: list, books: list):
        self.file_path = file_path
        self.days = days
        self.libraries = libraries
        self.books = books

    def parse_solution_file(self):
        path = "solved/{}".format(self.file_path)

        if not os.path.isfile(path):
            raise Exception('Didn\'t found the file: {}'.format(path))

        no_libraries = 0
        libraries = []
        books_assigned = []
        chosen_lib = None

        with open(path) as fp:
            for i, line in enumerate(fp):
                if line == '\n':
                    continue

                if i == 0:

                    no_libraries = line.strip()
                    if no_libraries > len(libraries):
                        raise Exception('You can\'t sign up more libraries that those available')

                elif i%2 == 0:

                    books_ids = list(map(int, line.strip().slipt(' ')))

                    # Check if the books scanned are in the chosen library
                    for book in chosen_lib.books:
                        if book.id not in books_ids:
                            raise Exception('Scanned a book that doesn\'t belong to the chosen library')

                else:

                    library_id, no_books = line.strip().split(' ')

                    if library_id > len(libraries):
                        raise Exception('This library doesn\'t exists!')

                    chosen_lib = libraries[library_id] # Get the chosen library from the libraries list

                    if no_books > chosen_lib.no_books:
                        raise Exception('You\'ve excided the max number of books of the library')
