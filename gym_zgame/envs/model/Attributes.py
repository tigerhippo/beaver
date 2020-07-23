
class Attributes:
    def __init__(self):

    def calculate_average(self, arr = []):
        total = 0
        for x in range(0, len(arr)):
            total += x
        return total / len(arr)

    