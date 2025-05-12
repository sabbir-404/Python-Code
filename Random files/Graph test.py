import matplotlib.pyplot as plt
import numpy as np

# Constants
k_e = 8.99e9  # N·m²/C²
q = 1e-8  # C

# Positions of the charges
pos_q1 = np.array([0.1, 0])
pos_q2 = np.array([-0.1, 0])

# Define the points of interest
points = {
    "Origin (0,0)": np.array([0, 0]),
    "(0.2, 0)": np.array([0.2, 0]),
    "(0.1, 0.15)": np.array([0.1, 0.15]),
    "(0, 0.1)": np.array([0, 0.1])
}

# Function to calculate the electric field at a point due to a charge
def electric_field(q, r_vec):
    r_mag = np.linalg.norm(r_vec)
    r_hat = r_vec / r_mag
    return k_e * q / r_mag**2 * r_hat

# Calculate the electric fields at the points
fields = {}
for label, point in points.items():
    E_q1 = electric_field(q, point - pos_q1)
    E_q2 = electric_field(q, point - pos_q2)
    fields[label] = E_q1 + E_q2

# Plotting
fig, ax = plt.subplots()
ax.set_aspect('equal', adjustable='box')
ax.grid(True)

# Plot the positions of the charges
ax.scatter(*pos_q1, color='red', label='q1: 1e-8 C', marker='o')
ax.scatter(*pos_q2, color='red', label='q2: 1e-8 C', marker='o')

# Plot the points and electric field vectors
for label, point in points.items():
    ax.scatter(*point, label=label, marker='x')
    E = fields[label]
    ax.quiver(point[0], point[1], E[0], E[1], angles='xy', scale_units='xy', scale=5e9, color='blue')

# Annotate the points
for label, point in points.items():
    ax.annotate(label, (point[0], point[1]), textcoords="offset points", xytext=(5,-10), ha='center')

# Add labels, title and legend
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(-0.5, 0.5)
ax.set_xlabel('x (m)')
ax.set_ylabel('y (m)')
ax.set_title('Electric Field due to Two Charges')
ax.legend()

plt.show()
