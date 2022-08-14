def isRobotBounded(instructions: str) -> bool:
    x, y, dx, dy = 0, 0, 0, 1
    for i in instructions:
        if i == "G":
            x += dx
            y += dy
        elif i == "L":
            dx, dy = dy, -dx
        elif i == "R":
            dx, dy = -dy, dx
    return x == 0 and y == 0 or dx != 0 or dy != 1


print(isRobotBounded("GG"))
