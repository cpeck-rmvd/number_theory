import numpy as np

def green(P, Q, C):
    # Approximate the line integral around the curve C with a finite sum of line segments
    integral = 0
    for i in range(len(C) - 1):
        x1, y1 = C[i]
        x2, y2 = C[i + 1]
        integral += (P(x1, y1) * (x2 - x1) + Q(x1, y1) * (y2 - y1))

    # Approximate the double integral over the region bounded by the curve C with a finite sum of rectangles
    dx = 0.1
    dy = 0.1
    double_integral = 0
    for x in np.arange(C[:, 0].min(), C[:, 0].max(), dx):
        for y in np.arange(C[:, 1].min(), C[:, 1].max(), dy):
            double_integral += (Q(x + dx, y) - Q(x, y)) * dx - (P(x, y + dy) - P(x, y)) * dy

    # Compare the line integral and the double integral
    print(f"Line integral: {integral}")
    print(f"Double integral: {double_integral}")

# Example usage

# Define the functions P and Q
def P(x, y):
    return x ** 2 + y ** 2

def Q(x, y):
    return x + y

# Define the curve C as a list of points
C = np.array([[0, 0], [1, 1], [1, 0], [0, 1], [0, 0]])

green(P, Q, C)
