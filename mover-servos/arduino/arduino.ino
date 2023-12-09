#include <Servo.h>

Servo servo1; 
Servo servo2; 
Servo servo3; 
int anguloInicial = 0;  // Angulo inicial del servo

int firstServoPin = 13;  //diablo
int secondServoPin = 12; //mantequilla
int thirdServoPin = 11; //picnic
int state = 0;

void setup() {
    servo1.attach(firstServoPin);
    servo2.attach(secondServoPin);
    servo3.attach(thirdServoPin);

    servo1.write(anguloInicial);
    servo2.write(anguloInicial);
    servo3.write(anguloInicial);

    Serial.begin(9600);
}
 
void loop() {

  if(Serial.available() > 0){
    state = Serial.read();
  } 

  //diablo
  if (state == '1') {
    servo1.write(180);
    state = 0;
  }
  //mantequilla
  else if (state == '2') {
    servo2.write(180);
    state = 0;
  }
  //picnic
  else if (state == '3') {
    servo3.write(180);
    state = 0;
  }

}