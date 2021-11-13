
import unittest
import requests

class Login(unittest.TestCase):
    def apiLogin(self):
        url = 'http://api.xiaoqishen.cn/member/external/parent/login'
        headers = {"Content-Type" : "application/json"}
        data = {"mobile":"15836473538","password":"123456"}
        result = requests.post(url=url,headers=headers,params=data)
        print(result.json())
        self.assertEqual(True,result.json()['success'])
        self.assertEqual(0,result.json()['code'])
        token =  result.json()['data']['token']
        print(token)



if __name__ == '__main__':
    Login().apiLogin()



