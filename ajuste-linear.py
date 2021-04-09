# importando as bibliotecas
import numpy as np 
import matplotlib.pyplot as plt 


# Introduzindo dados manualmente
x = np.array([5.1,10.2,15.4,20.1,24.9]) 
y = np.array([10.22,20.02,29.99,40.15,50.3])
inc = np.array([2.00,4.00,7.00,4.00,3.00]) # incerteza em y


# gerando gráfico
plt.errorbar(x, y, yerr=inc, fmt='o', markersize=8, capsize=5)
# fmt        - formato dos pontos.
# markersize - tamanho dos pontos.
# capsize    - Tamanho do traço superior e inferior da barra de erro. 

# descrição dos eixos
plt.xlabel('X (m)')
plt.ylabel('Y (m)')
plt.show()



# Definindo função f(x)=A+B*x
def f(x, A, B):
        return A + B*x
# Parâmetros da função f(x)
A=-0.52 ; B=2.02

# redefinindo os valores em x. Não é necessário calcular nos mesmos 
# pontos experimentais
x_fit = np.arange(0,30.0,0.5)
# obtendo y através da função ajustada f(x)=A+B*x
y_fit = f(x_fit, A, B)

# incluindo um grid no gráfico para melhor vizualização
plt.grid()

# gráfico dos pontos experimentais com suas incertezas
plt.errorbar(x, y, yerr=inc, fmt='o', markersize=8, capsize=5)

#gráfico do ajuste linead f(x)=A+B*x
plt.plot(x_fit, y_fit, '--', color='red')

# Definindo os limites de x e y.
plt.xlim(min(x_fit),max(x_fit))
plt.ylim(min(y_fit),max(y_fit))

# descrição dos eixos x e y
plt.xlabel('X (m)')
plt.ylabel('Y (m)')

plt.show()

# Gráfico de resíduos.
# Parâmetros da função f(x)
A=-0.52 ; B=2.02

# obtendo y através da função ajustada f(x)=A+B*x
y_fit = f(x, A, B)

# incluindo um grid no gráfico para melhor vizualização
plt.grid()

# gráfico dos resíduos. y-(A+b*x)
plt.errorbar(x, y-y_fit, fmt='--o', markersize=8, capsize=5)

# Definindo os limites de x e y.
plt.xlim(min(x_fit),max(x_fit))
plt.ylim(min(y-y_fit)-0.1,max(y-y_fit)+0.1)

# descrição dos eixos x e y
plt.xlabel('X (m)')
plt.ylabel('Y (m)')
plt.show()
