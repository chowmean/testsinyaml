import yaml
class Parser:
    def __init__(self,config):
        self.config_file=config

    def get_tests(self):
        with open(self.config_file,'r') as file:
            data=file.read()
            data=yaml.load(data)
        for test in data['tests']:
            yield test
