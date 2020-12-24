# LobLib by BlackLightHack
# Released under GNU license

from datetime import date, datetime
from sys import exit
 
now = datetime.now()
logfilename = str(''.join((str("{}.{}.{}-{}.{}".format(now.day, now.month, now.year, now.hour, now.minute)), ".log")))
fdh = open(logfilename, "tw", encoding="utf-8") # открыть файл
 
 
def logTimeUpdate():
    now = datetime.now() # Получить текущее время и дату
    global logtime # глобальной
    logtime = str("[{}:{}:{}]: ".format(now.hour, now.minute, now.second)) # Задать переменную времени
 
 
def write(obj): 
    logTimeUpdate() # Обновляем время в логе
    tup = logtime, obj # [10:16:42]: Запущена программа(но это кортеж!)
    wrie = ''.join(tup) # переобразовываем из кортежа в string
    fdh.write(wrie) # Записать в файл
 
write("[INFO] Loglib is running")

if SystemExit:
    fdh.close()
