#include "DHT.h"

DHT dht(2,DHT11);
float h,t;
void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  h=dht.readHumidity();
  t=dht.readTemperature();

  if(isnan(h) || isnan(t))
    return;

  Serial.print("#"); // Start of Frame
  Serial.print("~"); // Seperator
  Serial.print(h);
  Serial.print("~"); // Seperator
  Serial.print(t);
  Serial.print("~");
  Serial.println("$"); // End of Frame
  delay(4000); // 4 seconds of delay
  
}
