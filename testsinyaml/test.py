from testsinyaml.select_executers import get_executer
from testsinyaml.parser import Parser

def Execute(config):
    p=Parser(config=config)
    for test in p.get_tests():
        exc = get_executer(test["type"])(test)
        print(exc.execute())
