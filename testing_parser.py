def parse_hash_code_file(file_path):
    """
        Parsing the input data

        Returns:
            tuple -- d: the number of days, libraries: the list containing the libraries objects
    """
    path = "scenarios/{}".format(file_path)
    b, l, d = None, None, None
    books = []
    n, t, m = None, None, None
    lib_books = []
    libraries = []

    with open(path) as fp:
        cnt = 0
        for i, line in enumerate(fp):
            if i == 0:
                b, l, d = line.strip().split(' ')
            elif i == 1:
                books = list(line.strip().split(' '))
            elif i % 2 == 0:
                n, t, m = line.strip().split(' ')
            else:
                lib_books = list(line.strip().split(' '))
                libraries.append((n, t, m, lib_books))

    print(b, l, d)
    print(books)
    print(len(libraries))

    # file = open("scenarios/{}".format(file_path))
    # b, l, d = map(int,
    #               file.readline().split())  # number of different books, number of libraries, number of days
    # book_scores = list(map(int, file.readline().split()))  # scores of the individual books
    #
    # print(b, l, d)
    # print(book_scores)


def record_word_cnt(words, bag_of_words):
    for word in words:
        if word != '':
            if word.lower() in bag_of_words:
                bag_of_words[word.lower()] += 1
            else:
                bag_of_words[word.lower()] = 1


parse_hash_code_file("b_read_on.txt")
