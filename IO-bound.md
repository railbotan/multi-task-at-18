# IO-bound
# Измерение времени синхронной проверки:
<img width="1280" alt="image" src="https://user-images.githubusercontent.com/73825639/146364602-678a1602-2d14-4c5c-8818-8f9a14454b09.png">
Время: 2015 секунд.

Диспетчер задач:

<img width="586" alt="image" src="https://user-images.githubusercontent.com/73825639/146372910-b785f881-c201-4a46-8329-e4d3db61b870.png">

# При 5-ти воркетах:
<img width="1280" alt="image" src="https://user-images.githubusercontent.com/73825639/146368913-ae5d5ed6-ca51-4e94-8cbe-d7f52b31ddf5.png">
Время: 531 секунда.

Диспетчер задач:

<img width="526" alt="image" src="https://user-images.githubusercontent.com/73825639/146371784-87379048-17e7-4294-af6e-70200fcd90a5.png">

# При 10-ти воркетах:
<img width="1280" alt="image" src="https://user-images.githubusercontent.com/73825639/146370789-0da4d142-9ff1-4db6-9040-16877bf441ce.png">
Время: 231 секунда.

Диспетчер задач:

<img width="585" alt="image" src="https://user-images.githubusercontent.com/73825639/146370752-5849732a-031c-48ff-81d5-85f2510b6c87.png">

# При 100 воркетах:
<img width="1280" alt="image" src="https://user-images.githubusercontent.com/73825639/146371615-28b1a516-29cd-4df2-a718-89fe54692726.png">
Время: 150 секунд.

Диспетчер задач:

<img width="586" alt="image" src="https://user-images.githubusercontent.com/73825639/146371352-d5349366-ba0c-4ce0-851a-10359233a177.png">

# Вывод:
Можно подвести итог исходя из полученных данных: с учеличением воркетов, время проверки уменьшается, 
загрузка памяти изменяется, при измерении времени синхронной проверки и при 5-ти воркетах значения процессора(цп) плюс-минус
одинаково, а при 10-воркетах и при 100-воркетах очень сильно возрастает.
