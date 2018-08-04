def recommend(user_book, book_list):
    import math
    import collections
    import operator
    user_data = ""
    total_data = ""

    def check_iteration(book):
        if isinstance(book, collections.Iterable):
            return book
        else:
            book = (book,)
            return book

    user_book = check_iteration(user_book)

    for book in user_book:
        for name in book.booklinkauthor_set.all():
            user_data += name.author.name + ' '
        #for item in book.book_categorylink.all():
         #   user_data += item.category.title + ' '
        user_data += book.title + ' ' + book.category.title + ' '
    user_data = user_data.lower().split(" ")
    user_data.remove('')
    user_data = " ".join(user_data)
    print(user_data)

    for book in book_list:
        total_data += book.title + ' ' + book.category.title
        for name in book.booklinkauthor_set.all():
            total_data += ' ' + name.author.name
        #for item in book.book_categorylink.all():
         #   total_data += ' ' + item.category.title
        total_data += ';'

    def freq(term, doc):
        return doc.split().count(term)

    def voc_vector(corpus):
        vector = set()
        for doc in corpus:
            for word in doc.split():
                vector.update([word])
        return vector

    def u_vector(vec):
        u_vector = []
        denominator = .0
        for dimension in vec:
            denominator += dimension*dimension
        for dimension in vec:
            u_vector.append(dimension/math.sqrt(denominator))
        return u_vector

    total_data = total_data.lower().split(";")
    total_data.remove('')
    vocabulary = voc_vector(total_data)

    tf_matrix = []
    for doc in total_data:
        tf_vector = []
        for word in vocabulary:
            tf_vector.append(freq(word, doc))
        tf_matrix.append(tf_vector)

    tf_user = []
    for word in vocabulary:
        tf_user.append(freq(word, user_data))

    unit_vector = []
    for vec in tf_matrix:
        unit_vector.append(u_vector(vec))

    unit_user = u_vector(tf_user)

    def cosine(a, b):
        numerator = 0
        denominator_a = .0
        denominator_b = .0
        for dim_a, dim_b in zip(a, b):
            numerator += (dim_a*dim_b)
            denominator_a += (dim_a*dim_a)
            denominator_b += (dim_b*dim_b)
        denominator = math.sqrt(denominator_a)*math.sqrt(denominator_b)
        return numerator/denominator

    vec = unit_user
    angle = []
    for u_vec in unit_vector:
        angle.append(cosine(vec, u_vec))

    item_index = {}
    for i, item in enumerate(angle):
        if 0 < item < 1:
                item_index[i+1] = item

    sorted_value = sorted(item_index.items(), reverse=True, key=operator.itemgetter(1))

    item_index = []
    for x, _ in sorted_value:
        item_index.append(x)

    return item_index
