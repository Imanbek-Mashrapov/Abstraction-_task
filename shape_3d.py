from abc import ABC, abstractmethod


class Shape3d(ABC):
    @abstractmethod
    def surface_area(self):
        pass

    @abstractmethod
    def volume(self):
        pass