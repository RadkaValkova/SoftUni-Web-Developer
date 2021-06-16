class CapacityMixin:
    @staticmethod
    def get_capacity(capacity, amount):
        if amount > capacity:
            raise Exception('Capacity reached!')
        return capacity - amount # i thing that returns wrong value
