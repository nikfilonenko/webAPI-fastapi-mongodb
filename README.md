<h1 align='center'> Web API sample with FastAPI and MongoDB </h1>

<img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white"/> <img src="https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white"/> <img src="https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white"/> 

-----

## 1. MongoDB

- Для работы с БД необходимо запустить одноразовый контейнер MongoDB с помощью docker:

```docker run --name mongo -dit -p 27017:27017 mongo:latest```

![image](https://github.com/nikfilonenko/webAPI-fastapi-mongodb/assets/103507130/0f16043f-aeab-4e16-b5d3-84daa93f7f88)

## 2. Запуск проекта Проект

- Необходимо установить все необходимые зависимости с помощью команды:

```pip install -r requirements.txt```

- После успешной установки модулей, следует запустить сервер `uvicorn` следующей командой:

```uvicorn src.main:app --reload```
