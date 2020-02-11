
#include<ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

const char* ssid="TTNET_HUAWEI_9207";
const char* password ="80D75FD3A8";

void setup() {

  Serial.begin(115200);
  WiFi.begin(ssid,password);

  while(WiFi.status()!=WL_CONNECTED){
   
      delay(1000);
      Serial.println("Bağlanıyor...");
   }

}

void loop() {

  if(WiFi.status()==WL_CONNECTED){
     Serial.println("İçerideyiz");
    HTTPClient http;
  
      http.begin("http://jsonplaceholder.typicode.com/posts/1");
      int httpCode=http.GET();
      
     Serial.println(httpCode);
      if(httpCode>0){
          String body=http.getString();
          Serial.println(body);
        }
    
   http.end();
   }
   delay(3000);


}
