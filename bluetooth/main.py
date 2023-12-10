#libreria de facebook
#instalar con pip install facebook-sdk
import facebook
import serial
import time
temporal =""
token_acceso = "EAADUTsiz24gBO2SZBZAE9yxjRf93ZCVoHPpZBqPZCFYjc033H7L8HnbNiADOcwThWh31erKQUWoFy8UsIY4ZCq71aGivkwkZB31VgSXE2oDfl6GzwcjNA2D40LZA9H8NTZAZAClru2CYxQe7mkpd4vyoBKENlTahwM7J8Q1Pq2ZBYMGJ7iTmPLojEhnMvI5yBckCrEDgR7jc0nvDqn9hkTkneQT5uY5WxT5JEMZD"
#conexion a la api de facebook
asfb = facebook.GraphAPI(access_token=token_acceso)
cantidad_diablo=3
cantidad_mantequilla=3
cantidad_picnic=3
puerto_serial = serial.Serial('COM1', 9600) #puerto serial
time.sleep(2)

#bucle para recibir informacion constantemente
while True:
    #ultima publicacion del muro
    publicaciones = asfb.get_object("me/posts", fields="id,message,created_time", limit=1)
    if temporal != publicaciones["data"][0]["message"]:
        #si la galleta es diablo responde 1
        if (publicaciones["data"][0]["message"] == "diablo"):
            if (cantidad_diablo > 0):
             cantidad_diablo = cantidad_diablo - 1
             print(1)
             mensaje = "1"
             puerto_serial.write(mensaje.encode())
             puerto_serial.close()
            else:
             asfb.put_object(parent_object='me', connection_name='feed', message='No hay mas galletas diablo')
        #si la galleta es mantequilla responde 2
        elif (publicaciones["data"][0]["message"] == "mantequilla"):
            if cantidad_mantequilla > 0:
             cantidad_mantequilla = cantidad_mantequilla - 1
             print(2)
             mensaje = "2"
             puerto_serial.write(mensaje.encode())
             puerto_serial.close()
            else:
             asfb.put_object(parent_object='me', connection_name='feed', message='No hay mas galletas mantequilla')
        #si la galleta es picnic responde 3
        elif (publicaciones["data"][0]["message"] == "picnic"):
            if cantidad_picnic > 0:
             cantidad_picnic = cantidad_picnic - 1
             print(3)
             mensaje = "3"
             puerto_serial.write(mensaje.encode())
             puerto_serial.close()
            else:
             asfb.put_object(parent_object='me', connection_name='feed', message='No hay mas galletas picnic')
        #si no hay coincidencias imprime no hay coincidencias
        else:
            print("no hay coincidencias")
            mensaje = "no hay coincidencias"
            puerto_serial.write(mensaje.encode())
            puerto_serial.close()
        temporal = publicaciones["data"][0]["message"]
    else:
        #si no hay cambios solo imprime no hay cambios
        print("no hay cambios")
    #tiempo de espera para volver a ejecutar el bucle y no consumer mucha memoria del sistema
    time.sleep(8)