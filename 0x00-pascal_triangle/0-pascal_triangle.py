#!/usr/bin/python3
"""Defining the function for the pascal triangle"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the Pascalal
    triangle of n.
    Arguments:
        n (int): Height of the triangle.
    """
    triangle = []
    
    for i in range(n):
        if i == 0:
            triangle.append([1])
        else:
            row = [1]
            for j in range(i - 1):
                row.append(triangle[i-1][j] + triangle[i-1][j+1])
            row.append(1)
            triangle.append(row)
    return triangle
    