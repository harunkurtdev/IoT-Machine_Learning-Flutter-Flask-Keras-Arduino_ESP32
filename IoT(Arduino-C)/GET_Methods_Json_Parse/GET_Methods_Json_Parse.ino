//Wifi Kütüphanesi ve Http istek Kütüphanesi
#include<ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
//Json Kütüphanesi
#include<ArduinoJson.h>


StaticJsonBuffer<200> jsonBuffer;
//wifi ismi ve şifre
const char* ssid="TTNET_HUAWEI_9207";
const char* password ="80D75FD3A8";


void setup() {
  // put your setup code here, to run once:
  //serial haberleşme
  Serial.begin(115200);
  //wifi bağlantısı
  WiFi.begin(ssid,password);

  // wifi ye Bağlanıyor iken
  while(WiFi.status()!=WL_CONNECTED){
   
      delay(1000);
      Serial.println("Bağlanıyor...");
   }
  
  // eğer wifiye bağlanmış şse
   if(WiFi.status()==WL_CONNECTED){
    
    //http kütüphanesinden
    HTTPClient http;
    //ilgili url e istek at
    http.begin("http://jsonplaceholder.typicode.com/posts/1");
    //atılan istek kodu
    int httpCode=http.GET();
    //başarılı ise 
    if(httpCode==200){
          // içinde ki tüm değerleri string e ata
          String body=http.getString();
          Serial.println(body);
          //ve json objesine aktar parçalatmak için
          JsonObject& jsonparse=jsonBuffer.parseObject(body);
          
          //gelen json verisinde ki title keyinni title a ata
          const char* title= jsonparse["title"];
          //ve serial ekrana yazdır
          Serial.printf("VErimiz : %s",title);
          
      }
      //tüm işlemler sonrasında http isteğini kes
    http.end();
    }else{
      //herhangi bir hata olursa ekranda göster
      Serial.println("Bağlantı hatası");
      }

}

void loop() {
//sonsuz döngü

}
