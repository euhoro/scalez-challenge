from flask import Flask

from closest_vector_cached import ClosestVectorFinderCached

SEMI_COLON = ';'
CLOSEST_ALGORITHM = 'closest'
app = Flask(__name__)
cache = {}


@app.route('/')
def hello():
    return "App running!"  # print app running


@app.route('/build/<str_vectors>')  # http://localhost:5000/build/1 2 3;5 6 7
def build(str_vectors):
    matrix = []
    str_mat = str_vectors.split(SEMI_COLON)
    for str_v in str_mat:
        vector = list(map(int, get_delimited_values(str_v)))
        matrix.append(vector)

    closest_vector_finder = ClosestVectorFinderCached(matrix)  # vectors)
    closest_vector_finder.build()
    cache[CLOSEST_ALGORITHM] = closest_vector_finder
    return "build ok!"


@app.route('/query/<str_new_sample>')  # http://localhost:5000/query/1 2 3
def query(str_new_sample):
    if CLOSEST_ALGORITHM in cache:
        closest_vector_finder = cache[CLOSEST_ALGORITHM]
        new_sample = list(map(int, get_delimited_values(str_new_sample)))
        res = closest_vector_finder.query(new_sample)
        return str(res)
    else:
        return "not yet build!"


def get_delimited_values(str_new_sample):
    return str_new_sample.split(' ')


if __name__ == '__main__':
    app.run()
