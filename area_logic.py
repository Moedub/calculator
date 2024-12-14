class AreaLogic:
    @staticmethod
    def calculate_circle_area(radius: float) -> float:
        return 3.14159 * (radius ** 2)

    @staticmethod
    def calculate_rectangle_area(length: float, width: float) -> float:
        return length * width

    @staticmethod
    def calculate_triangle_area(base: float, height: float) -> float:
        return 0.5 * base * height

    @staticmethod
    def calculate_square_area(side: float) -> float:
        return side ** 2
