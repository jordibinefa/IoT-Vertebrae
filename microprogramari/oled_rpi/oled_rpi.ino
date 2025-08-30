
// https://es.aliexpress.com/item/1005006263058736.html
// https://github.com/olikraus/u8g2/wiki

#include <Wire.h>
#include <U8g2lib.h>

U8G2_SSD1306_128X64_NONAME_F_SW_I2C u8g2(U8G2_R0, 12, 14, U8X8_PIN_NONE);

void setup() {
  Serial.begin(115200);
  u8g2.begin();
}

void loop() {
  if (Serial.available() > 0) {
    String str = Serial.readString();
    str.trim();
    u8g2.clearBuffer();
    u8g2.setFont(u8g2_font_7x14B_tr);
    u8g2.drawStr(0, 10, str.c_str());
    u8g2.sendBuffer();
  }
  delay(1000);
}
