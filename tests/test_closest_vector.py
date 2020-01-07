import unittest
from closest_vector_cached import ClosestVectorFinder, ClosestVectorFinderCached


def build(vectors):
    closest_finder = ClosestVectorFinderCached(vectors)
    closest_finder.build()
    return closest_finder


class TestClosestVector(unittest.TestCase):
    def test_fact(self):
        closest_finder = ClosestVectorFinder([[1, 0, 1, 0], [0, 1, 1, 0], [0, 1, 0, 1]])
        closest_finder.build()
        closest_vector = closest_finder.query([0, 0, 0, 1])
        self.assertEqual(closest_vector, [0, 1, 0, 1])

    def test_all(self):
        vectors = [[1, 0, 1, 0], [0, 1, 1, 0], [0, 1, 0, 1]]
        v_q1 = [1, 0, 0, 0]
        v_q2 = [0, 0, 0, 1]
        obj = build(vectors)  # run in O(N * log (N))
        v_a1 = obj.query(v_q1)  # run in O(log (N))
        res = v_a1 == [1, 0, 1, 0]  # True
        self.assertTrue(res)
        v_a2 = obj.query(v_q2)  # run in O(log (N))
        res = v_a2 == [0, 1, 0, 1]  # True
        self.assertTrue(res)
        v_a3 = obj.query(v_q1)  # run in O(1)
        res = v_a3 == [1, 0, 1, 0]  # True
        self.assertTrue(res)


if __name__ == '__main__':
    unittest.main()
