import numpy as np
import matplotlib.pyplot as plt

#模型参数
r = 0.5
K = 1000
d = 0.1
k = 0.01
g = 0.5
h = 0.2

dt = 0.1
num_steps = 1000

N = np.zeros(num_steps)
F = np.zeros(num_steps)
M = np.zeros(num_steps)
food = np.zeros(num_steps)

N[0] = 500
F[0] = 250
M[0] = 250
food[0] = 1000

for i in range(1, num_steps):
    P_female = k * (N[i-1]/k)* (F[i-1]/ (F[i-1] + M[i-1]))
    P_male =k * (N[i-1] / K)* (M[i-1]/(F[i-1]+ M[i-1]))

    N[i]=N[i-1] + dt * (r * N[i-1] * (1 - N[i-1]/K) -d *N[i-1])
    F[i]= F[i-1] + dt * (P_male * M[i-1] - d * F[i-1])
    M[i]= M[i-1] + dt * (P_female * F[i-1] - d * M[i-1])

    food[i]= food[i-1]+dt * (g * food[i-1] * (1 - N[i-1] / K)-h * food[i-1]*(F[i-1]+M[i-1]))

time= np.arange(0, num_steps * dt, dt)

plt.figure(figsize=(10, 6))
plt.plot(time, N, label='Total Population')
plt.plot(time, F, label='Female')
plt.plot(time, M, label='Male')
plt.plot(time, food, label='Food')
plt.xlabel('Time')
plt.ylabel('Quantity')
plt.title('Population Dynamics')
plt.legend()
plt.show()
plt.savefig('lamprey_model.png')