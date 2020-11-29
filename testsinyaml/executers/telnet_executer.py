from telnetlib import Telnet
class Executer:
    def __init__(self, test):
        if "host" in test:
            self.host = test['host']
        else:
            raise Exception("HOST needed")
        if "port" in test:
            self.port = test['port']
        else:
            raise Exception("port needed")
        if "success_value" not in test:
            self.success_value = [True]
        else:
            self.success_value = test['success_value']

    def execute(self):
        try:
            telnet = Telnet(host=self.host,port=self.port)
            return True
        except Exception as e:
            return False

