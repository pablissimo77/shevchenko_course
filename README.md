# Shevchenko course (backend+frontend)

## Chapters 

* [Frontend](#frontend)
    * [Lesson 1](#lesson-1-2022-06-02)
    * [Lesson 2](#lesson-2-2022-06-06)
    * [Lesson 3](#lesson-3-2022-06-09)
    * [Lesson 4](#lesson-4-2022-06-13)
    * [Lesson 5](#lesson-5-2022-06-17)
    * [Lesson 6](#lesson-6-2022-06-20)
    * [Lesson 7](#lesson-7-2022-06-23)

* [Backend](#backend)
    * [Lesson 1](#lesson-1-2022-06-03)
    * [Lesson 2](#lesson-2-2022-06-07)
    * [Lesson 3](#lesson-3-2022-06-10)
    * [Lesson 4](#lesson-4-2022-06-14)
    * [Lesson 5](#lesson-5-2022-06-18)
    * [Lesson 6](#lesson-6-2022-06-21)
    * [Lesson 7](#lesson-7-2022-06-24)



-----

## Frontend

-----

### Lesson 1 (2022-06-02)

Изучение HTML, основные теги

Домашнее задание - создать страничку с биографией: ``/frontend/lesson1/bio.html``

Ссылки:

* [Запись урока на Youtube](https://youtu.be/mSeRyDT7L1Y)
* [Справочник по HTML тегам](https://html5book.ru/html-tags/)
* [Репозиторий Шевченко](https://github.com/shevchenko126/courses)


-----

<iframe width="560" height="315" src="https://www.youtube.com/embed/mSeRyDT7L1Y" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

-----

[<img src="https://img.youtube.com/vi/mSeRyDT7L1Y/maxresdefault.jpg" width="50%">](https://youtu.be/mSeRyDT7L1Y)

-----

https://youtu.be/mSeRyDT7L1Y

-----


[^^^](#chapters)

-----

### Lesson 2 (2022-06-06)

Изучение CSS

Ссылки:

* [Запись урока на Youtube](https://youtu.be/v9dPnaUiOHo)


[^^^](#chapters)

-----

### Lesson 3 (2022-06-09)

Изучение HTML5, CSS3

Ссылки:

* [Запись урока на Youtube](https://youtu.be/ROhP_E4VuNE)
* [Сайт для проверки браузеров](http://caniuse.com/)


[^^^](#chapters)

-----

### Lesson 4 (2022-06-13)

Изучение pseudo-elements, HTML5, CSS3

Ссылки:

* [Запись урока на Youtube](https://youtu.be/QYKa0ZOs_-c)

### Lesson 5 (2022-06-17)

Изучение адаптивности и бутстрапа

Ссылки:

* [Запись урока на Youtube](https://youtu.be/Mm1VizI-oos)
* [Документація з бутстрапу](https://getbootstrap.com/docs/5.0/getting-started/introduction/)

[^^^](#chapters)

-----

### Lesson 6 (2022-06-20)

Верстаємо і встановлюємо react

Ссылки:

* [Запись урока на Youtube](https://youtu.be/uf84ss-9bho)

[^^^](#chapters)

-----

### Lesson 7 (2022-06-23)

Починаємо розбирати react

Ссылки:

* [Запись урока на Youtube](https://youtu.be/HtdP22Hw2U4)

[^^^](#chapters)

-----



## Backend

-----

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

Ссылки:

* [Запись урока на Youtube](https://youtu.be/H1lgOQ1ojhU)

[^^^](#chapters)

-----

### Lesson 2 (2022-06-07) 

Изучение циклов, условий, списков, словарей.

Домашнее задание: Из списка словарей `transactions_homework` найти сумму транзакций, если add = True и среди продуктов есть "Хлеб"
Должен получится ответ: `172`

Решение: `/backend/lesson2/transactions.py`

```python
transactions_homework = {...}

sum_amount = sum(
    [
        transaction.get("amount", 0)
        for transaction in transactions_homework
        if transaction.get("add", False) and "Хлеб" in transaction.get("products", [])
    ]
)

print(sum_amount)
```

Ссылки:

* [Запись урока на Youtube](https://youtu.be/_4lrmg4zoOo)

[^^^](#chapters)

-----

### Lesson 3 (2022-06-10) 

Изучение функции, пакеты и virtual environment

Домашнее задание: создать virtual environment

Ссылки:

* [Запись урока на Youtube](https://youtu.be/d8mlbtXg930)
* [Документация по Virtual Environment](https://docs.python.org/3/tutorial/venv.html)


[^^^](#chapters)

-----

### Lesson 4 (2022-06-14) 

Изучение функции, пакеты и virtual environment

Домашнее задание: создать virtual environment

Ссылки:

* [Запись урока на Youtube](https://youtu.be/3HnNeqjtb48)
* [PEP8 на pythonworld](https://pythonworld.ru/osnovy/pep-8-rukovodstvo-po-napisaniyu-koda-na-python.html)
* [PEP8 Официальная документация](https://peps.python.org/pep-0008/)


[^^^](#chapters)

-----

### Lesson 5 (2022-06-18) 

Изучение моделей в Django

Ссылки:

* [Запись урока на Youtube](https://youtu.be/ZTagiWzGB2Q)

[^^^](#chapters)

-----

### Lesson 6 (2022-06-21) 

Вчимо запити і роботу з моделями Django

Ссылки:

* [Запись урока на Youtube](https://youtu.be/8tmCBLpnU5M)

[^^^](#chapters)

-----

### Lesson 7 (2022-06-24) 

Продовжуємо вчити Django

**ДЗ по бекенду:** Зробити модель `Subject` - предмет. З групи зробити **ForeignKey** до нього.
Потім зробити окремий урл `/courses/subject/`, за яким, будуть видаватися всі предмети
І зробити окремий урл `/courses/subject/<id>/`, за яким, будуть видаватися імена всіх студентів, які записані в групи, які слухають цей предмет (за id)
Дедлайн - понеділок вечір

Ссылки:

* [Запись урока на Youtube](https://youtu.be/m3PP3DWU7Z0)

[^^^](#chapters)

-----

