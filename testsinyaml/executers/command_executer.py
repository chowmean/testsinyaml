import os
class Executer:
    def __init__(self, test):
        if "command" in test:
            self.command = test['command']
        else:
            raise Exception("command needed")

        if "success_value" not in test:
            self.success_value = True
        else:
            self.success_value = test['success_value']

    def execute(self):
        try:
            stream = os.popen(self.command)
            output = stream.read()
            if output.strip() == self.success_value:
                return True
            return False
        except Exception as e:
            return False

