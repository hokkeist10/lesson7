class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_weight(self, weight, number_sm):
        result_weight = self._length * self._width * weight * number_sm
        return result_weight

r = Road(5000, 20)
w = r.calc_weight(25, 0.05)
print(f'Суммарный вес асфальта = {w}')