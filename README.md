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

[![Watch the video](https://img.youtube.com/vi/mSeRyDT7L1Y/maxresdefault.jpg)](https://youtu.be/mSeRyDT7L1Y)

[download video](https://github.com/pablissimo77/shevchenko_course/raw/main/frontend/videos/Online%20Фронт%20від%20Shevchenkod%20-%20Frontend%20заняття%201-mSeRyDT7L1Y)

Изучение HTML, основные теги

Домашнее задание - создать страничку с биографией: ``/frontend/lesson1/bio.html``

Ссылки:

* [Справочник по HTML тегам](https://html5book.ru/html-tags/)
* [Репозиторий Шевченко](https://github.com/shevchenko126/courses)

[^^^](#chapters)

-----

### Lesson 2 (2022-06-06)

[![Watch the video](https://img.youtube.com/vi/v9dPnaUiOHo/maxresdefault.jpg)](https://youtu.be/v9dPnaUiOHo)

[download video](https://github.com/pablissimo77/shevchenko_course/raw/main/frontend/videos/Online%20Фронт%20від%20Shevchenkod%20-%20Frontend%20заняття%202-v9dPnaUiOHo.mp4)

Изучение CSS

[^^^](#chapters)

-----

### Lesson 3 (2022-06-09)

[![Watch the video](https://img.youtube.com/vi/ROhP_E4VuNE/maxresdefault.jpg)](https://youtu.be/ROhP_E4VuNE)

Изучение HTML5, CSS3

Ссылки:

* [Сайт для проверки браузеров](http://caniuse.com/)


[^^^](#chapters)

-----

### Lesson 4 (2022-06-13)

[![Watch the video](https://img.youtube.com/vi/QYKa0ZOs_-c/maxresdefault.jpg)](https://youtu.be/QYKa0ZOs_-c)

Изучение pseudo-elements, HTML5, CSS3

### Lesson 5 (2022-06-17)

[![Watch the video](https://img.youtube.com/vi/Mm1VizI-oos/maxresdefault.jpg)](https://youtu.be/Mm1VizI-oos)

Изучение адаптивности и бутстрапа

Ссылки:

* [Документація з бутстрапу](https://getbootstrap.com/docs/5.0/getting-started/introduction/)

[^^^](#chapters)

-----

### Lesson 6 (2022-06-20)

[![Watch the video](https://img.youtube.com/vi/uf84ss-9bho/maxresdefault.jpg)](https://youtu.be/uf84ss-9bho)

Верстаємо і встановлюємо react

[^^^](#chapters)

-----

### Lesson 7 (2022-06-23)

[![Watch the video](https://img.youtube.com/vi/HtdP22Hw2U4/maxresdefault.jpg)](https://youtu.be/HtdP22Hw2U4)

Починаємо розбирати react


[^^^](#chapters)

-----

### Lesson 8 (2022-06-27)

[![Watch the video](https://img.youtube.com/vi/TJGNvstVPHQ/maxresdefault.jpg)](https://youtu.be/TJGNvstVPHQ)

Вивчамо props і state в react

[^^^](#chapters)

-----

### Lesson 9 (2022-06-30)

[![Watch the video](https://img.youtube.com/vi/VVG6mCWoMMo/maxresdefault.jpg)](https://youtu.be/VVG6mCWoMMo)

Вчимо react useEffect і map


[^^^](#chapters)

-----

### Lesson 10 (2022-07-04)

[![Watch the video](https://img.youtube.com/vi/EnEh_7VRG8o/maxresdefault.jpg)](https://youtu.be/EnEh_7VRG8o)

Вчимо fetch


[^^^](#chapters)

-----


## Backend

-----

### Lesson 1 (2022-06-03)

[![Watch the video](https://img.youtube.com/vi/H1lgOQ1ojhU/maxresdefault.jpg)](https://youtu.be/H1lgOQ1ojhU)

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

-----

### Lesson 2 (2022-06-07) 

[![Watch the video](https://img.youtube.com/vi/_4lrmg4zoOo/maxresdefault.jpg)](https://youtu.be/_4lrmg4zoOo)

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

[^^^](#chapters)

-----

### Lesson 3 (2022-06-10) 

[![Watch the video](https://img.youtube.com/vi/d8mlbtXg930/maxresdefault.jpg)](https://youtu.be/d8mlbtXg930)

Изучение функции, пакеты и virtual environment

Домашнее задание: создать virtual environment

Ссылки:

* [Документация по Virtual Environment](https://docs.python.org/3/tutorial/venv.html)


[^^^](#chapters)

-----

### Lesson 4 (2022-06-14) 

[![Watch the video](https://img.youtube.com/vi/3HnNeqjtb48/maxresdefault.jpg)](https://youtu.be/3HnNeqjtb48)

Изучение функции, пакеты и virtual environment

Домашнее задание: создать virtual environment

Ссылки:

* [PEP8 на pythonworld](https://pythonworld.ru/osnovy/pep-8-rukovodstvo-po-napisaniyu-koda-na-python.html)
* [PEP8 Официальная документация](https://peps.python.org/pep-0008/)


[^^^](#chapters)

-----

### Lesson 5 (2022-06-18) 

[![Watch the video](https://img.youtube.com/vi/ZTagiWzGB2Q/maxresdefault.jpg)](https://youtu.be/ZTagiWzGB2Q)

Изучение моделей в Django

[^^^](#chapters)

-----

### Lesson 6 (2022-06-21) 

[![Watch the video](https://img.youtube.com/vi/8tmCBLpnU5M/maxresdefault.jpg)](https://youtu.be/8tmCBLpnU5M)

Вчимо запити і роботу з моделями Django

[^^^](#chapters)

-----

### Lesson 7 (2022-06-24) 

[![Watch the video](https://img.youtube.com/vi/m3PP3DWU7Z0/maxresdefault.jpg)](https://youtu.be/m3PP3DWU7Z0)

Продовжуємо вчити Django

**ДЗ по бекенду:** Зробити модель `Subject` - предмет. З групи зробити **ForeignKey** до нього.
Потім зробити окремий урл `/courses/subject/`, за яким, будуть видаватися всі предмети
І зробити окремий урл `/courses/subject/<id>/`, за яким, будуть видаватися імена всіх студентів, які записані в групи, які слухають цей предмет (за id)
Дедлайн - понеділок вечір

[^^^](#chapters)

-----

### Lesson 8 (2022-06-28) 

[![Watch the video](https://img.youtube.com/vi/WG512WgCJ2I/maxresdefault.jpg)](https://youtu.be/WG512WgCJ2I)

Продовжуємо вчити Django
Users and decorators

[^^^](#chapters)

-----

### Lesson 9 (2022-07-01) 

[![Watch the video](https://img.youtube.com/vi/VtxvgQVfW0k/maxresdefault.jpg)](https://youtu.be/VtxvgQVfW0k)

Продовжуємо вчити Django та підключаємо вже Django Rest Framework

[^^^](#chapters)

-----

### Lesson 10 (2022-06-21) 

[![Watch the video](https://img.youtube.com/vi/0_ToHGVN-b8/maxresdefault.jpg)](https://youtu.be/0_ToHGVN-b8)

Вчимо серіалайзери і токени

[^^^](#chapters)

-----
