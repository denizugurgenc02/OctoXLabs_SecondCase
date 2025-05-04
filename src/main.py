import requests
import os

#Patch adresi ve headers alan bir üst sınıf oluşturuyorum.
class BaseRequestFactory:
    def __init__(self, path_address, headers):
        self.main_URL = os.getenv("main_URL", "https://httpbin.org/")
        self.path_address = path_address
        self.headers = headers

#get metodu için özel sınıf
class GetRequestFactory(BaseRequestFactory):
    def __init__(self, path_address, headers):
        super().__init__(path_address, headers)
        self.action()
    def action(self):
        response = requests.get(f"{self.main_URL}/{self.path_address}", headers=self.headers)#istenilen url ve path e bağlan get ile veriyi çek.
        print("Server Response:",response.status_code)#Sunucunun cevabını konsola yazar. bazı web sayfaları request isteğine cevap vermez örnek: sahibinden.com
        print(response.text)#Sunucunun cevabını console'a yazdır.

#post metodu için özel sınıf
class PostRequestFactory(BaseRequestFactory):
    def __init__(self, path_address, headers, data): #base sınıfa ek olarak data parametresi var.çünki post metodu sunucuya işlemesi için veri gönderir.
        super().__init__(path_address, headers)
        self.data = data
        self.action()
    def action(self):
        response = requests.post(f"{self.main_URL}/{self.path_address}", headers=self.headers, data=self.data)
        print("Server Response:",response.status_code)
        print(response.text)

#put metodu için özel sınıf
class PutRequestFactory(BaseRequestFactory):
    def __init__(self, path_address, headers, data):
        super().__init__(path_address, headers)
        self.data = data
        self.action()
    def action(self):
        response = requests.put(f"{self.main_URL}/{self.path_address}", headers=self.headers, data=self.data)
        print("Server Response:",response.status_code)
        print(response.text)

#delete metodu için öcel sınıf
class DeleteRequestFactory(BaseRequestFactory):
    def __init__(self, path_address, headers):
        super().__init__(path_address, headers)
        self.action()
    def action(self):
        response = requests.delete(f"{self.main_URL}/{self.path_address}", headers=self.headers)
        print("Server Response:",response.status_code)
        print(response.text)

#test ediyorum.
app = GetRequestFactory("/get", {"accept": "application/json"})