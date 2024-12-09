import numpy as np
import matplotlib.pyplot as plt

# Parameters
N, M = 10, 10  # Grid dimensions
F_crit = 4  # Critical force
F_out = 0.001  # Incremental force per time step
max_idle_steps = 100  # Maximum consecutive idle steps before stopping
time_steps = 10000  # Safety limit for maximum time steps

# Initialize the grid
grid = np.random.uniform(0, F_crit, (N, M))

# Secondary grids for redistribution and seismic activity
seismic_activity_grid = np.zeros((N, M))

# File to record seismic activity
output_file = "seismic_activity_ofc_scaled.txt"

# Simulation
def ofc_simulation(grid, F_crit, F_out, max_idle_steps, time_steps, output_file):
    seismic_magnitudes = []
    idle_steps = 0  # Counter for idle steps (no seismic events)

    with open(output_file, "w") as file:
        for t in range(time_steps):
            grid += F_out  # Increment all grid values

            # Step A: Check for cells exceeding critical force
            while np.any(grid > F_crit):
                exceeded = np.argwhere(grid > F_crit)
                for i, j in exceeded:
                    redistribution_amount = grid[i, j] / 4
                    grid[i, j] = 0
                    seismic_activity_grid[i, j] = 1  # Mark this cell as part of the seismic event

                    # Distribute force to neighbors
                    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < N and 0 <= nj < M:  # Check boundaries
                            grid[ni, nj] += redistribution_amount

            # Measure earthquake magnitude after redistribution
            earthquake_size = np.sum(seismic_activity_grid)  # Total affected cells
            seismic_activity_grid.fill(0)  # Reset seismic activity grid

            if earthquake_size > 0:
                scaled_magnitude = 2 * np.log10(earthquake_size) + 3  # Scale logarithmically
                idle_steps = 0  # Reset idle counter if seismic event occurs
                file.write(f"Time step {t}: Scaled Earthquake Magnitude = {scaled_magnitude:.2f}\n")
                print(f"Time step {t}: Scaled Earthquake Magnitude = {scaled_magnitude:.2f}")
                seismic_magnitudes.append(scaled_magnitude)
            else:
                idle_steps += 1
                seismic_magnitudes.append(0)

            # Stop if no seismic activity for consecutive steps
            if idle_steps >= max_idle_steps:
                print(f"Simulation stabilized after {t} steps.")
                break

    return seismic_magnitudes

# Run simulation
seismic_magnitudes = ofc_simulation(grid, F_crit, F_out, max_idle_steps, time_steps, output_file)

# Plot results
plt.plot(seismic_magnitudes, label="Earthquake Magnitudes")
plt.xlabel("Time Steps")
plt.ylabel("Earthquake Magnitude")
plt.title("Seismic Activity over Time (Scaled)")
plt.legend()
plt.show()
