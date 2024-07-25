#!/usr/bin/python3
"""
Pascal's Triangle Generator

This module provides a function to generate Pascal's Triangle up to n rows.
Pascal's Triangle is a triangular array of the binomial coefficients that arises
in probability theory, combinatorics, and algebra.

Function:
    pascal_triangle(n): Returns a list of lists representing Pascal's Triangle.

Each number is the sum of the two numbers directly above it.
"""

def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]  # Start with the first row

    for i in range(1, n):
        row = [1]  # Every row starts with a 1
        for j in range(1, i):
            # Calculate the value based on the two values directly above it
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # Every row ends with a 1
        triangle.append(row)

    return triangle

def print_triangle(triangle):
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
