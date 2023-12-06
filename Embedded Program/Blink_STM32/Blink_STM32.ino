const int Led_Board = PC13;
void setup() {
  pinMode(Led_Board, OUTPUT);
}

void loop() {
  digitalWrite(Led_Board, LOW);
  delay(500);
  digitalWrite(Led_Board, HIGH);
   delay(500);
}
