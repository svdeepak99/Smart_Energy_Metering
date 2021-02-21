float time0,prev_time,max_time=0,Dt=0,prev_maxtime=0,max_val,val;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(2000000);
  pinMode(A0,INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  prev_time=micros();
  max_val=0; val=201;
  while( (micros()-prev_time<10000) && val>100 )
  {
    time0=micros();
    val=analogRead(A0);
    if(val>max_val){
      max_val=val;
      max_time=time0;
    }
  }
  if(max_val>100){
    Dt=max_time-prev_maxtime;
    if(Dt < 22000 && Dt > 18000){
      Serial.print(max_val);Serial.print('\t');
      Serial.println(1000000/Dt);
    }
    prev_maxtime=max_time;
  }
  while(analogRead(A0) < 100)
    delayMicroseconds(100);
}
