//json verisi olusturmak iöçinü

//json kütüphanesi
#include<ArduinoJson.h>

  StaticJsonBuffer<200> jsonBuffer;
  
void setup() {
  // put your setup code here, to run once:
  //seri haberleşme
  Serial.begin(115200);

  // json objesi oluşturma kütüphanesi
  JsonObject& jsoncreate=jsonBuffer.createObject();

  //keyi adin ve soyad olan bir json olustur
  jsoncreate["adin"]="harunlakodla";
  jsoncreate["soyad"]="Kurt";

  //data altında bir array olusturmak istersek
  JsonArray& data =jsoncreate.createNestedArray("data");

  data.add(44);
  data.add("Merhaba Nasılsın");

  
  //jsoncreate.printTo(Serial);
  // json verisini serial ekranda basmak istersek
  jsoncreate.prettyPrintTo(Serial);

}

void loop() {
  // put your main code here, to run repeatedly:

}
