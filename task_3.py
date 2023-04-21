class Worker:
    def __init__(self, name: str, surname: str, position: str, wage: int, bonus: int):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):

    def get_full_name(self):
        return ' '.join(sorted([self.name, self.surname]))

    def get_total_income(self):
        return sum(self._income.values())

obj = Position('Konstantin', 'Ivanov', 'developer', 45000, 15000)
k = obj.get_full_name()
m = obj.get_total_income()
print(f'Работник: {k}, должность: {obj.position}, общий оклад: {m}')