# Добавить сумму транзакции, если add = True и среди продуктов есть "Хлеб"
# Должно выйти 172

transactions_homework = [
    {
        "add": True,
        "amount": 69,
        "products": [
            "Хлеб",
            "Масло",
            "Сок",
        ],
    },
    {
        "add": True,
        "amount": 30,
        "products": [
            "Сок",
        ],
    },
    {
        "add": True,
        "amount": 94,
        "products": [
            "Мука",
            "Хлеб",
            "Масло",
        ],
    },
    {
        "add": False,
        "amount": 24,
        "products": [
            "Конфеты",
            "Хлеб",
        ],
    },
    {
        "add": True,
        "amount": 9,
        "products": [
            "Хлеб",
            "Шоколад",
            "Гречка",
        ],
    },
    {
        "add": True,
        "amount": 91,
        "products": [
            "Апельсин",
            "Гречка",
        ],
    },
    {
        "add": True,
        "amount": 84,
        "products": [
            "Помидоры",
            "Сок",
        ],
    },
    {
        "add": False,
        "amount": 45,
        "products": [
            "Хлеб",
            "Гречка",
        ],
    },
    {
        "add": True,
        "amount": 9,
        "products": [
            "Лимон",
            "Сок",
        ],
    },
]

sum_amount = sum(
    [
        transaction.get("amount", 0)
        for transaction in transactions_homework
        if transaction.get("add", False) and "Хлеб" in transaction.get("products", [])
    ]
)

print(sum_amount)
