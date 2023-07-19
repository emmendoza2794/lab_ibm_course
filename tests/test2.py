import os

# Obtiene la ruta absoluta del archivo actual
current_file = os.path.abspath(__file__)

# Obtiene el directorio padre (root) del proyecto
project_root = os.path.dirname(os.path.dirname(current_file))

# Imprime el path root del proyecto
print("Path root del proyecto:", project_root)
