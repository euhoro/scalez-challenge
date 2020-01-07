from sklearn.neighbors import NearestNeighbors


class ClosestVectorFinder:
    def __init__(self, training_sample):
        self.training_sample = training_sample
        self.neigh = NearestNeighbors(len(training_sample))

    def build(self):
        self.neigh.fit(self.training_sample)

    def query(self, new_sample):
        neighbours = self.neigh.kneighbors([new_sample], 1, return_distance=False)
        return self.training_sample[neighbours[0][0]]


class ClosestVectorFinderCached:
    def __init__(self, training_sample):
        self.cache = {}
        self.closest_vector_finder = ClosestVectorFinder(training_sample)

    def build(self):
        self.closest_vector_finder.build()

    def query(self, new_sample):
        if str(new_sample) in self.cache:
            res = self.cache[str(new_sample)]
        else:
            res = self.closest_vector_finder.query(new_sample)
            self.cache[str(new_sample)] = res
        return res
