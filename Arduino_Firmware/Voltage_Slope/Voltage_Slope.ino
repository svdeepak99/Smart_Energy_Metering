float t0=0,t1=0,val=0,prev_val=0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(2000000);
  pinMode(A0,INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  t1=millis();
  val=analogRead(A0);
  Serial.println((val-prev_val)/(t1-t0));
  prev_val=val;
  t0=t1;
  //delayMicroseconds(500);
}
