import numpy as np
import matplotlib.pyplot as plt


N = 1000  
beta = 0.1  
timesteps = 1000  


I = np.zeros(timesteps) 
S = np.zeros(timesteps) 
I[0] = 1  
S[0] = N - I[0] 

t = 1  


while t < timesteps and S[t - 1] > 0:
    new_infections = beta * I[t - 1] * S[t - 1] / N
    I[t] = I[t - 1] + new_infections
    S[t] = S[t - 1] - new_infections
    
    t += 1  

I = np.clip(I, 0, N)

plt.figure(figsize=(10, 5))
plt.plot(I[:t], label='Μολυσμένοι Υπολογιστές')  
plt.xlabel('Χρόνος')
plt.ylabel('Αριθμός Μολυσμένων')
plt.title('Μετάδοση Κακόβουλου Λογισμικού σε Δίκτυο Υπολογιστών')
plt.legend()
plt.grid()
plt.show()
