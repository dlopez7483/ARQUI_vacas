#libreria de facebook
#instalar con pip install facebook-sdk
import facebook
import time
temporal =""
token_acceso = "EAADUTsiz24gBOxKRUUnxSowRwkefbsNqvszVgkah5U5nId3VOzNBzEjqPGvi3DOGeVORs0Cl9rvvUchlxE1kNkN6iSQ3Ksuf7fKm7DZCMkSgugZBFZB8GG0ci7xAZCSK155u2brca2fBWvxcpr6Eq8Xpn65FpkZAqR7i6hLAx7ZACz6f6XsYBtx2lFYeg8qiskeWeKVmo1JmQyfUjZAKjgkE0iqkZCaH89oZD"
#conexion a la api de facebook
asfb = facebook.GraphAPI(access_token=token_acceso)


cantidad_diablo=3
cantidad_mantequilla=3
cantidad_picnic=3


#bucle para recibir informacion constantemente

while True:
    #ultima publicacion del muro
    publicaciones = asfb.get_object("me/posts", fields="id,message,created_time", limit=1)
    if temporal != publicaciones["data"][0]["message"]:
        #si la galleta es diablo responde 1
        if (publicaciones["data"][0]["message"] == "diablo"):
            if cantidad_diablo > 0:
                print(1)
                cantidad_diablo = cantidad_diablo - 1
            else:
              asfb.put_object(parent_object='me', connection_name='feed', message='No hay mas galletas diablo')
        #si la galleta es mantequilla responde 2
        elif (publicaciones["data"][0]["message"] == "mantequilla"):
            if cantidad_mantequilla > 0:
                print(2)
                cantidad_mantequilla = cantidad_mantequilla - 1
            else:
              asfb.put_object(parent_object='me', connection_name='feed', message='No hay mas galletas mantequilla')
        #si la galleta es picnic responde 3
        elif (publicaciones["data"][0]["message"] == "picnic"):
            if cantidad_picnic > 0:
                print(3)
                cantidad_picnic = cantidad_picnic - 1
            else:
              asfb.put_object(parent_object='me', connection_name='feed', message='No hay mas galletas picnic')
        #si no hay coincidencias imprime no hay coincidencias
        else:
         print("no hay coincidencias")
            
        
        
        temporal = publicaciones["data"][0]["message"]
    else:
        #si no hay cambios solo imprime no hay cambios
        print("no hay cambios")
    #tiempo de espera para volver a ejecutar el bucle y no consumer mucha memoria del sistema
    time.sleep(8)