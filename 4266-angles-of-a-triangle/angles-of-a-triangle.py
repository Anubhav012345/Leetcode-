class Solution:
    def internalAngles(self, sides: list[int]) -> list[float]:
        sides.sort()
        if (sides[0] + sides[1]) <= sides[2]:
            return []

        a = sides[0] ** 2
        b = sides[1] ** 2
        c = sides[2] ** 2

        cos_a = ((a  + b - c) / (2 * sides[0] * sides[1]))
        cos_b = ((a  + c - b) / (2 * sides[0] * sides[2]))
        cos_c = ((c  + b - a) / (2 * sides[2] * sides[1]))

        angle_a = math.degrees(math.acos(cos_a))
        angle_b = math.degrees(math.acos(cos_b))
        angle_c = math.degrees(math.acos(cos_c))
        return sorted([angle_a, angle_b, angle_c])
        