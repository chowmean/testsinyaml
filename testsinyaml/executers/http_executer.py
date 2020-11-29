import requests
class Executer:
    def __init__(self, test):
        if "url" not in test:
            raise Exception("Need URL")
        self.url = test['url']
        if "query_params" not in test:
            self.query_params = {}
        else:
            self.query_params = test['query_params']
        if "post_params" not in test:
            self.post_params = {}
        else:
            self.post_params = test['post_params']
        if "headers" not in test:
            self.headers = {}
        else:
            self.headers = test['headers']
        if "success_field" not in test:
            self.success_field = "status_code"
        else:
            self.success_field = test['success_field']
        if "success_value" not in test:
            self.success_value = [200]
        else:
            self.success_value = test['success_value']
        return None

    def execute(self):
        data = requests.get(self.url)
        print(data.status_code)
        if self.success_field == "status_code":
            if data.status_code in self.success_value:
                return True
            else:
                return False
        else:
            return False