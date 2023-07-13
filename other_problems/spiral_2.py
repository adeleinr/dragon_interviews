def spiral(matrix):
    top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
    direction = "right"
    result = []

    while top <= bottom and left <= right:
        if direction == "right":
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1
            direction = "down"
        elif direction == "down":
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1
            direction = "left"
        elif direction == "left":
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
            direction = "up"
        elif direction == "up":
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
            direction = "right"

    return result
