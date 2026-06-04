#include <Adafruit_NeoPixel.h>

#define PIN 7
#define NUM_LEDS 60
Adafruit_NeoPixel strip(NUM_LEDS, PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  analogReference(INTERNAL);
  Serial.begin(115200);
  strip.begin();
  strip.show();
}

void loop() {
  float voltage = analogRead(A0) * (1.1 / 1023.0);
  int ledsOn = map(voltage * 1000, 0, 110, 1, NUM_LEDS);
  int red = map(voltage * 1000, 0, 110, 0, 255);
  int green = 255 - red;
  strip.clear();
  for (int i = 0; i < ledsOn; i++) {
    strip.setPixelColor(i, strip.Color(red, green, 0));
  }
  strip.show();
  Serial.println(voltage, 5);
  delay(50);
}
