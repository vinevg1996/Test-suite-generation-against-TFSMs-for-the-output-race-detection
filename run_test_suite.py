import subprocess
import shlex
import json
import requests 
import time
import sys

device1 = "of:0000000000000001"
device2 = "of:0000000000000002"
app = 666

pattern = ''' curl -u onos:rocks -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '''
url = ''' 'http://localhost:8181/onos/v1/flows?appId=666' '''


dummy_payload = """{
        "flows": [
        {
          "priority": 40000,
          "timeout": 0,
          "isPermanent": false,
          "deviceId": "of:0000000000000001",
          "treatment": {
            "instructions": [
              {
                "type": "OUTPUT",
                "port": "2"
              }
            ]
          },
          "selector": {
            "criteria": [
              {
                "type": "IN_PORT",
                "port": "1"
              },
              {
                "type": "ETH_SRC",
                "mac": "9a:d8:73:d8:90:6a"
              },
              {
                "type": "ETH_DST",
                "mac": "9a:d8:73:d8:90:6b"
              }
            ]
          }
        }
        ]
    }"""

class ONOS_interface:
    def __init__(self):
        self.flow_rules = list()
        return

    def run_curl_cmd(self, cmd):
        args = shlex.split(cmd)
        process = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        resp = json.loads(stdout.decode('utf-8'))
        return resp

    def delete_rules_from_flow_rules(self):
        delete_str = 'http://localhost:8181/onos/v1/flows/of%3A0000000000000001/'
        for flowId in self.flow_rules:
            delete_str_flowId = delete_str + flowId
            resp = requests.delete(delete_str_flowId, auth=('onos', 'rocks'))
            #print("resp =", resp)
        return

    def get_rules_from_flow_rules(self):
        get_str = 'http://localhost:8181/onos/v1/flows/of%3A0000000000000001/'
        for flowId in self.flow_rules:
            get_str_flowId = get_str + flowId
            resp = requests.get(get_str_flowId, auth=('onos', 'rocks'))
            #print("resp =", resp)
        return

    def create_payload_rule(self, priority, timeout):
        data = json.loads(dummy_payload)
        data["flows"][0]['priority'] = int(priority)
        data["flows"][0]['timeout'] = int(timeout)
        json_data_payload = json.dumps(data)
        return json_data_payload

    def run_test1(self):
        #(pf1,1.1),(pf2,2.9)
        time.sleep(1.1)
        resp1 = self.run_curl_cmd(self.cmd_dummy_payload1)
        time.sleep(2.9)
        resp2 = self.run_curl_cmd(self.cmd_dummy_payload2)
        return

    def run_test2(self):
        #(pf1,1.1),(pf2,1.1)
        time.sleep(1.1)
        resp1 = self.run_curl_cmd(self.cmd_dummy_payload2)
        time.sleep(1.1)
        resp2 = self.run_curl_cmd(self.cmd_dummy_payload1)
        return

    def run_test3(self):
        #(pf1,1.1),(pf1,9.9),(pf2,2.9)
        time.sleep(1.1)
        resp1 = self.run_curl_cmd(self.cmd_dummy_payload1)
        time.sleep(9.9)
        resp2 = self.run_curl_cmd(self.cmd_dummy_payload1)
        time.sleep(2.9)
        resp3 = self.run_curl_cmd(self.cmd_dummy_payload2)
        return

    def run_test4(self):
        #(pf1,1.1),(pf1,9.9),(pf1,1.1)
        time.sleep(1.1)
        resp1 = self.run_curl_cmd(self.cmd_dummy_payload1)
        time.sleep(9.9)
        resp2 = self.run_curl_cmd(self.cmd_dummy_payload2)
        time.sleep(1.1)
        resp3 = self.run_curl_cmd(self.cmd_dummy_payload1)
        return

    def run_test6(self):
        #(pf2,1.1),(pf2,9.9),(pf1,1.1)
        time.sleep(1.1)
        resp1 = self.run_curl_cmd(self.cmd_dummy_payload2)
        time.sleep(9.9)
        resp2 = self.run_curl_cmd(self.cmd_dummy_payload2)
        time.sleep(1.1)
        resp3 = self.run_curl_cmd(self.cmd_dummy_payload1)
        return

    def run_test7(self):
        #(pf2,1.1),(pf1,9.9),(pf2,2.9)
        time.sleep(1.1)
        resp1 = self.run_curl_cmd(self.cmd_dummy_payload2)
        time.sleep(9.9)
        resp2 = self.run_curl_cmd(self.cmd_dummy_payload1)
        time.sleep(2.9)
        resp3 = self.run_curl_cmd(self.cmd_dummy_payload2)
        return

    def run_test8(self):
        #(pf2,1.1),(pf1,1.9),(pf2,5.1)
        time.sleep(1.1)
        resp1 = self.run_curl_cmd(self.cmd_dummy_payload2)
        time.sleep(1.9)
        resp2 = self.run_curl_cmd(self.cmd_dummy_payload1)
        time.sleep(5.1)
        resp3 = self.run_curl_cmd(self.cmd_dummy_payload2)
        return

    def run_test9(self):
        #(pf1,1.1),(pf2,2.9),(pf1,9.9),(pf2,2.9)
        time.sleep(1.1)
        resp1 = self.run_curl_cmd(self.cmd_dummy_payload1)
        time.sleep(2.9)
        resp2 = self.run_curl_cmd(self.cmd_dummy_payload2)
        time.sleep(9.9)
        resp3 = self.run_curl_cmd(self.cmd_dummy_payload1)
        time.sleep(2.9)
        resp4 = self.run_curl_cmd(self.cmd_dummy_payload2)
        return

    def run_test10(self):
        #(pf2,1.1),(pf1,1.9),(pf2,9.9),(pf1,1.1)
        time.sleep(1.1)
        resp1 = self.run_curl_cmd(self.cmd_dummy_payload2)
        time.sleep(2.9)
        resp2 = self.run_curl_cmd(self.cmd_dummy_payload1)
        time.sleep(9.9)
        resp3 = self.run_curl_cmd(self.cmd_dummy_payload2)
        time.sleep(1.1)
        resp4 = self.run_curl_cmd(self.cmd_dummy_payload1)
        return

    def run_test11(self):
        #(pf1,1.1),(pf2,2.9),(pf1,4.9),(pf2,2.9)
        time.sleep(1.1)
        resp1 = self.run_curl_cmd(self.cmd_dummy_payload1)
        time.sleep(2.9)
        resp2 = self.run_curl_cmd(self.cmd_dummy_payload2)
        time.sleep(4.9)
        resp3 = self.run_curl_cmd(self.cmd_dummy_payload1)
        time.sleep(2.9)
        resp4 = self.run_curl_cmd(self.cmd_dummy_payload2)
        return

    def run_test_suite(self, test_num):
        self.json_data_payload1 = self.create_payload_rule(40001, 5)
        self.cmd_dummy_payload1 = pattern + ''' ' ''' + self.json_data_payload1 + ''' ' ''' + str(url)
        self.json_data_payload2 = self.create_payload_rule(40002, 2)
        self.cmd_dummy_payload2 = pattern + ''' ' ''' + self.json_data_payload2 + ''' ' ''' + str(url)
        if test_num == "test1":
            self.run_test1()
        elif test_num == "test2":
            self.run_test2()
        elif test_num == "test3":
            self.run_test3()
        elif test_num == "test4":
            self.run_test4()
        elif test_num == "test6":
            self.run_test6()
        elif test_num == "test7":
            self.run_test7()
        elif test_num == "test8":
            self.run_test8()
        elif test_num == "test9":
            self.run_test9()
        elif test_num == "test10":
            self.run_test10()
        elif test_num == "test11":
            self.run_test11()
        else:
            print("forgot a test suite")
        return

onos = ONOS_interface()
onos.run_test_suite(sys.argv[1])