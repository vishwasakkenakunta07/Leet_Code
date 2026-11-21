
class Solution:
    def validSquare(self, p1, p2, p3, p4):

        points = [p1, p2, p3, p4]
        distances = []

        for i in range(4):
            for j in range(i + 1, 4):

                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]

                d = dx * dx + dy * dy
                distances.append(d)

        distances.sort()

        return (
            distances[0] > 0 and
            distances[0] == distances[1] ==
            distances[2] == distances[3] and
            distances[4] == distances[5] and
            distances[4] == 2 * distances[0]
        )
