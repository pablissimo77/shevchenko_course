# Shevchenko course (backend+frontend)


[backend lesson 1](#lesson-1-2022-06-03)


## Frontend

### Lesson 1 (2022-06-02)

Изучение HTML, основные теги

Домашнее задание - создать страничку с биографией: ``/frontend/lesson1/bio.html``

Ссылки:

* [Запись урока на Youtube](https://youtu.be/mSeRyDT7L1Y)

* [Справочник по HTML тегам](https://html5book.ru/html-tags/)

* [Репозиторий Шевченко](https://github.com/shevchenko126/courses)

## Backend

### Lesson 1 (2022-06-03)

Из словаря `dict_homework` достать значение "GET ME"

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
```

Решение:

`/backend/lesson1/get_me.py`

```python
print(dict_homework["key1"]["s"][10]["mm"][1])
```
