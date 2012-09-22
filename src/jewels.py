from math import sqrt


# TODO: wildcard jewel
JEWELS = {
    ("orange", "normal"): (226, 130, 49),
    ("green", "normal"): (40, 209, 71),
    ("green", "fire"): (84, 238, 115),
    ("green", "cross"): (72, 223, 120),
    ("purple", "normal"): (150, 42, 158),
    ("purple", "fire"): (204, 94, 193),
    ("purple", "cross"): (189, 121, 204),
    ("white", "normal"): (206, 206, 206),
    ("white", "fire"): (239, 238, 236),
    ("yellow", "normal"): (202, 179, 37),
    ("yellow", "fire"): (232, 201, 57),
    ("yellow", "cross"): (227, 227, 179),
    ("red", "normal"): (230, 24, 52),
    ("red", "fire"): (245, 48, 77),
    ("blue", "normal"): (21, 113, 197),
    ("blue", "fire"): (52, 128, 199),
    ("wildcard", "special"): (142, 158, 132)
}


def get_closest_jewel(color):
    """Given a color from the screen, find the closest jewel color and
    kind.

    >>> get_closest_jewel((225, 129, 50))
    ("orange", "normal")

    """
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


