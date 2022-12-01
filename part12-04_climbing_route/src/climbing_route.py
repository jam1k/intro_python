class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"

# Write your solution herer:
def order_by_length(route: ClimbingRoute):
        return route.length

def sort_by_length(routes: list):
    
    return sorted(routes, key = order_by_length, reverse = True)

def sort_by_difficulty(routes: list):
    def order_by_difficulty (route: ClimbingRoute):
        return (route.grade, route.length)
    return sorted(routes, reverse=True, key = order_by_difficulty)
if __name__ == "__main__":
    r1 = ClimbingRoute("Edge", 38, "6A+")
    r2 = ClimbingRoute("Smooth operator", 9, "7A")
    r3 = ClimbingRoute("Syncro", 14, "8C+")
    sort_by_difficulty([r1, r2, r3])
    for route in sort_by_difficulty([r1, r2, r3]):
        print(route)