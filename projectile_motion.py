import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

g = 9.8

initial_velocity = float(input("Enter initial velocity (m/s): "))
launch_angle = float(input("Enter launch angle (degrees): "))
g_input = input("Enter gravitational acceleration (m/s²) [9.8]: ")

if g_input.strip():
    g = float(g_input)

angle = np.radians(launch_angle)

time_of_flight = (2 * initial_velocity * np.sin(angle)) / g
maximum_height = (initial_velocity * np.sin(angle)) ** 2 / (2 * g)
range_ = (initial_velocity ** 2 * np.sin(2 * angle)) / g

t = np.linspace(0, time_of_flight, 500)

x = initial_velocity * np.cos(angle) * t
y = initial_velocity * np.sin(angle) * t - 0.5 * g * t ** 2

vx = np.full_like(t, initial_velocity * np.cos(angle))
vy = initial_velocity * np.sin(angle) - g * t
speed = np.sqrt(vx ** 2 + vy ** 2)

print("\nPROJECTILE MOTION RESULTS")
print("-" * 32)
print(f"Time of flight : {time_of_flight:.2f} s")
print(f"Maximum height : {maximum_height:.2f} m")
print(f"Range          : {range_:.2f} m")

fig, ax = plt.subplots(figsize=(10, 6))

ax.set_xlim(0, range_ * 1.08)
ax.set_ylim(0, maximum_height * 1.25)

ax.set_xlabel("Horizontal Distance (m)")
ax.set_ylabel("Vertical Height (m)")
ax.set_title("Projectile Motion Simulation")
ax.grid(True, alpha=0.3)

trajectory, = ax.plot([], [], linewidth=2, label="Trajectory")
projectile, = ax.plot([], [], "o", markersize=8, label="Projectile")
path, = ax.plot([], [], "--", alpha=0.5)

info = ax.text(
    0.02,
    0.95,
    "",
    transform=ax.transAxes,
    verticalalignment="top"
)

ax.legend()

def update(frame):
    trajectory.set_data(x[:frame + 1], y[:frame + 1])
    projectile.set_data([x[frame]], [y[frame]])
    path.set_data(x[:frame + 1], y[:frame + 1])

    info.set_text(
        f"Time: {t[frame]:.2f} s\n"
        f"Height: {y[frame]:.2f} m\n"
        f"Distance: {x[frame]:.2f} m\n"
        f"Speed: {speed[frame]:.2f} m/s"
    )

    return trajectory, projectile, path, info

animation = FuncAnimation(
    fig,
    update,
    frames=len(t),
    interval=20,
    blit=True,
    repeat=False
)

plt.tight_layout()
plt.show()

fig2, ax2 = plt.subplots(figsize=(10, 6))

ax2.plot(t, x, label="Horizontal Position x(t)")
ax2.plot(t, y, label="Vertical Position y(t)")

ax2.set_xlabel("Time (s)")
ax2.set_ylabel("Position (m)")
ax2.set_title("Projectile Position Analysis")
ax2.grid(True, alpha=0.3)
ax2.legend()

plt.tight_layout()
plt.show()