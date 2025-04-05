import numpy as np
import matplotlib.pyplot as plt

def create_pentagon(center_x, center_y, size):
    angles = np.linspace(0, 2 * np.pi, 6)
    x = center_x + size * np.cos(angles)
    y = center_y + size * np.sin(angles)
    return np.column_stack((x, y))

def transform(vertices, matrix):
    homogeneous_vertices = np.hstack((vertices, np.ones((vertices.shape[0], 1))))
    transformed_vertices = np.dot(homogeneous_vertices, matrix.T)
    return transformed_vertices[:, :2]

def translation_matrix(tx, ty):
    return np.array([
        [1, 0, 0],
        [0, 1, 0],
        [tx, ty, 1]
    ])

def rotation_matrix(angle):
    theta = np.radians(angle)
    return np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])

def scaling_matrix(sx, sy):
    return np.array([
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, 1]
    ])

def composite_transformation(vertices, tx, ty, angle, sx, sy):
    translation = translation_matrix(tx, ty)
    vertices = transform(vertices, translation)
    rotation = rotation_matrix(angle)
    vertices = transform(vertices, rotation)
    scaling = scaling_matrix(sx, sy)
    vertices = transform(vertices, scaling)
    return vertices

center_x, center_y = 0, 0
size = 1
pentagon_vertices = create_pentagon(center_x, center_y, size)
tx, ty = 4, 3
angle = 52
sx, sy = 1, 2.5
transformed_pentagon = composite_transformation(pentagon_vertices, tx, ty, angle, sx, sy)

plt.figure()
plt.plot(pentagon_vertices[:, 0], pentagon_vertices[:, 1], label="Original Pentagon")
plt.plot(transformed_pentagon[:, 0], transformed_pentagon[:, 1], label="Transformed Pentagon")
plt.legend()
plt.grid(True)
plt.axis("equal")
plt.title("Composite 2D Transformations on a Pentagon")
plt.show()
