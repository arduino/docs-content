const int Trigger = 2;
const int Echo = 3; 

void setup() {
 Serial.begin(9600);
 pinMode(Trigger, OUTPUT);
 pinMode(Echo, INPUT);
 digitalWrite(Trigger, LOW);
}

void loop()
{
 
long t; //Tiempo de regreso
 long d; //Distancia en centímetros
  
 digitalWrite(Trigger, HIGH);
 delayMicroseconds(10); //Se envía un pulso de 10us
 digitalWrite(Trigger, LOW);
 
 t = pulseIn(Echo, HIGH); 
 d = t/59; //Se obtiene la distancia en centímetros
 
 Serial.print("Distancia: ");
 Serial.print(d);
 Serial.print("cm");
 Serial.println();
 delay(100); //Hacemos una pausa de 100ms
}
