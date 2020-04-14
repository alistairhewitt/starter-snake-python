"""
Home to hold my various experimental strategy code and appraoches. To be
used by the server.py code
"""

import global_variables as var


def _predict_future_position(current_head, next_move):
    """
    Given the current snake head position, and a proposed move,
    returns what the new snake head position would be.
    """
    future_head = current_head

    if next_move in ["left", "right"]:
        # moving left means decreasing x by 1, right increase by 1
        future_head["x"] = current_head["x"] + var.MOVE_LOOKUP[next_move]
    elif next_move in ["up", "down"]:
        # moving up means decreasing y by 1, down increase by 1
        future_head["y"] = current_head["y"] + var.MOVE_LOOKUP[next_move]
    return future_head


def avoid_wall(future_head):
    """
    Return True if the proposed future_head avoids a wall, False if it means
    you will hit a wall.
    """
    result = True

    x = int(future_head["x"])
    y = int(future_head["y"])

    if x < 0 or y < 0 or x > var.BOARD_MAXIMUM_X or y > var.BOARD_MAXIMUM_Y:
        result = False
    return result


def avoid_self(future_head, your_body):
    """
    Return True if the proposed move avoids running into yourself, false if you
    will totally run into yourself.

    TODO - this is basic, I probably want to add later a check for the tail, if
    you are about to eat food, and now you are going to get longer.
    """
    result = True

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
    future_head = _predict_future_position(current_head, next_move)
    print(f"Future head on a {next_move} is as follows: {future_head}")

    safe_wall = avoid_wall(future_head)
    safe_body = avoid_self(future_head, your_body)

    print(f"future_head {future_head}: safe_wall {safe_wall}, safe_body {safe_body}")
    is_safe = safe_wall and safe_body

    return is_safe
