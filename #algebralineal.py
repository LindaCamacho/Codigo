import numpy as np # type: ignore

# Definimos el espacio S y los vectores u, v, w, z
S = np.array([[6, -7, 8, 6], [4, 6, -4, 1]])
u = np.array([-42, 113, -112, -60])
v = np.array([49/2, 98/4, -14, 19/2])
w = np.array([-4, -14, 27/2, 53/8])
z = np.array([8, 4, -1, 17/4])

# Función para verificar si un vector puede ser expresado como una combinación lineal de los vectores en S
def es_combinacion_lineal(S, vector):
    try:
        # Intentamos resolver el sistema de ecuaciones lineales
        coeficientes = np.linalg.solve(S.T, vector)
        return True
    except np.linalg.LinAlgError:
        # Si el sistema no tiene solución, el vector no puede ser expresado como una combinación lineal de S
        return False

# Verificamos si cada vector puede ser expresado como una combinación lineal de los vectores en S
print("u es combinación lineal de S:", es_combinacion_lineal(S, u))
print("v es combinación lineal de S:", es_combinacion_lineal(S, v))
print("w es combinación lineal de S:", es_combinacion_lineal(S, w))
print("z es combinación lineal de S:", es_combinacion_lineal(S, z))
