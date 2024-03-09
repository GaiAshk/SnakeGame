from src.modles.modles import Location


def do_location_intersect(
    location_a: Location, location_b: Location, threshold: int
) -> bool:
    """do 2 location intersect, when taking threshold around location a"""
    location_a_x = location_a[0]
    location_a_x_left_range = location_a_x - threshold
    location_a_x_right_range = location_a_x + threshold

    location_b_x = location_b[0]
    if not (location_a_x_left_range <= location_b_x <= location_a_x_right_range):
        return False

    location_a_y = location_a[1]
    location_a_y_top_range = location_a_y - threshold
    location_a_y_bottom_range = location_a_y + threshold

    location_b_y = location_b[1]
    if not (location_a_y_top_range <= location_b_y <= location_a_y_bottom_range):
        return False

    return True
