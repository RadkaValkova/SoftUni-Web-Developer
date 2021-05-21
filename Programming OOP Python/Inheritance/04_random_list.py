import random


class RandomList(list):

    def get_random_element(self):
        element_to_remove = random.choice(self)
        self.remove(element_to_remove)
        return element_to_remove


ll = RandomList([1,2,3,4])
print(ll.get_random_element())
print(ll)