class Task01:

    def __init__(self, number_from, number_to):
        self.number_from = number_from
        self.number_to = number_to

    def filter_number(self, number):
        """
        Check if number is can be divided by 3 and does not end with 4 or 7
        :return: int number if satisfied to conditions or 0 if not
        """
        if number % 3 == 0 and number % 10 != 4 and number % 10 != 7:
            return number
        return 0

    def calculate_sum(self):
        numbers_to_sum = [self.filter_number(i) for i in range(self.number_from, self.number_to + 1)]
        return sum(numbers_to_sum)


task_01 = Task01(1, 1_000_000_002)
print(task_01.calculate_sum())

# 133333334466666672
