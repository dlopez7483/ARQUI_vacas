// Colocar los pines de salida y entrada
int TRIG = 10;
int ECO = 9;
int CTE = 58.2;
int DURACION;
int DISTANCIA;
String MSG = "PRODUCTO ENTREGADO";

void setup() {
  // put your setup code here, to run once:
  pinmode(TRIG, OUTPUT);
  pinmode(ECO, INPUT);
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(TRIG, HIGH);
  delay(1);
  digitalWrite(TRIG, LOW);
  // Envía el pulso para entener el retorno hasta el rebote
  DURACION = pulseIn(ECO, HIGH);
  // Distancia se divide en una constante que es 58.2 para obtener en cm
  DISTANCIA = DURACION / CTE;
  if (DISTANCIA < 19 && DISTANCIA >= 0){
    Serial.print(MSG);
    delay(200);
  }
}

void ultrasonico