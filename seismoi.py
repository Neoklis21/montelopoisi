import numpy as np

# Parameters
N, M = 10, 10  # Grid size
F_crit = 4  # Critical force
F_out = 0.01  # Incremental force per time step
time_steps = 1000000  # Number of time steps

# Initialize the grid with random values between 0 and F_crit
grid = np.random.uniform(0, F_crit, (N, M))

# File to record seismic activity
output_file = "seismic_activity.txt"

# Step B: Increment values and record activity
def step_b(grid, F_crit, F_out, time_steps, output_file):
    with open(output_file, "w") as file:
        for t in range(time_steps):
            if np.any(grid > F_crit):
                print("At time step {}, some cells exceeded the critical force.".format(t))
                return  # If Step B is not applicable, exit early

            # Record no seismic activity
            file.write("Time step {}: Earthquake size = 0\n".format(t))
            print("Time step {}: Earthquake size = 0".format(t))

            # Increment all grid values by F_out
            grid += F_out

# Execute Step B
print("Initial Grid:")
print(grid)
step_b(grid, F_crit, F_out, time_steps, output_file)
print("Seismic activity recorded in {}".format(output_file))
