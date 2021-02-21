float time0,prev_time,max_time=0,max_val,val;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(2000000);
  pinMode(A0,INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  prev_time=micros();
  max_val=0;
  while( (micros()-prev_time<10000) && analogRead(A0)>200 )
  {
    time0=micros();
    val=analogRead(A0);
    if(val>max_val){
      max_val=val;
      max_time=time0;
    }
  }
  if(max_val>200)
    Serial.println(max_val);
  while(analogRead(A0) < 200)
    delayMicroseconds(100);
}
