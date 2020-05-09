import os.path


class SolutionParser:

    def __init__(self, file_path: str, days: int, libraries: list, books: list):
        self.file_path = file_path
        self.days = days
        self.libraries = libraries
        self.books = books

    def compute_tot_score(self, assigned_book):
        # Compute the total score
        books_assigned = set(assigned_book)
        total_score = 0

        for book in self.books:
            if book.id in books_assigned:
                total_score += book.score

        return total_score

    def parse_solution_file(self):
        path = "solved/{}.solution.txt".format(self.file_path)

        if not os.path.isfile(path):
            raise Exception('Didn\'t found the file: {}'.format(path))

        no_libraries = 0
        assigned_books = []
        chosen_lib = None
        tot_sign_up = 0

        with open(path) as fp:
            for i, line in enumerate(fp):
                if line == '\n':
                    continue

                if i == 0:

                    no_libraries = int(line.strip())
                    if no_libraries > len(self.libraries):
                        raise Exception('You can\'t sign up more libraries that those available')

                elif i % 2 == 0:

                    books_ids = list(map(int, line.strip().split(' ')))

                    if len(books_ids) > chosen_lib.no_books:
                        raise Exception('You\'ve exceeded the max number of books that library contains')

                    # Check if the books scanned are in the chosen library
                    for book in books_ids:
                        if book not in chosen_lib.get_books_ids():
                            raise Exception('Scanned a book that doesn\'t belong to the chosen library')

                    assigned_books += (books_ids) # add the assigned books to the tot books assigned
                else:

                    library_id, no_books = map(int ,line.strip().split(' '))

                    if library_id > len(self.libraries):
                        raise Exception('This library doesn\'t exists!')

                    chosen_lib = self.libraries[library_id]  # Get the chosen library from the libraries list

                    if no_books > chosen_lib.no_books:
                        raise Exception('You\'ve exceeded the max number of books of the library')

                    no_libraries += 1 # increment the number of chosen libraries
                    tot_sign_up += chosen_lib.sign_up_time

        # Control if the tot_sign_up time don't exceed the number of days
        if tot_sign_up > self.days:
            raise Exception('The total sign up exceed the maximum number of days')

        return self.compute_tot_score(assigned_books)