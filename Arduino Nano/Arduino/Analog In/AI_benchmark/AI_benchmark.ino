#define NUM_SAMPLES 10000
#define PIN A0

void setup() {
  Serial.begin(115200);
  float duration;
  unsigned long start_time;
  unsigned long stop_time;

  start_time = micros();
  
  int samples[NUM_SAMPLES];
  
  for (int ii = 0; ii < NUM_SAMPLES; ii++){
    samples[ii] = analogRead(PIN);
  }
  stop_time = micros();
  duration = (stop_time - start_time)/1000.0;

  Serial.print("Function Arduino Time = ");
  Serial.print((float)duration);
  Serial.println(" ms");
  Serial.flush();
  delay(1000);
}

void loop() {
  // put your main code here, to run repeatedly:

}
