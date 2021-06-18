# send-gmail
Script sencillo para enviar correos desde gmail con python. 

Pre-requisitos:
* Si la cuenta de gmail tiene habilitada la doble autenticacion, previo a la utilizacion del script, se debe generar una contraseña de aplicacion.
  En la documentacion oficial de google, estan los pasos para lograr esto: https://support.google.com/mail/answer/185833?hl=es 
* La version de python utlizada es la 3 o superior. 

Instrucciones:
Se puede correr directamente sobre la consola. Consta de cuatro argumentos obligatorios:
-f: Indica el remitente del mail.
-t: indica el destinatario del mail.
-s: Asunto del mail.
-m: Corresponde al texto que va incrustado en el cuerpo del mail. 

Ejemplo de uso:

python sendgmail.py -f remitente@gmail.com -t destinatario@serverejemplo.com -s "test" -m "Cuerpo del correo"


