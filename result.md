# Pre-test info
#### Parsed wiki links count - 1561 ([here](res.txt))
#### CPU - 12 Core (24 Threads) 3.8GHz
#### RAM - 16 GB
#### Internet connection speed - 100 Mb/s
# IO-Bound
### Sync (1 thread)

> Task Manager
![](screenshots/io_1_task_manager.png)
Time (profiler) - 31.76 mins
![](screenshots/io_1_report.png)

### ThreadPoolExecutor
#### 5 workers

> Task Manager
![](screenshots/io_5_task_manager.png)
Time (profiler) - 6.81 mins
![](screenshots/io_5_report.png)

#### 10 workers

> Task Manager
![](screenshots/io_10_task_manager.png)
Time (profiler) - 3.37 mins
![](screenshots/io_10_report.png)

#### 100 workers

> Task Manager
![](screenshots/io_100_task_manager.png)
Time (profiler) - 1.5 min
![](screenshots/io_100_report.png)

### Conclusion

* Скорость выполнения IO-Bound задачи возрастает с увеличением количества потоков исполнения
* На больших количествах потоков, скорость выполнения может возрастать нелинейно

# CPU-Bound
Number of required coins: 4
### 1 Core

> Task Manager
![](screenshots/cpu_1_task_manager.png)
Time (profiler) - 3.67 mins
![](screenshots/cpu_1_report.png)

### ProcessPoolExecutor
#### 2 workers

> Task Manager
![](screenshots/cpu_2_task_manager.png)
Time (profiler) - 0.7 min (42.23 sec)
![](screenshots/cpu_2_report.png)

#### 4 workers

> Task Manager
![](screenshots/cpu_4_task_manager.png)
Time (profiler) - 0.85 min (51 sec)
![](screenshots/cpu_4_report.png)

#### 5 workers

> Task Manager
![](screenshots/cpu_5_task_manager.png)
Time (profiler) - 0.66 min (39.6 sec)
![](screenshots/cpu_5_report.png)

#### 10 workers

>Task Manager
![](screenshots/cpu_10_task_manager.png)
Time (profiler) - 1.5 min (89 sec)
![](screenshots/cpu_10_report.png)

- Время сильно увеличилось из-за долгого нахождения одного койна (просто не везло)

#### 100 workers

> ![](screenshots/cpu_100_error.png)

### Conclusion
* Скорость выполнения CPU-Bound задач не возрастает за счёт увеличения количества ядер
