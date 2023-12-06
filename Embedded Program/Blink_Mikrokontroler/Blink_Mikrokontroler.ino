bool COM;
unsigned long WaktuSekarang, Interval = 0;
void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  WaktuSekarang = millis();
  if (WaktuSekarang - 500 < Interval) {
    COM = 1;
    digitalWrite(LED_BUILTIN, HIGH);
  } else if (WaktuSekarang - 1000 < Interval) {
    COM = 0;
    digitalWrite(LED_BUILTIN, LOW);
  } else {
    Interval = WaktuSekarang;
  }
  Serial.print("Waktu Millis : ");
  Serial.print(WaktuSekarang);
  Serial.print(" Kondisi LED : ");
  Serial.print(COM);
  Serial.print("\n");
}
