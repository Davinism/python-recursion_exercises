import pdb;

def x_traverse(x_forward, y_forward, result, depth, start_idx, start_jdx, matrix):
    if len(result) == len(matrix) * len(matrix):
        return result

    if x_forward:
        for jdx in range(0, len(matrix) - depth):
            result.append(matrix[start_idx][start_jdx + jdx])
        start_idx += 1
        start_jdx += len(matrix) - depth - 1
    else:
        for jdx in range(0, len(matrix) - depth):
            result.append(matrix[start_idx][start_jdx - jdx])
        start_idx -= 1
        start_jdx -= (len(matrix) - depth - 1)
    x_forward = not x_forward
    depth += 1
    return y_traverse(x_forward, y_forward, result, depth, start_idx, start_jdx, matrix)


def y_traverse(x_forward, y_forward, result, depth, start_idx, start_jdx, matrix):
    if len(result) == len(matrix) * len(matrix):
        return result

    if y_forward:
        for idx in range(0, len(matrix) - depth):
            result.append(matrix[start_idx + idx][start_jdx])
        start_idx += len(matrix) - depth - 1
        start_jdx -= 1
    else:
        for idx in range(0, len(matrix) - depth):
            result.append(matrix[start_idx - idx][start_jdx])
        start_idx -= (len(matrix) - depth - 1)
        start_jdx += 1
    y_forward = not y_forward
    return x_traverse(x_forward, y_forward, result, depth, start_idx, start_jdx, matrix)

def main():
    matrix = ([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ])

    result = []
    x_forward = True
    y_forward = True
    depth = 0

    print x_traverse(x_forward, y_forward, result, depth, 0, 0, matrix)

    return None

if __name__ == "__main__":
    main()
