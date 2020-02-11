/*
bu örnek json parçalamak işlemi içindir
*/

// json kütüphanesi
#include<ArduinoJson.h>

  
  StaticJsonBuffer<200> jsonBuffer;
  //json verimiz
  char json[]="{adin:haurnlakodla,soyad:kurt,il:kocaeli}";
  void setup(){
    //seri haberleşme
  Serial.begin(115200);
  }


  void loop(){
    //json u parçalamak için
    JsonObject& jsonparse=jsonBuffer.parseObject(json);
    // her bir keyden verilerimizi alıyoruz
    const char* adin= jsonparse["adin"];
    const char* soyad= jsonparse["soyad"];
    const char* il= jsonparse["il"];
    // her birini ekrana basıyoruz
    Serial.println(adin);
    Serial.println(soyad);
    Serial.println(il);    

    delay(1000);
    }
