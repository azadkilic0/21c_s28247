from abc import ABC, abstractmethod

class SquareGenerator(ABC):
    @abstractmethod
    def generate_squares(self, start, end):
        """Abstract method to generate a list of squares for a given range of numbers."""
        pass

class CubicGenerator(SquareGenerator):
    def generate_squares(self, start, end):
        """Generate a list of squares for a given range of numbers."""
        if start > end:
            raise ValueError("Start of range must be less than or equal to the end.")
        return [x ** 2 for x in range(start, end + 1)]

    def generate_cubes(self, start, end):
        """Generate a list of cubes for a given range of numbers."""
        return [x ** 3 for x in range(start, end + 1)]