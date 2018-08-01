import math
book = []
data = []
book.append({'author': "Ravi", 'book_name': "Hello 2", 'category': "Sci-Fi"})
book.append({'author': "Sujan", 'book_name': "Hello", 'category': "Sci-Fi"})
book.append({'author': "Alish", 'book_name': "World", 'category': "Fiction"})

for i in range(0, 3):
    data.append(book[i]['author']+' '+book[i]['book_name']+' '+book[i]['category'])


def freq(term, doc):
    return doc.split().count(term)


def voc_vector(corpus):
    vector = set()

    for doc in corpus:
        for word in doc.split():
            vector.update([word])
            print(vector)
    return vector


def u_vector(vec):
    u_vector = []
    denominator = .0
    for dimension in vec:
        denominator += dimension*dimension
    for dimension in vec:
        u_vector.append(dimension/math.sqrt(denominator))
    return u_vector


vocabulary = voc_vector(data)

tf_matrix = []
for doc in data:
    tf_vector = []
    for word in vocabulary:
        tf_vector.append(freq(word, doc))
    tf_matrix.append(tf_vector)

unit_vector = []
for vec in tf_matrix:
    unit_vector.append(u_vector(vec))


def cosine(A, B):
    numerator = 0
    denominator_a = .0
    denominator_b = .0
    for dim_a, dim_b in zip(A, B):
        numerator += (dim_a*dim_b)
        denominator_a += (dim_a*dim_a)
        denominator_b += (dim_b*dim_b)
    denominator = math.sqrt(denominator_a)*math.sqrt(denominator_b)
    return numerator/denominator


vec = unit_vector[0]
angle = []
for next_vec in unit_vector:
    angle.append(cosine(vec, next_vec))

item_index = []
for i, item in enumerate(angle):
    if item > 0.5:
        item_index.append(i)

print(item_index)
