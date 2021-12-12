# IO-bound

### Замер времени синхронной проверки:

![1](https://user-images.githubusercontent.com/93836720/145708722-805536a4-1e0b-4c01-88dc-90c4fd5939e8.jpg)

Время 1494 секунд

Диспетчер задач:

![1_д](https://user-images.githubusercontent.com/93836720/145709809-9e028483-a0ee-4bca-bc00-c31e2eacf402.jpg)

###  При 5 воркерах:

![2](https://user-images.githubusercontent.com/93836720/145709469-b897f99e-2621-4562-a3f0-8199f781d75c.jpg)

Время 323 секунды

Диспетчер задач:

![2_д](https://user-images.githubusercontent.com/93836720/145709471-15a2125c-a8c0-4e84-99a3-28b241a1095f.jpg)

###  При 10 воркерах:

![3](https://user-images.githubusercontent.com/93836720/145709502-9afe5138-79da-4cf2-9286-b91f9ce6c670.jpg)

Время 185 секунд

Диспетчер задач:

![3_д](https://user-images.githubusercontent.com/93836720/145709511-081cab84-a3aa-444f-9bff-cc6ac4b18c5b.jpg)

###  При 10 воркерах:

![4](https://user-images.githubusercontent.com/93836720/145709822-121995eb-753f-4b1c-a25b-e098446ca2a8.jpg)

Время 35 секунд

Диспетчер задач:

![4_д](https://user-images.githubusercontent.com/93836720/145709835-f96575cd-0bc7-46cb-af12-9785cdb6fbc7.jpg)

Можно сделать вывод, что с увеличением количества воркеров, время проверки ссылок становится меньше, загрузка памяти почти не отличается, процессор(цп) в основном тоже одинаков, но бывают моменты когда скачок становится больше
