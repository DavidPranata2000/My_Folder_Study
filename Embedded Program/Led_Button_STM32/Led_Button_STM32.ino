const int Led_Board = PC13;
const int Button = PA0;
int Button_Read;
void setup() {
  Serial.begin(115200);
  pinMode(Button, INPUT_PULLUP);
  pinMode(Led_Board, OUTPUT);
}

void loop() {
  Button_Read = digitalRead(Button);
  if (Button_Read == 0) {
    digitalWrite(Led_Board, LOW);
  }
  else {
    digitalWrite(Led_Board, HIGH);
  }
  Serial.println(Button_Read);
}
