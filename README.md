# Shevchenko course (backend+frontend)

## Chapters 

* [Frontend](#frontend)
    * [Lesson 1](#lesson-1-2022-06-02)
    * [Lesson 2](#lesson-2-2022-06-06)
* [Backend](#backend)
    * [Lesson 1](#lesson-1-2022-06-03)
    * [Lesson 2](#lesson-2-2022-06-07)
    
-----

## Frontend

### Lesson 1 (2022-06-02)

Изучение HTML, основные теги

Домашнее задание - создать страничку с биографией: ``/frontend/lesson1/bio.html``

Ссылки:

* [Запись урока на Youtube](https://youtu.be/mSeRyDT7L1Y)

* [Справочник по HTML тегам](https://html5book.ru/html-tags/)

* [Репозиторий Шевченко](https://github.com/shevchenko126/courses)

[^^^](#chapters)

### Lesson 2 (2022-06-06) [^](#chapters)

Изучение CSS

[^^^](#chapters)

## Backend

### Lesson 1 (2022-06-03)

Изучение типов данных.

Домашнее задание - из словаря `dict_homework` достать значение "GET ME"

Решение: `/backend/lesson1/get_me.py`


```python
dict_homework = {
    "key1": {
        "d": 44,
        "f": None,
        "s": {
            8: 44,
            9: None,
            10: {"mm": ["s", "GET ME", 7]},
        },
    },
    "key2": {
        "fff1": 44,
        "f": None,
    },
}

print(dict_homework["key1"]["s"][10]["mm"][1])
```

[^^^](#chapters)

### Lesson 2 (2022-06-07) 

Изучение циклов, условий, списков, словарей.

Домашнее задание: Из списка словарей `transactions_homework` найти сумму транзакций, если add = True и среди продуктов есть "Хлеб"
Должен получится ответ: 172

Решение: `/backend/lesson2/transactions.py`

[^^^](#chapters)
