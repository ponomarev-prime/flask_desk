import os

# Запуск команды Bash
output = os.popen("ls -l").read()

# Вывод результата
print(output)
