# Tests In Yaml [testsinyaml]

#### Define your test cases in yaml and they will get executed and result will be shared. 

### Usage:

```
from testinyaml import tests
tests.execute(tests.yaml)
```
How your tests.yaml should look like?

```
tests:
  - type: http
    url: https://www.google.com
    verification_field: status_code
    success_value:
      - 200

  - type: telnet
    host: 127.0.0.1
    port: 22
    sucess_value: connected

  - type: command
    command: echo Returned output
    success_value: Returned output
```

### Options: 

This tool curently support three kind of executers. Means you can write these three kind of tests. 
1. HTTP Executer: Test http requests. 
2. TELNET Executer: Test telnet. 
3. COMMAND Executer: Test shell commands on local. 
