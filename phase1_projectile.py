import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# PARAMETERS

g = 9.81                     # gravity m/s²
v0 = 700                  # nominal speed m/s
angle_deg = 15            # nominal launch angle
h0 = 28.6                  # initial height m
vz = 50                   # lateral velocity m/s

# uncertainty parameters

num_samples = 30          # number of uncertainty samples
v_std = 5                 # speed std dev
angle_std = 0.5           # angle std dev (degrees)

# NOMINAL TRAJECTORY

angle_rad = np.radians(angle_deg)
vx = v0 * np.cos(angle_rad)
vy = v0 * np.sin(angle_rad)

# quadratic for flight time: h0 + vy*t - 0.5*g*t^2 = 0

a = -0.5 * g
b = vy
c = h0
discriminant = b**2 - 4*a*c
t_impact = (-b + np.sqrt(discriminant)) / (2*a)
range_x = vx * t_impact
range_z = vz * t_impact

# log numerical outputs

with open("bullet_log.txt", "w") as f:
    f.write(f"Gravity: {g}\n")
    f.write(f"Launch speed: {v0}\n")
    f.write(f"Launch angle: {angle_deg}\n")
    f.write(f"Lateral speed: {vz}\n")
    f.write(f"Flight time: {t_impact:.3f} s\n")
    f.write(f"Horizontal range: {range_x:.2f} m\n")
    f.write(f"Lateral range: {range_z:.2f} m\n")

# 3D TRAJECTORY WITH UNCERTAINTY

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel("X (forward m)")
ax.set_ylabel("Z (lateral m)")
ax.set_zlabel("Height (m)")
ax.set_title("Bullet Trajectory with Uncertainty")

# time array

t = np.linspace(0, t_impact, 500)

# plot nominal trajectory

x_nom = vx * t
y_nom = h0 + vy * t - 0.5 * g * t**2
z_nom = vz * t
ax.plot(x_nom, z_nom, y_nom, color='red', label='Nominal')

# plot uncertainty bands

v_samples = np.random.normal(v0, v_std, num_samples)
angle_samples = np.random.normal(angle_deg, angle_std, num_samples)

for v_s, a_s in zip(v_samples, angle_samples):
    a_rad = np.radians(a_s)
    vx_s = v_s * np.cos(a_rad)
    vy_s = v_s * np.sin(a_rad)
    x_s = vx_s * t
    y_s = h0 + vy_s * t - 0.5 * g * t**2
    z_s = vz * t
    mask = y_s >= 0
    ax.plot(x_s[mask], z_s[mask], y_s[mask], color='blue', alpha=0.2)

ax.legend()
plt.show()
