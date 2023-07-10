# sudo apt install jq

import os

# Запуск команды Bash
output = os.popen("curl -s https://ponomarev-aa.ru/test.json | jq .").read()

# Вывод результата
print(output)
