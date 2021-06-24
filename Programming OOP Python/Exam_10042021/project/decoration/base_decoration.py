from abc import ABC, abstractmethod


class BaseDecoration(ABC):
    @abstractmethod
    def __init__(self, comfort:float, price:float):
        self.comfort = comfort
        self.price = price
