void setup() {
  // put your setup code here, to run once:
  Serial.begin(2000000);
  pinMode(A0,INPUT);
  pinMode(A1,INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.print(analogRead(A0)); Serial.print('\t');
  Serial.println(analogRead(A1));
  delayMicroseconds(500);
}
