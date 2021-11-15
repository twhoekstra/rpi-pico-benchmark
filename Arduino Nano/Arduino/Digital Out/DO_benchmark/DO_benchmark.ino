#define periods 100000
#define LED_PIN 13

void setup() {
  Serial.begin(115200);
  float duration;
  unsigned long start_time;
  unsigned long stop_time;

  pinMode(LED_BUILTIN, OUTPUT);

  start_time = micros();
  for (long ii = 0; ii < periods; ii++){
    digitalWrite(LED_BUILTIN, HIGH);
    digitalWrite(LED_BUILTIN, LOW);
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
