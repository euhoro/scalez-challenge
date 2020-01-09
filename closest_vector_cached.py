from sklearn.neighbors import NearestNeighbors

from closest_vector_implementation import make_kd_tree, get_nearest, dist_sq_dim


class ClosedVectorKDtree:
    def __init__(self, training_sample):
        self.training_sample = training_sample
        self.dim = len(self.training_sample[0])

    def build(self):
        self.kd_tree = make_kd_tree(self.training_sample, len(self.training_sample[0]))

    def query(self, vector):
        val = get_nearest(self.kd_tree, vector, self.dim, dist_sq_dim)
        return val[1]


class ClosestVectorFinder:
    def __init__(self, training_sample):
        self.training_sample = training_sample
        self.neigh = NearestNeighbors(1,algorithm="kd_tree")

    def build(self):
        self.neigh.fit(self.training_sample)

    def query(self, new_sample):
        neighbours = self.neigh.kneighbors([new_sample], 1, return_distance=False)
        return self.training_sample[neighbours[0][0]]


class ClosestVectorFinderCached:
    def __init__(self, training_sample):
        self.cache = {}
        self.closest_vector_finder = ClosedVectorKDtree(training_sample)

    def build(self):
        self.closest_vector_finder.build()

    def query(self, new_sample):
        if str(new_sample) in self.cache:
            res = self.cache[str(new_sample)]
        else:
            res = self.closest_vector_finder.query(new_sample)
            self.cache[str(new_sample)] = res
        return res
