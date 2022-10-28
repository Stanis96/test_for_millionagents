
  <h3 align="center"> Тестовое задание: "MillionAgents"</h3>

### Содержание:
1. ```task_practice\task_1.py``` - Секция 1. Практическое задание Python 1.1;
2. ```task_shorter\.py``` - Секция 1. 1.2 Короткие ссылки;
3.```task_2sql\task_2.2.sql``` - Секция 2. Практическое задание SQL/PostgreSQL 2.2;


### Используемый стек технологий в тестовом задании:
* poetry
* FastAPI
* SQLAlchemy
* uvicorn
* environ

### Перед запуском выполните:

* Виртуальное окружение:
  ```sh
  poetry config virtualenvs.in-project true
  poetry install
  ```

* В корне проекта создайте ```.env``` и задайте значения переменных:
    ```sh
    ENV=
    URL=
    DB=
    ```
* Для запуска задания 1.2, Вам потребуется перейти в директорию ```\task_shorter``` и прописать в терминале:
    ```sh
    uvicorn shorter.main:app --reload
    ```


