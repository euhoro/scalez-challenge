import ast

from closest_vector_cached import ClosestVectorFinderCached


def query_vectors():
    str_vectors = input("Enter vectors ex: [[1, 0, 1, 0], [0, 1, 1, 0], [0, 1, 0, 1 ]]  (*press ctrl+c to quit) : ")
    matrix = ast.literal_eval(str_vectors)
    print("you entered vectors : ")
    print(str(matrix))

    closest_finder = ClosestVectorFinderCached(matrix)
    closest_finder.build()

    while True:
        str_query = input("Enter query ex: [0, 0, 0, 1]  (*press ctrl+c to quit) : ")
        query = ast.literal_eval(str_query)
        print("you queried : ")
        print(query)

        closest_vector = closest_finder.query(query)
        print("result: " + str(closest_vector))


if __name__ == '__main__':
    query_vectors()
