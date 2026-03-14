from My_Bot import *

import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "main:app",          # main - назва файлу, app - об’єкт FastAPI
        host="0.0.0.0",      # слухати всі інтерфейси
        port=8000,           # порт, можна змінити
        reload=True          # автоматичний перезапуск при зміні коду
    )
