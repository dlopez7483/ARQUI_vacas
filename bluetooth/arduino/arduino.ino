int ledPin = 13;
int state = 0;

int CountDiablo = 3;
int CountMantequilla = 3;
int CountPicnic = 3;

void setup() {
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);
  Serial.begin(9600);
}

void loop() {
  switch (state) {
    case 0:
      {
        if (Serial.available() > 0 && Serial.available() < 2) {
          state = Serial.read();
        }
        if (state >= 1 && state <= 3) {
          Serial.println("Numero aceptado");
        } else {
          Serial.println("Numero Invalido");
          state = 0;
        }
      }
    case 1:
      {//galleta tipo 1 diablo
        if (CountDiablo > 0){
          //codigo de servos
          CountDiablo--;
        }else{
          Serial.println("Galletas Diablo Agotadas");
        }
        state = 0;
      }
    case 2:
      {//galleta tipo 2 mantequilla
        if (CountMantequilla > 0){
          //codigo de servos
          CountMantequilla--;
        }else{
          Serial.println("Galletas Mantequilla Agotadas");
        }
        state = 0;
      }
    case 3:
      {//galleta tipo 3 picnic
        if (CountPicnic > 0){
          //codigo de servos
          CountPicnic--;
        }else{
          Serial.println("Galletas Picnic Agotadas");
        }
        state = 0;
      }
  }
}

/* if(Serial.available() > 0){
    state = Serial.read();
  } 

  if (state == '1') {
    digitalWrite(ledPin, HIGH);
    state = 0;
  }
*/
