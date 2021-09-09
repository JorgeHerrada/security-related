import os       #Importamos modulo que nos ayuda a cambiar de directorio
import shutil   #Importamos modulo que nos ayuda a copiar información 
import sys      #importamos modulo para terminar ejecución en caso de exepción 


def restore():

    print('Elige la opcion que deseas recuperar del respaldo: ')
    opt = input('1.- Fotos\n2.- Tareas\n0.- CANCELAR y SALIR\n')
    
    if opt == '1':
        print('Introduce la ruta del directorio destino donde quieres guardar la información recuperada:')
        #C:\\Users\\toluc\\OneDrive\\Documentos\\Jorge\\INCO\\7mo Semestre\\Seguridad - Armida\\Act 2.2 Recuperacion
        destiny = input()
        source = 'C:\\Users\\toluc\\OneDrive\\Documentos\\BACKUP\\fotos'
        file = 'familia.jpg'
        try:
            # Nos movemos a la ruta donde se encuentra el archivo a recuperar 
            os.chdir(source)

            # Primer parámetro es el archivo a recuperar, segundo la ruta donde se copiará
            shutil.copy(file,destiny)
        except:
            print('Algo no salió bien con la recuperacion de la información.')
            sys.exit()
        
        print('Recuperación terminada')
    elif opt == '2':
        print('Introduce la ruta del directorio destino donde quieres guardar la información recuperada:')
        #C:\\Users\\toluc\\OneDrive\\Documentos\\Jorge\\INCO\\7mo Semestre\\Seguridad - Armida\\Act 2.2 Recuperacion
        destiny = input()
        source = 'C:\\Users\\toluc\\OneDrive\\Documentos\\BACKUP\\tareas'
        file = 'TAREA.txt'
        try:
            # Nos movemos a la ruta donde se encuentra el archivo a recuperar 
            os.chdir(source)

            # Primer parámetro es el archivo a recuperar, segundo la ruta donde se copiará
            shutil.copy(file,destiny)
        except:
            print('Algo no salió bien con la recuperación de la información.')
            sys.exit()
        
        print('Recuperación terminada')
    elif opt == '0':
        sys.exit()
    else:
        print('No se ha reconocido la opcion, intenta de nuevo')
    
        

while True:
    print('\n************Bienvenido a la recuperacion de archivos mamalones**********\n')
    
    # Funcion que respalda un archivo
    restore()

    salir = input('\n1.- Salir  \n0.- Realizar otra recuperación\n')

    if salir == '1':
        sys.exit()