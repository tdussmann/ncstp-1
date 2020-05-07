from math import sqrt, ceil


class PlanarRF:
    """Tool to calculate rf power at a given point for a 2D-grid of given baseStations."""

    def_base_stations = [
        (0,0,10),
        (20,20,5),
        (10,0,12)
    ]

    def find_best_station(self, p, base_stations=None):
        """Identifies the most suitable base station (with most power) for a given point (x,y).
        Args:
            p (tupel of x,y): The point to solve for.
            base_stations (arr of tupels of (x,y,reach)): The list of base stations (optional).
        Returns:
            The best base station as (x,y,pwr) or None if none is in reach.
        """
        bss = self.def_base_stations if base_stations is None else base_stations
        ranking = []
        for idx, bs in enumerate(bss):
            dist = self.distance(bs[:2], p)
            pw = 0 if dist > bs[2] else self.power(bs[2], dist)
            ranking.append((idx, pw))
        best_bs_pwr = max(ranking, key=lambda i: i[1])
        if 0 == best_bs_pwr[1]:
            print("No link station within reach for point {}, {}".format(p[0], p[1]))
            return None
        else:
            best_bs_pos = bss[best_bs_pwr[0]]
            best_bs_x, best_bs_y, best_bs_pwr = best_bs_pos[0], best_bs_pos[1], round(best_bs_pwr[1],2)
            print("Best link station for point {},{} is {},{} with power {}".format(p[0], p[1], best_bs_x, best_bs_y, best_bs_pwr))
            return best_bs_x, best_bs_y, best_bs_pwr

    def distance(self, p1, p2):
        """Calculates the distance between two points on a plane."""
        return sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

    def power(self, reach, distance):
        """Calculates the RF power for a given distance from link station with given reach."""
        return (reach-distance)**2
