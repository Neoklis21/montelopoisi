import numpy as np
import random
import matplotlib.pyplot as plt

# Parameters
N = 10  # Grid size (N x N)
timesteps = 3000  # Number of time steps
network = np.zeros((N, N))  # NxN grid initialized with 0 (uninformed)

# Initial conditions
initial_x, initial_y = random.randint(0, N - 1), random.randint(0, N - 1)
network[initial_x, initial_y] = 1  # Random sensor starts informed
info_count = [1]  # Track informed sensors
time = [0]

# Simulation
for t in range(1, timesteps + 1):
    informed_sensors = np.argwhere(network == 1)  # Find all informed sensors
    
    if len(informed_sensors) == N * N:  # Stop if all sensors are informed
        break
    
    # Select a random informed sensor
    source = informed_sensors[random.randint(0, len(informed_sensors) - 1)]
    x, y = source
    
    # Define neighbors
    neighbors = []
    if x > 0: neighbors.append((x - 1, y))  # Up
    if x < N - 1: neighbors.append((x + 1, y))  # Down
    if y > 0: neighbors.append((x, y - 1))  # Left
    if y < N - 1: neighbors.append((x, y + 1))  # Right
    
    # Select a random neighbor
    target = neighbors[random.randint(0, len(neighbors) - 1)]
    tx, ty = target
    
    if network[tx, ty] == 0:  # If the neighbor is uninformed
        network[tx, ty] = 1  # Inform the neighbor
    
    # Update informed count
    info_count.append(np.sum(network))
    time.append(t)

# Save results to file
with open("discrete_transmission_data.txt", "w") as file:
    for t, count in zip(time, info_count):
        file.write(f"Time {t}: {count} informed sensors\n")

# Plot results
plt.plot(time, info_count, marker='o')
plt.title("Μετάδοση Πληροφορίας στο Δίκτυο (Διακριτή Προσέγγιση)")
plt.xlabel("Χρονική Στιγμή (t)")
plt.ylabel("Αισθητήρες με Πληροφορία")
plt.grid()
plt.show()
