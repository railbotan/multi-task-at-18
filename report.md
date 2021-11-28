# Task-on-topic-No.-11-Multi
**my CPU: AMD A6-3410MX (4C/4T)*\
***В задании "CPU-bound" я уменьшил количество нулей в искомом md5-hash до 4, т.к. поиск 
на моем компьютере даже одного значения с 5-ю нулями слишком времязатратный*
____

## ThreadPoolExecutor

**Вывод**: от увеличения кол-ва воркеров увеличивались нагрузка на процессор, 
объём занимаемой оперативной памяти и нагрузка на сеть. Время работы сокращалось.

Время выполнения без использования ThreadPoolExecutor:

![woTPE](img_ThreadPoolExecutor/woTPE.png "woTPE.png")

Время выполнения с использованием ThreadPoolExecutor:

![tDefault](img_ThreadPoolExecutor/tDefault.png "tDefault.png")

ThreadPoolExecutor(max_workers=5):

![t5](img_ThreadPoolExecutor/t5.png "t5.png")

ThreadPoolExecutor(max_workers=10):

![t10](img_ThreadPoolExecutor/t10.png "t10.png")

ThreadPoolExecutor(max_workers=100):

![t100](img_ThreadPoolExecutor/t100.png "t100.png")


## ProcessPoolExecutor

**Вывод**: от установки большего кол-ва воркеров, чем ядер процессора, нагрузка на процессор никак не изменилась 
и время выполнения практически не изменялось; а при установке кол-ва воркеров меньше чем ядер процессора 
время выполнения увеличилось.

Поиск 30 md5-hash без использования ProcessPoolExecutor:

![woPPE](img_ProcessPoolExecutor/woPPE.png "woPPE.png")

Поиск 30 md5-hash с использованием ProcessPoolExecutor:

![Default](img_ProcessPoolExecutor/pDefault.png "pDefault.png")

ProcessPoolExecutor(max_workers=2):

![p2](img_ProcessPoolExecutor/p2.png "p2.png")

ProcessPoolExecutor(max_workers=10):

![p10](img_ProcessPoolExecutor/p10.png "p10.png")

ProcessPoolExecutor(max_workers=100):

![p100](img_ProcessPoolExecutor/p100.png "p100.png")

ProcessPoolExecutor(max_workers=61):

![p61](img_ProcessPoolExecutor/p61.png "p61.png")