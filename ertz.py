import numpy as np
import matplotlib.pyplot as plt

def simulate_information_spread_until_full(N):
    """
    Simulate information spread in a NxN grid network until all sensors are informed.
    Args:
        N: Size of the grid (NxN).
    Returns:
        A list of the number of informed sensors at each time step.
    """
    grid_size = N * N
    informed = np.zeros(grid_size, dtype=int)  # 1D array for the grid
    initial_sensor = np.random.randint(grid_size)  # Randomly choose initial sensor
    informed[initial_sensor] = 1  # Mark initial sensor as informed
    
    informed_counts = [1]  # Start with one informed sensor
    steps = 0
    
    while np.sum(informed) < grid_size:  # Run until all sensors are informed
        # Find currently informed sensors
        current_informed_indices = np.where(informed == 1)[0]
        
        # Randomly choose one informed sensor to spread the information
        spreading_sensor = np.random.choice(current_informed_indices)
        
        # Find neighbors in the grid
        row, col = divmod(spreading_sensor, N)
        neighbors = []
        if row > 0: neighbors.append(spreading_sensor - N)  # Up
        if row < N-1: neighbors.append(spreading_sensor + N)  # Down
        if col > 0: neighbors.append(spreading_sensor - 1)  # Left
        if col < N-1: neighbors.append(spreading_sensor + 1)  # Right
        
        # Randomly choose one neighbor to inform
        uninformed_neighbors = [n for n in neighbors if informed[n] == 0]
        if uninformed_neighbors:
            new_informed = np.random.choice(uninformed_neighbors)
            informed[new_informed] = 1
        
        # Count the total number of informed sensors
        informed_counts.append(np.sum(informed))
        steps += 1  # Increment steps
    
    return informed_counts

def plot_results_until_full(N_values):
    """
    Plot the normalized results for different grid sizes, running until full coverage.
    Args:
        N_values: List of grid sizes (NxN).
    """
    plt.figure(figsize=(10, 6))
    
    for N in N_values:
        informed_counts = simulate_information_spread_until_full(N)
        normalized_counts = [count / (N * N) for count in informed_counts]
        plt.plot(range(len(normalized_counts)), normalized_counts, label=f'N={N}')
    
    plt.title('Normalized Information Spread Over Time (Until Full Coverage)')
    plt.xlabel('Time Steps (t)')
    plt.ylabel('Normalized Informed Sensors (I/N)')
    plt.legend()
    plt.grid()
    plt.show()

# Parameters
N_values = [5, 10, 30, 50, 100]  # Grid sizes

# Run and plot results
plot_results_until_full(N_values)
