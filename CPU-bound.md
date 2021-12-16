# CPU-bound
Генерация 2-х монет.

# Замер скорости генерации на 1-ом ядре:
<img width="1280" alt="image" src="https://user-images.githubusercontent.com/73825639/146382511-cdf20a07-1dfc-4ad9-9a7a-8b28a860ba6a.png">

Время: 508 секунд.
Диспетчер задач:

<img width="584" alt="image" src="https://user-images.githubusercontent.com/73825639/146382439-e0507263-49ea-4fd2-b8bd-991b32d25261.png">

# Замер сторости генерации на 2-х ядрах:
<img width="1280" alt="image" src="https://user-images.githubusercontent.com/73825639/146384750-4f34c1d1-5c25-47c2-bd2c-532065f148b8.png">

Время: 311 секунд.
Диспетчер задач:

<img width="587" alt="image" src="https://user-images.githubusercontent.com/73825639/146384142-437f0aa0-25fb-4cab-81a4-d117dfd28456.png">

# Замер сторости генерации на 4-х ядрах:
<img width="1280" alt="image" src="https://user-images.githubusercontent.com/73825639/146385458-edb2cde3-d4b6-4181-bd97-b481e0c33fea.png">

Время: 127 секунд.
Диспетчер задач:

<img width="583" alt="image" src="https://user-images.githubusercontent.com/73825639/146385205-cd6e565c-0bf3-4a36-b436-00b5197729d6.png">

# Замер сторости генерации на 5-ти ядрах:
<img width="1280" alt="image" src="https://user-images.githubusercontent.com/73825639/146386318-ada85761-939e-43f2-9597-57a67daa4874.png">

Время: 141 секунда.
Диспетчер задач:

<img width="585" alt="image" src="https://user-images.githubusercontent.com/73825639/146385737-91befe67-2a0c-454b-a5e9-35ab3957462f.png">

# Замер сторости генерации на 10-х ядрах:
<img width="1280" alt="image" src="https://user-images.githubusercontent.com/73825639/146387523-cf9b2302-118d-411d-8196-96d92210d82a.png">

Время: 90 секунд.
Диспетчер задач:

<img width="584" alt="image" src="https://user-images.githubusercontent.com/73825639/146386766-e7317605-8a71-4566-aed3-c4773c137038.png">

# Замер сторости генерации на 100 ядрах:
<img width="1280" alt="image" src="https://user-images.githubusercontent.com/73825639/146387716-18e2db4a-3e19-4a6b-b697-bc854562028b.png">

Нельзя запустить на 100 ядрах, поскольку максимально возможно только 61.

# Вывод
При увеличении ядер от 1 до 4 - загруженность на ЦП возрастает, память и диск не изменятся, после 4-х ядер с 5 до 10 
заметен скачек, загруженность то увеличивается, то уменьшается. 

После 4-х увеличивать количество ядер бесполезно, ведь значения будут рандомными, потому что больше 4-х ядер не существует.


