# IO-bound

#### Замер времени синхронной проверки:

![](https://github.com/alyonafilyaeva/multi-task-at-18/blob/main/screens/1_run.jpg)

Время: примерно 1315 секунд

#### Замер времени для 5 потоков: 

![](https://github.com/alyonafilyaeva/multi-task-at-18/blob/main/screens/5_run.jpg)

Время: примерно 393 секунды

#### Замер времени для 10 потоков: 

![](https://github.com/alyonafilyaeva/multi-task-at-18/blob/main/screens/10_run.jpg)

Время: примерно 331 секунда

#### Замер времени для 100 потоков:

![](https://github.com/alyonafilyaeva/multi-task-at-18/blob/main/screens/100_run.jpg)

Время: прмерно 183 секунды

Можно сделать вывод, что с увеличением количества потоков, уменьшается время проверки ссылок, но при этом несильно увеличивается нагрузка на ЦП, заметно увеличивается нагрузка на память, диск.

# CPU-bound

Будем генерировать 3 монеты.

#### Замер скорости генерации на 1 ядре:

![](https://github.com/alyonafilyaeva/multi-task-at-18/blob/main/screens/1_process.jpg)

Время: примерно 105 секунд

#### Замер скорости генерации на 2 ядрах:

![](https://github.com/alyonafilyaeva/multi-task-at-18/blob/main/screens/2_process.jpg)

Время: 83 секунды

![](https://github.com/alyonafilyaeva/multi-task-at-18/blob/main/screens/2_process_dis.jpg)

Загруженность: ЦП-36%, память-86%, диск-10%

#### Замер скорости генерации на 4 ядрах:

![](https://github.com/alyonafilyaeva/multi-task-at-18/blob/main/screens/4_process.jpg)

Время: 43 секунды

![](https://github.com/alyonafilyaeva/multi-task-at-18/blob/main/screens/4_process_dis.jpg)

Загруженность: ЦП-50%, память-88%, диск-48%

#### Замер скорости генерации на 5 ядрах:

![](https://github.com/alyonafilyaeva/multi-task-at-18/blob/main/screens/5_process.jpg)

Время: 279 секунд

![](https://github.com/alyonafilyaeva/multi-task-at-18/blob/main/screens/5_process_dis.jpg)

Загруженность: ЦП-99%, память-89%, диск-4%


#### Замер скорости генерации на 10 ядрах:

![](https://github.com/alyonafilyaeva/multi-task-at-18/blob/main/screens/10_process.jpg)

Время: 62 секунды

![](https://github.com/alyonafilyaeva/multi-task-at-18/blob/main/screens/10_process_dis.jpg)

Загруженность: ЦП-84%, память-91%, диск-7%

#### Замер скорости генерации на 100 ядрах:

![](https://github.com/alyonafilyaeva/multi-task-at-18/blob/main/screens/100_process.jpg)

Запустить на 100 ядрах нельзя, так как максимальное возможное число 61.

Проведя анализ, можно заметить, что при увеличении ядер от 1 до 4, загруженность на ЦП, памяти, диске растет. А после 4 заметны скачки, загруженность то уменьшается, то увеличивается.

Можно сделать вывод, что в CPU-задаче увеличение количества ядер ускоряет выполнение до определенного числа ядер - в моем случае 4. Далее увеличение бесполезно, т.к физически больших ядер не существует и значения получаются рандомными. 
