import os
import shutil

def delete_pycache(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Crea una lista de directorios para eliminar mientras iteras
        dirs_to_remove = [d for d in dirnames if d == '__pycache__']
        
        for dir_to_remove in dirs_to_remove:
            full_path = os.path.join(dirpath, dir_to_remove)
            print(f"Eliminando {full_path}")
            # Elimina el directorio y todo su contenido
            shutil.rmtree(full_path)

# Especifique aquí el directorio raíz que desea limpiar
root_directory = '/Users/antonio.vallejo/Documents/Coding/Python/ToDo'
delete_pycache(root_directory)