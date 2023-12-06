const int Led_Board = PC13;
const int Led = PB9;
const int Analog = PA0;
int Analog_Read;
unsigned int Mapping;
void setup() {
  Serial.begin(115200);
  pinMode(Analog, INPUT_ANALOG);
  pinMode(Led_Board, OUTPUT);
  pinMode(Led, PWM);
}

void loop() {
  Analog_Read = analogRead(Analog);
  Mapping=map(Analog_Read,0,4095,0,65535);
  pwmWrite(Led, 1000);
  Serial.print(Analog_Read);
  Serial.print(" - ");
  Serial.print(Mapping);
  Serial.print("\n");  
}
