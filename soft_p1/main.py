#libreria de facebook
#instalar con pip install facebook-sdk
import facebook
import time
temporal =""
token_acceso = "EAADUTsiz24gBO1yRFWskwoFVkC7nkhUc4pzaJMAjjC1BEsmfGyTwmZB9J8DgAljO7tfXTqXGi6AmZBaJUZCTP1LNszfhsm9ZCntxlAcFdoF1uUSWIAxYLwsYp6fJJnqC4f6KJc2OS0cCYOFNISIR3JnyJfSI8TZCIOzaPFz7jAHRyJOVmQbid9TGlwzfJIPCcWFIv5fHrfyZATqY9oXjvxZCgfQOM1jlaAZD"
#conexion a la api de facebook
asfb = facebook.GraphAPI(access_token=token_acceso)





#bucle para recibir informacion constantemente

while True:
    #ultima publicacion del muro
    publicaciones = asfb.get_object("me/posts", fields="id,message,created_time", limit=1)
    if temporal != publicaciones["data"][0]["message"]:
        #si la galleta es diablo responde 1
        if (publicaciones["data"][0]["message"] == "diablo"):
            print(1)
        #si la galleta es mantequilla responde 2
        elif (publicaciones["data"][0]["message"] == "mantequilla"):
            print(2)
        #si la galleta es picnic responde 3
        elif (publicaciones["data"][0]["message"] == "picnic"):
            print(3)
        #si no hay coincidencias imprime no hay coincidencias
        else:
         print("no hay coincidencias")
            
        
        
        temporal = publicaciones["data"][0]["message"]
    else:
        #si no hay cambios solo imprime no hay cambios
        print("no hay cambios")
    #tiempo de espera para volver a ejecutar el bucle y no consumer mucha memoria del sistema
    time.sleep(8)