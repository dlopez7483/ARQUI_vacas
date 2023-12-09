int ledPin = 13;
int state = 0;

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
      {
        //galleta tipo 1 diablo
        state = 0;
      }
    case 2:
      {
        //galleta tipo 2 mantequilla
        state = 0;
      }
    case 3:
      {
        //galleta tipo 3 picnic
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
