## IO-bound

### Выполнение  синхронно, в 1 поток:

время выполнения: 

<img src='https://github.com/NastyaBay/multi-task-at-18/blob/main/%D1%81%D0%BA%D1%80%D0%B8%D0%BD%D1%8B/io-bound(%D1%81%D0%B8%D0%BD%D1%85%D1%80%2C%20%D0%B2%D1%80%D0%B5%D0%BC%D1%8F).jpg'>

Диспечер задач:

<img src='https://github.com/NastyaBay/multi-task-at-18/blob/main/%D1%81%D0%BA%D1%80%D0%B8%D0%BD%D1%8B/io-bound(%D1%81%D0%B8%D0%BD%D1%85%D1%80%D0%BE%D0%BD%D0%BD%D1%8B%D0%B9).jpg'>


### Выполнение используя ThreadPoolExecutor:

### воркер = 5:

время выполнения: 

<img src='https://github.com/NastyaBay/multi-task-at-18/blob/main/скрины/io-b2(время).jpg'>

Диспечер задач:

<img src='https://github.com/NastyaBay/multi-task-at-18/blob/main/%D1%81%D0%BA%D1%80%D0%B8%D0%BD%D1%8B/io-b2(%D0%94%D0%B7).jpg'>

### воркер = 10:

время выполнения: 

<img src='https://github.com/NastyaBay/multi-task-at-18/blob/main/%D1%81%D0%BA%D1%80%D0%B8%D0%BD%D1%8B/io-b2(10%D0%B2%D1%80%D0%B5%D0%BC%D1%8F).jpg'>

Диспечер задач:

<img src='https://github.com/NastyaBay/multi-task-at-18/blob/main/%D1%81%D0%BA%D1%80%D0%B8%D0%BD%D1%8B/10.jpg'>
<img src='https://github.com/NastyaBay/multi-task-at-18/blob/main/%D1%81%D0%BA%D1%80%D0%B8%D0%BD%D1%8B/10(2).jpg'>

### воркер = 100:

время выполнения: 

<img src='https://github.com/NastyaBay/multi-task-at-18/blob/main/%D1%81%D0%BA%D1%80%D0%B8%D0%BD%D1%8B/io-b2(100%D0%B2%D1%80%D0%B5%D0%BC%D1%8F).jpg'>

Диспечер задач:

<img src='https://github.com/NastyaBay/multi-task-at-18/blob/main/%D1%81%D0%BA%D1%80%D0%B8%D0%BD%D1%8B/io-b2(100%D0%94%D0%B7).jpg'>


При преобразование время выполнения уменьшается, а загрузка памяти почти не отличается, процессор(цп) в основном тоже одинаков, но бывают моменты когда скачок и становится больше


##CPU-bound:

### Выполнение на 1 ядре:

время выполнения: 

<img src='https://github.com/NastyaBay/multi-task-at-18/blob/main/%D1%81%D0%BA%D1%80%D0%B8%D0%BD%D1%8B/cpu-b1(%D0%B2%D1%80%D0%B5%D0%BC%D1%8F).jpg'>

Диспечер задач:

<img src='https://github.com/NastyaBay/multi-task-at-18/blob/main/скрины/cpu-b1(дз).jpg'>

### Выполнение используя ProcessPoolExecutor:

### Воркаут = 2:

время выполнения: 

<img src='https://github.com/NastyaBay/multi-task-at-18/blob/main/%D1%81%D0%BA%D1%80%D0%B8%D0%BD%D1%8B/cpu-b2(%D0%B2%D1%80%D0%B5%D0%BC%D1%8F).jpg'>

Диспечер задач:

<img src='https://github.com/NastyaBay/multi-task-at-18/blob/main/%D1%81%D0%BA%D1%80%D0%B8%D0%BD%D1%8B/cpu-b2(%D0%94%D0%B7).jpg'>

### Воркаут = 4:

время выполнения: 

<img src='https://github.com/NastyaBay/multi-task-at-18/blob/main/%D1%81%D0%BA%D1%80%D0%B8%D0%BD%D1%8B/cpu-b4(%D0%B2%D1%80%D0%B5%D0%BC%D1%8F).jpg'>

Диспечер задач:

<img src='https://github.com/NastyaBay/multi-task-at-18/blob/main/%D1%81%D0%BA%D1%80%D0%B8%D0%BD%D1%8B/cpu-b4(%D0%B4%D0%B7).jpg'>

### Воркаут = 5:

время выполнения: 

<img src='https://github.com/NastyaBay/multi-task-at-18/blob/main/%D1%81%D0%BA%D1%80%D0%B8%D0%BD%D1%8B/cpu-b5(%D0%B2%D1%80%D0%B5%D0%BC%D1%8F).jpg'>

Диспечер задач:

<img src='https://github.com/NastyaBay/multi-task-at-18/blob/main/%D1%81%D0%BA%D1%80%D0%B8%D0%BD%D1%8B/cpu-b5(%D0%B4%D0%B7).jpg'>

### Воркаут = 10:

время выполнения: 

<img src='https://github.com/NastyaBay/multi-task-at-18/blob/main/%D1%81%D0%BA%D1%80%D0%B8%D0%BD%D1%8B/cpu-b10(%D0%B2%D1%80%D0%B5%D0%BC%D1%8F).jpg'>

Диспечер задач:

<img src='https://github.com/NastyaBay/multi-task-at-18/blob/main/%D1%81%D0%BA%D1%80%D0%B8%D0%BD%D1%8B/cpu-b10(%D0%B4%D0%B7).jpg'>

### Воркаут = 100:

<img src='https://github.com/NastyaBay/multi-task-at-18/blob/main/%D1%81%D0%BA%D1%80%D0%B8%D0%BD%D1%8B/cpu-b100.jpg'>

При увеличении с 2 на 4 воркаута увеличивается загруженость процессора(ЦП) до 100%, что означает что все(4) ядра заняты. При этом время уменьшается(быстрее проходит), после 4 и до 61 будет примерно одинаковые значения, которые уже рандомны(так как монеты формируем случайно(+ отбираем нужный)) воркаут = 100 не проходит(ошибка: возможно толкьо до 61)

