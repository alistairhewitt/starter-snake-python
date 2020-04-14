"""
Home to hold my various experimental strategy code and appraoches. To be
used by the server.py code
"""

import global_variables


def _predict_future_position(current_head, next_move):
    """
    Given the current snake head position, and a proposed move,
    returns what the new snake head position would be.
    """
    future_head = current_head
    if next_move == "left":
        # moving left means decreasing x by 1
        future_head["x"] = future_head["x"] - 1
    elif next_move == "right":
        # moving right means increasing x by 1
        future_head["x"] = future_head["x"] + 1
    elif next_move == "up":
        # moving up means decreasing Y by 1
        future_head["y"] = future_head["y"] - 1
    elif next_move == "down":
        # moving down means increasing Y by 1
        future_head["y"] = future_head["y"] + 1
    return future_head


def avoid_walls(current_head, next_move):
    """
    Return True if the proposed move avoids a wall, False if it means you will
    hit a wall.
    """
    result = True

    future_head = _predict_future_position(current_head, next_move)
    print(f"Future head on a {next_move} is as follows: {future_head}")

    if future_head["x"] < 0 or future_head["y"] < 0:
        result = False
    elif future_head["x"] > global_variables.BOARD_MAXIMUM_X:
        result = False
    elif future_head["y"] > global_variables.BOARD_MAXIMUM_Y:
        result = False

    print(f"Future head will NOT result in a wall collision? {result}")
    return result
