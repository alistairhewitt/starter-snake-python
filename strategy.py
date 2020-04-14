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
        future_head["x"] = current_head["x"] - 1
    elif next_move == "right":
        # moving right means increasing x by 1
        future_head["x"] = current_head["x"] + 1
    elif next_move == "up":
        # moving up means decreasing Y by 1
        future_head["y"] = current_head["y"] - 1
    elif next_move == "down":
        # moving down means increasing Y by 1
        future_head["y"] = current_head["y"] + 1
    return future_head


def avoid_walls(current_head, next_move):
    """
    Return True if the proposed move avoids a wall, False if it means you will
    hit a wall.
    """
    result = True

    future_head = _predict_future_position(current_head, next_move)
    # print(f"Future head on a {next_move} is as follows: {future_head}")

    x = int(future_head["x"])
    y = int(future_head["y"])

    if x < 0 or y < 0:
        result = False
    elif x > global_variables.BOARD_MAXIMUM_X:
        result = False
    elif y > global_variables.BOARD_MAXIMUM_Y:
        result = False

    # print(f"Future head will NOT result in a wall collision? {result}")
    return result


def stop_hitting_yourself(your_body, next_move):
    """
    Return True if the proposed move avoids running into yourself, false if you
    will totally run into yourself.

    TODO - this is basic, I probably want to add later a check for the tail, if
    you are about to eat food, and now you are going to get longer.
    """
    result = True
    future_head = _predict_future_position(your_body[0], next_move)

    if future_head in your_body:
        result = False

    return result


def validate_move(your_body, next_move):
    """
    Basic set of logical checks that only prevent disaster. This function is not
    responsible for picking a move, it is responsible for saying if that move
    if safe.
    Return True if safe, False if not (and another move is needed).
    """
    current_head = your_body[0]

    safe_wall = avoid_walls(current_head, next_move)
    safe_body = stop_hitting_yourself(your_body, next_move)

    is_safe = safe_wall and safe_body
    return is_safe
