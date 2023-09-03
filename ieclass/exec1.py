import numpy as np
import matplotlib.pyplot as plt

# %%%%%%%%%%%%%%%%%%%%%%%%%%%
# % dados de simulacao
# % \dot{x}(t) = -2x(t)+bu(t)
# % x = (b/(s+2))u

# %%%%%%%%%%%%%%%%%%%%%%%%%%%
# Dados de simulação
b = 3
num = [b]
den = [1, -2]  # Ajuste o sinal do coeficiente '2' para '-2' para representar o sistema correto
N = 300  # Número de amostras
dt = 0.01
T = np.arange(0, N * dt, dt)
u = np.ones(N)
y = np.zeros(N)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%
# Algoritmo de identificação de parâmetros
teta = np.zeros(N)
erro = np.zeros(N)
phi = np.zeros(N)
gama = 1000
ms = 10

# %%%%%%%%%%%%%%%%%%%%%%%%%%%
for k in range(N):
    y[k] = (b / (1 - np.exp(-2 * T[k])))  # Simulação da planta
    teta[k] = teta[k] + gama * dt * ((y[k] - teta[k] * phi[k]) / ms) * phi[k]
    phi[k] = u[k] - 2 * phi[k] * dt
    erro[k] = y[k] - teta[k] * phi[k]

# %%%%%%%%%%%%%%%%%%%%%%%%%%%
# Gráfico dos parâmetros identificados e do erro
plt.figure(figsize=(10, 6))
plt.plot(T, teta, 'b', linewidth=2, label='Parâmetro b')
plt.plot(T, erro, 'r', linewidth=2, label='Erro')
plt.legend()
plt.xlabel('Tempo')
plt.ylabel('Parâmetro Identificado / Erro')
plt.grid(True)
plt.show()
