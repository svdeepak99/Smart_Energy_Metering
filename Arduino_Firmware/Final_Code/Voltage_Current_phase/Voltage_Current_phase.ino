#include <SimpleKalmanFilter.h>
#include<math.h>

SimpleKalmanFilter pf_t(1,1,0.01),freq_t(20000,20000,0.01);

float time0,prev_time,max_time=0,Dt=0,prev_maxtime=0,max_val,val;
float i_val=0,time1,max_ival=0,max_itime=0,Dvi_t=0;
void setup() {
  // put your setup code here, to run once:
  delay(1000);
  Serial.begin(2000000);
  delay(1000);
  pinMode(A0,INPUT);
  pinMode(A1,INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  prev_time=micros();
  max_val=0; val=201;
  max_ival=0;
  while( (micros()-prev_time<17000)  )
  {
    delay(1);
    time0=micros();
    val=analogRead(A0);
    time1=micros();
    i_val=analogRead(A1);
    if(val>max_val){
      max_val=val;
      max_time=time0;
    }
    if(i_val>max_ival){
      max_ival=i_val;
      max_itime=time1;
    }
  }
  if(max_val>200){
    Dt=freq_t.updateEstimate(max_time-prev_maxtime);
    Dvi_t=pf_t.updateEstimate(max_time-max_itime);
    if(Dt < 22000 && Dt > 18000){
      Serial.print((max_val*0.0257)-1.292);Serial.print('\t');Serial.print((max_ival*332)/190);Serial.print('\t');Serial.print(1000000/Dt);Serial.print('\t');
      Serial.print(cos((2*3.14*Dvi_t)/Dt));Serial.println('\t');
    }
    prev_maxtime=max_time;
  }
  while(analogRead(A0) < 200)
    delayMicroseconds(100);       //wait until positive waveform arises again
}
