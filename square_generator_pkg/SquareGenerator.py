class SquareGenerator:
    def generate_squares(self, start, end):
        """Generate a list of squares for a given range of numbers."""
        return [x ** 2 for x in range(start, end + 1)]

class CubicGenerator(SquareGenerator):
    def generate_cubes(self, start, end):
        """Generate a list of cubes for a given range of numbers."""
        return [x ** 3 for x in range(start, end + 1)]

