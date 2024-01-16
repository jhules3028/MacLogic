import mysql.connector

def Conexion(opcion,usuario,contraseña,correo):
    # Establecer conexión a la base de datos en DB4FREE
    mydb = mysql.connector.connect(
      host="db4free.net",
      user="jendicdncjidn",
      password="ElpincheMomoEstaHermoso9877@",
      database="kakcndoicno7"
    )

    # Crear un cursor
    mycursor = mydb.cursor()


    #                                                       Agregar a un Usuario
    if opcion==1:
        sql = "INSERT INTO Usuarios (Nombre_usuario , Contrasena , correo_electronico , Numero_celular ) VALUES (%s, %s, %s, %s)"
        # Datos que deseas insertar
        numero_celular_alternativo="0000000"
        val = (usuario, contraseña, correo, numero_celular_alternativo)
        try:
            mycursor.execute(sql, val)
            # Confirmar los cambios
            mydb.commit()

            return 0

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return 1



            #                                                      Verificar el Inicio de Sesion
    if opcion==2:
        #   Intentar encontrar al usuario con nombre de usuario y contraseña
        mycursor.execute("SELECT * FROM Usuarios WHERE Nombre_usuario = %s AND Contrasena = %s", (usuario, contraseña))
        usuarios=mycursor.fetchall()

        if  len(usuarios) > 0:

            print("Usuario encontrado con nombre de usuario y contraseña")
            with open('Usuario.txt', 'w') as archivo:
                archivo.write(usuario)
            opcion_entrada = "3"
            with open('opcion_inicio_sesion.txt', 'w') as archivo:
                archivo.write(opcion_entrada)


            return 0

        #   Intentar encontrar al usuario con correo y contraseña
        mycursor.execute("SELECT * FROM Usuarios WHERE correo_electronico  = %s AND Contrasena = %s", (correo, contraseña))
        usuarios = mycursor.fetchall()
        if  len(usuarios) > 0:
            print("Usuario encontrado con correo y contraseña")

            with open('Usuario.txt', 'w') as archivo:
                archivo.write(usuario)
            opcion_entrada = "3"
            with open('opcion_inicio_sesion.txt', 'w') as archivo:
                archivo.write(opcion_entrada)


            return 0

        print("No he encontrado nada")
        return 1


    # Cerrar el cursor y la conexión
    mycursor.close()
    mydb.close()

