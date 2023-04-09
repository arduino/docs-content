// Lampjes schakelen met transistor en FET
int transistorPin = 12;
int fetPin = 11;

void setup() {
  // Configureer de pinmodes
  pinMode(transistorPin, OUTPUT);
  pinMode(fetPin, OUTPUT);
}

void loop() {
  // Schakel het FET-lampje aan
  digitalWrite(fetPin, HIGH);
  
  // Schakel het transistorlampje uit als het FET-lampje aan is, anders aan
  if(digitalRead(fetPin) == HIGH) {
    digitalWrite(transistorPin, LOW);
  } else {
    digitalWrite(transistorPin, HIGH);
  }
  
  delay(1000);

  // Schakel beide lampjes uit
  digitalWrite(transistorPin, LOW);
  digitalWrite(fetPin, LOW);
  delay(1000);
}
