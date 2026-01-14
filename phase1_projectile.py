import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# PHASE 1: BASIC PROJECTILE MOTION
# -----------------------------

# Constants
GRAVITY = 9.81  # m/s^2

# Initial conditions (you can change these)
initial_speed = 700      # m/s
launch_angle_deg = 15    # degrees
initial_height = 1.5     # meters (approx shoulder height)

# Convert angle to radians
launch_angle_rad = np.radians(launch_angle_deg)

# Initial velocity components
vx = initial_speed * np.cos(launch_angle_rad)
vy = initial_speed * np.sin(launch_angle_rad)

# Time array
t = np.linspace(0, 2, 500)  # simulate first 2 seconds

# Position equations
x = vx * t
y = initial_height + vy * t - 0.5 * GRAVITY * t**2

# Stop trajectory when bullet hits the ground
ground_index = np.where(y >= 0)
x = x[ground_index]
y = y[ground_index]

# Plot
plt.figure()
plt.plot(x, y)
plt.xlabel("Horizontal Distance (meters)")
plt.ylabel("Height (meters)")
plt.title("Phase 1: Basic Bullet Trajectory")
plt.grid(True)
plt.show()
