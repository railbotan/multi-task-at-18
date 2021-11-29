# IO-bound 
## Синхронная проверка ссылок:
### Время выполнения
![img.png](Screens/io_time1.png)
### Диспетчер задач
![img.png](Screens/io_tm1.png)
## Используя ThreadPoolExecutor:
## Воркер 5:
### Время
![img.png](Screens/io_time2.png)
### Диспетчер
![img.png](Screens/io_tm2.png)
## Воркер 10:
### Время
![img.png](Screens/io_time3.png)
### Диспетчер
![img.png](Screens/io_tm3.png)
## Воркер 100:
### Время 
![img.png](Screens/io_time4.png)
### Диспетчер
![img.png](Screens/io_tm4.png)
Загрузка памяти почти не отличается, загрузка ЦП совсем немного увеличивается. Но время выполнения существенно сокращается
# CPU-bound
Замер будет на поиске 5-и монет
## Скорость генерации на 1 ядре
### Время
![img.png](Screens/cpu_time1.png)
### Диспетчер
![img.png](Screens/cpu_tm1.png)
## Используя ProcessPoolExecutor:
## Воркер 2:
### Время
![img.png](Screens/cpu_time2.png)
### Диспетчер
![img.png](Screens/cpu_tm2.png)
## Воркер 4:
### Время
![img.png](Screens/cpu_time3.png)
### Диспетчер
![img.png](Screens/cpu_tm3.png)
## Воркер 5:
### Время
![img.png](Screens/cpu_time4.png)
### Диспетчер
![img.png](Screens/cpu_tm4.png)
## Воркер 10:
### Время
![img.png](Screens/cpu_time5.png)
### Диспетчер
![img.png](Screens/cpu_tm5.png)
## Воркер 100:
![img.png](Screens/cpu_time6.png)
Сильно меняется загрузка процессора, время выполнения уменьшается с увеличением количества воркеров. Максимальное количество воркеров - 61 из-за особенностей ОС. 