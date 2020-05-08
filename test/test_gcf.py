import unittest

import main

from unittest.mock import Mock



class MyTestCase(unittest.TestCase):
    def test_best_station(self):
        params = {'x': 18, 'y': 18}
        req = Mock(args=params)
        ret = main.best_station(req)
        assert ret == "Best link station for point 18,18 is 20,20 with power 4.72"

if __name__ == '__main__':
    unittest.main()
