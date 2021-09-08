import os       #Importamos modulo que nos ayuda a cambiar de directorio
import shutil   #Importamos modulo que nos ayuda a copiar información 
import sys      #importamos modulo para terminar ejecución en caso de exepción 


def backup():
    print('Introduce la ruta del directorio donde se encuentra el archivo:')
    source = input()
    print('Introduce el nombre del archivo:')
    file = input()
    print('Introduce la ruta del directorio destino:')
    destiny = input()

    try:
        # Nos movemos a la ruta donde se encuentra el archivo a respaldar 
        os.chdir(source)

        # Primer parámetro es el archivo a respaldar, segundo la ruta donde se copiará
        shutil.copy(file,destiny)
    except:
        print('Algo no salió bien con el respaldo.')
        sys.exit()
    
    print('Respaldo terminado')

while True:
    print('\n************Bienvenido al respaldo de archivos mamalones**********\n')
    
    # Funcion que respalda un archivo
    backup()

    salir = input('\n1.- Salir  \n0.- Realizar otro respaldo\n')

    if salir == '1':
        sys.exit()