import unittest

from planar_rf.planar_rf import PlanarRF

class TestPlanarRF(unittest.TestCase):

    testPoints = [
        (0,0),
        (100,100),
        (15,10),
        (18,18)
    ]

    def test_calc_distance(self):
        prf = PlanarRF()
        dist = prf.distance((18, 18), (20, 20))
        dist_rounded = round(dist, 2)
        assert dist_rounded == 2.83

    def test_calc_power(self):
        prf = PlanarRF()
        assert round(prf.power(10, 5.0),2) == 25

    def test_find_best_station(self):
        results = []
        prf = PlanarRF()
        for pt in self.testPoints:
            results.append(prf.find_best_station(pt))
        assert (0,0,100.00) in results
        assert (10,0,0.67) in results
        assert (20,20,4.72) in results
        assert None in results

if __name__ == '__main__':
    unittest.main()