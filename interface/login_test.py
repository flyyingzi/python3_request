import unittest
import requests
import os, sys, json
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db_fixture import test_data


class AddEventTest(unittest.TestCase):
    ''' 添加发布会 '''

    def setUp(self):
        self.base_url = "http://192.168.1.9:18081/login"

    def tearDown(self):
        # print(self.result)
        pass
    def test_add_event_all_null(self):
        ''' 所有参数为空 '''
        header = {"Content-Type": "application/x-www-form-urlencoded","Accept": 'application/json',"X-Appkey":"web_merchant"}
        payload = {'login_name':'18264609967','password':'123456'}
        r = requests.post(self.base_url, headers = header,data=payload, )
        self.result = r.json()
        # self.result2 = json.dumps(self.result.json(),sort_keys=True)
        print(self.result)
        self.assertEqual(self.result['code'], '0')
        

    


if __name__ == '__main__':
    test_data.init_data() # 初始化接口测试数据
    unittest.main()
