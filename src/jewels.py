from math import sqrt


# TODO: wildcard jewel
JEWELS = {
    "orange": (226, 130, 49),
    "green": (40, 209, 71),
    "purple": (150, 42, 158),
    "white": (206, 206, 206),
    "yellow": (202, 179, 37),
    "red": (230, 24, 52),
    "blue": (21, 113, 197)
}


def get_closest_jewel(color):
    """Given a color from the screen, find the closest jewel color."""
    first_color = JEWELS.keys()[0]

    # initialise
    closest_color = first_color
    shortest_distance = get_distance(color, JEWELS[first_color])

    # find the closest color
    for jewel_name, jewel_color in JEWELS.items():
        distance = get_distance(color, jewel_color)

        if distance < shortest_distance:
            shortest_distance = distance
            closest_color = jewel_name

    return closest_color


def get_distance(x, y):
    """Find the Euclidean distance between two 3-dimensional points."""
    p1, p2, p3 = x
    q1, q2, q3 = y

    distance = sqrt((p1 - q1) ** 2 + (p2 - q2) ** 2 + (p3 - q3) ** 2)
    return distance


