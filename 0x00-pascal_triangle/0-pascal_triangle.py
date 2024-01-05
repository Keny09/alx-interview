def pascal_triangle(n):
    # Create an empty list to store the triangle
    triangle = []

    # If n <= 0, return the empty list
    if n <= 0:
        return triangle

    # Iterate over the range of 1 to n + 1 (inclusive)
    for i in range(1, n + 1):
        # Append a new row to the triangle
        triangle.append([])

        # The first and last element of each row should be 1
        triangle[i - 1].append(1)

        # The remaining elements in the row should be the sum of the elements immediately above and left of the current element in the previous row
        for j in range(1, i):
            triangle[i - 1].append(triangle[i - 2][j - 1] + triangle[i - 2][j])

        # The last element of each row should be 1
        triangle[i - 1].append(1)

    return triangle