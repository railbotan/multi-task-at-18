# CPU-bound

Будет генерация 2 монет

### Замер скорости генерации на 1 ядре:

![с1](https://user-images.githubusercontent.com/93836720/145710521-fcbf678a-5549-41e7-a6ec-acf48ab3faae.jpg)

Время 58 секунд

Диспетчер задач:

![с1_д](https://user-images.githubusercontent.com/93836720/145710531-702aaf93-29e0-4486-90cb-e460e63724be.jpg)

### Замер скорости генерации на 2 ядрах:

![с2](https://user-images.githubusercontent.com/93836720/145710711-50a96a4a-609c-42a3-981f-baf829294ce2.jpg)

Время 46 секунд

Диспетчер задач:

![с2_д](https://user-images.githubusercontent.com/93836720/145710717-564f9e94-6b15-49fe-8935-62ea99ba0fbb.jpg)

### Замер скорости генерации на 4 ядрах:

![с3](https://user-images.githubusercontent.com/93836720/145710778-a21af641-ff95-4711-9bf7-0e65bb82187b.jpg)

Время 89 секунд

Диспетчер задач:

![с3_д](https://user-images.githubusercontent.com/93836720/145710786-c524c0ef-3fdd-4fc2-8b39-dce9ace8253e.jpg)

### Замер скорости генерации на 5 ядрах:

![с4](https://user-images.githubusercontent.com/93836720/145710829-15f26f24-004b-4618-a8a4-1cdfab0e38b5.jpg)

Время 94 секунды

Диспетчер задач:

![с4_д](https://user-images.githubusercontent.com/93836720/145710837-d13336ea-f3c8-464b-8b4f-20dbac7cdaad.jpg)

### Замер скорости генерации на 10 ядрах:

![с5](https://user-images.githubusercontent.com/93836720/145710986-f4dca5b6-4747-4efc-8265-367d95ba6b7d.jpg)

Время 57 секунд

Диспетчер задач:

![с5_д](https://user-images.githubusercontent.com/93836720/145710990-a75d72eb-a65d-44b6-81c1-c1f596ecd79b.jpg)

### Замер скорости генерации на 100 ядрах:

![с6](https://user-images.githubusercontent.com/93836720/145711062-9ccd6c33-7591-4666-9375-b36a20ecd5cf.jpg)


Запустить на 100 ядрах нельзя, т.к. максимально возможно 61.

При увеличении ядер от 1 до 4, загруженность на ЦП, памяти, диске растет. А после 4 заметны скачки, загруженность то увеличивается, то уменьшается.
Далее увеличивать бесполезно(после 4), т.к физически больших ядер не существует и значения будут рандомными. 
