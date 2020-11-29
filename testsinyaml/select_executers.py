from testsinyaml.executers import *

executer_types_map = {
    "http": http_executer.Executer,
    "telnet": telnet_executer.Executer,
    "command": command_executer.Executer
}


def get_executer(type):
    return executer_types_map[type]