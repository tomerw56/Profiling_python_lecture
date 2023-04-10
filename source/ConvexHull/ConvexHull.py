import math
import dataclasses
import random
import setproctitle
import os
import sys

@dataclasses.dataclass
class point:
    x:int
    y:int
    def __lt__(self, other):
        if self.y < other.y:
            return True
        elif self.y > other.y:
            return False
        elif self.x < other.x:
            return True
        else:
            return False

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y




# Define the ConvexHull Class

class ConvexHull:
    def __init__(self, points):
        self.points=points
        self.hull = self.graham_scan()

    def graham_scan(self):
        """
        Returns the vertices of the convex hull of a set of points using the Graham scan algorithm
        """
        # Find the point with the lowest y-coordinate (min function implemented in Point Class
        pivot = min(self.points)

        # Sort the points in increasing order of the angle they and the pivot point make with the x-axis
        sorted_points = sorted(self.points, key=lambda p: (
            math.atan2(p.y - pivot.y, p.x - pivot.x), (p.x - pivot.x) ** 2 + (p.y - pivot.y) ** 2))

        # Add the first two sorted points to the convex hull
        hull = [pivot, sorted_points[0]]
        for i in range(1, len(sorted_points)):
            while len(hull) >= 2 and orientation(hull[-2], hull[-1], sorted_points[i]) != 2:
                hull.pop()
            hull.append(sorted_points[i])

        # convert to list of tuple [(x,y),(x,y),(x,y)...]
        hull = [(p.x, p.y) for p in hull]

        # special case - all vertex on the same line - the convexHull is only 2 point - add 3rd point
        if len(hull) == 2:
            hull.append(hull[1])

        return hull


def orientation(p, q, r):
    """
    Returns the orientation of the triplet (p, q, r)
       0 --> p, q and r are colinear
       1 --> Clockwise
       2 --> Counterclockwise
    """
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    if val == 0:
        return 0  # colinear
    elif val > 0:
        return 1  # clockwise
    else:
        return 2  # counterclockwise


def get_points():
    points=[]
    number_of_points = random.randint(3,30)
    for point_number in range(number_of_points):
        points.append(point(x=random.randint(0,300),y=random.randint(0,300)))
    return points

flag=True
setproctitle.setproctitle("convex_hull")
print(f"long running task pid {os.getpid()}")
number_of_iterations=int(sys.argv[1]) if len(sys.argv) > 1 else 1000000
print(f"number of iterations {number_of_iterations}")
counter =0
while flag and counter<number_of_iterations:
    points=get_points()
    hull_solver=ConvexHull(points=points)
    print(f"processed {len(points)} got hull the size of {len(hull_solver.hull)}")
    counter+=1