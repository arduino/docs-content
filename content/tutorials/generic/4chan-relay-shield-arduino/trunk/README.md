# 4chan-relay-shield-arduino
How to interact with Ks0251 keyestudio 4-channel Relay Shield

## Sample Code
```
/*
  DANCE OFF

  By Randal Burger
  https://codelyfe.github.io

  HOW TO: 
  Ks0251 keyestudio 4-channel Relay Shield

  I believe they did not have the right
  sample to teach others. So I made this one.
  
*/
  int PINDa = 4;
  int PINCb = 5;
  int PINBc = 6;
  int PINAd = 7;

void setup() {
  pinMode(PINDa, OUTPUT); // 4th Relay
  pinMode(PINCb, OUTPUT); // 3rd Relay
  pinMode(PINBc, OUTPUT); // 2nd Relay
  pinMode(PINAd, OUTPUT); // 1st Relay
}

void loop() {
  // 4th Relay
  digitalWrite(PINDa, HIGH); //   
  delay(100); //                       
  digitalWrite(PINDa, LOW); //    
  delay(100); // 
  // 3rd Relay  
  digitalWrite(PINCb, HIGH); //   
  delay(200); //                       
  digitalWrite(PINCb, LOW); //    
  delay(200); // 
  // 2nd Relay
  digitalWrite(PINBc, HIGH); //   
  delay(300); //                       
  digitalWrite(PINBc, LOW); //    
  delay(300); // 
  // 1st Relay
  digitalWrite(PINAd, HIGH); //   
  delay(100); //                       
  digitalWrite(PINAd, LOW); //    
  delay(100); //                     
}
```
