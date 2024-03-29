#libreria de facebook
#instalar con pip install facebook-sdk
import facebook
import serial
import time
temporal =""
token_acceso = "EAADUTsiz24gBOZCCeu886TDZC2asyF5S00KRXd2vQtpXKvImZAgkF5pOi0b9QIVNzpXmZB6zy8SsOWwNCijoAq9i98mcrDUWfOLVc5LhIsseY4mZAjhDtIHTwWLZBZCWNpgVgDZBHB27ZAPdcGPbMIIYHp0ZAca6PEKigNvZBFzlW4y3KvJoje1alUZCe9vaC2TdSunmwIrRWu1fJCIIwZAJTfKrc0rZCd45QKbVwZD"
#conexion a la api de facebook
asfb = facebook.GraphAPI(access_token=token_acceso)

puerto_serial = serial.Serial('COM1', 9600) #puerto serial
time.sleep(2)

#bucle para recibir informacion constantemente
while True:
    #ultima publicacion del muro
    publicaciones = asfb.get_object("me/posts", fields="id,message,created_time", limit=1)
    if temporal != publicaciones["data"][0]["message"]:
        #si la galleta es diablo responde 1
        if (publicaciones["data"][0]["message"] == "diablo"):
            print(1)
            mensaje = "1"
            puerto_serial.write(mensaje.encode())
            puerto_serial.close()
        #si la galleta es mantequilla responde 2
        elif (publicaciones["data"][0]["message"] == "mantequilla"):
            print(2)
            mensaje = "2"
            puerto_serial.write(mensaje.encode())
            puerto_serial.close()
        #si la galleta es picnic responde 3
        elif (publicaciones["data"][0]["message"] == "picnic"):
            print(3)
            mensaje = "3"
            puerto_serial.write(mensaje.encode())
            puerto_serial.close()
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