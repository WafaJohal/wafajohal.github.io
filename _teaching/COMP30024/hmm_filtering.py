import matplotlib.pyplot as plt
import numpy as np

# Transition probabilities: P(state_t | state_{t-1})
transition_matrix = np.array([[0.5, 0.5], [0.5, 0.5]]) # these should be changed

sensor_enabled  = True
# Sensor model: P(observation_t | state_t)
sensor_model = np.array([[0.5, 0.5], [0.5, 0.5]]) # these should be changed

# Initial state distribution
initial_distribution = np.array([1, 0])

# Observations: 1 (True), 0 (False)
observations = [1, 1, 1, 1, 1, 0, 0]

# Function to perform forward filtering (forward algorithm)
def forward_filtering(observations, transition_matrix, sensor_model, initial_distribution):
    num_states = transition_matrix.shape[0]
    num_obs = len(observations)
    alpha = np.zeros((num_obs, num_states))
    
    # Initialize with initial distribution
    if(sensor_enabled):
        alpha[0, :] = initial_distribution * sensor_model[:, observations[0]]
    else:
        alpha[0, :] = initial_distribution 
    
    # Forward pass
    for t in range(1, num_obs):
        for s in range(num_states):
            if(sensor_enabled):
                alpha[t, s] = np.sum(alpha[t - 1, :] * transition_matrix[:, s]) * sensor_model[s, observations[t]]
            else:
                alpha[t, s] = np.sum(alpha[t - 1, :] * transition_matrix[:, s]) 
    
    # Normalize each step to get probabilities
    for t in range(num_obs):
        alpha[t, :] /= np.sum(alpha[t, :])
    
    return alpha

# Run the forward filtering algorithm
alpha = forward_filtering(observations, transition_matrix, sensor_model, initial_distribution)

# Visualize the probability distribution over time
plt.figure(figsize=(10, 6))
plt.plot(alpha[:, 0], label='Rain')
plt.plot(alpha[:, 1], label='No Rain')
#plt.plot(observations, label='Umbrella')
plt.legend()
plt.xlabel('Time Step')
plt.ylabel('Probability')
plt.title('State Probability Distribution Over Time (HMM)')
plt.grid(True)
plt.show()
