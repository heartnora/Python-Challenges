def draw_spaces_and_xs(spaces, xs):
    """Draws a line with the given number of spaces and Xs."""
    print(" " * spaces + "X" * xs)

def draw_picture(pattern):
    """Draws a picture using the given pattern."""
    for spaces, xs in pattern:
        draw_spaces_and_xs(spaces, xs)

# Example usage:
pattern = [(5, 1), (4, 3), (3, 5), (2, 7), (1, 9)]
draw_picture(pattern)
