# Step 1: Import libraries
import numpy as np            # for calculations
import matplotlib.pyplot as plt  # for plotting

# Step 2: Define constants
g = 9.81  # gravity in m/s²

# Step 3: Set initial conditions
v0 = 700         # initial speed in m/s
angle_deg = 15   # launch angle in degrees
h0 = 1.5         # initial height in meters

# Step 4: Convert angle to radians
angle_rad = np.radians(angle_deg)

# Step 5: Calculate velocity components
vx = v0 * np.cos(angle_rad)  # horizontal speed
vy = v0 * np.sin(angle_rad)  # vertical speed

# Step 6: Create time array
t_max = 2                       # maximum time to simulate (seconds)
num_points = 500                 # number of points in the simulation
t = np.linspace(0, t_max, num_points)

# Step 7: Calculate positions
x = vx * t                          # horizontal positions
y = h0 + vy * t - 0.5 * g * t**2   # vertical positions

# Step 8: Remove points below ground
ground_mask = y >= 0
x = x[ground_mask]
y = y[ground_mask]

# Step 9: Plot trajectory
plt.figure(figsize=(8,4))
plt.plot(x, y, color='blue')
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Height (m)")
plt.title("Step-by-Step Bullet Trajectory")
plt.grid(True)
plt.show()
