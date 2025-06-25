# **МАҢЫЗДЫ: СТУДЕНТТЕРГЕ АРНАЛҒАН ТАПСЫРМАЛАР!**

Дағдыларды бекітуге арналған практикалық тапсырмалар. Қателерден қорықпа, бұл оқу процесінің бір бөлігі!

---

# **Жоба 4/10: Сілтеме қысқартқыш**

URL-ды қысқартуға арналған қарапайым веб-қосымша. Бұл жоба FastAPI-де HTTP-редиректтерді өңдеуді және Python сөздігін "кілт-мәнді" дерекқор ретінде пайдалануды көрсетеді.

---

**🚀 Технологиялар**

* **Бэкенд**: FastAPI
* **Фронтенд**: Next.js, React, Axios
* **Негізгі концепция**: Перенаправлениелерді орындау үшін FastAPI-дегі `RedirectResponse`.

**✨ Функционал**

* Ұзын URL-ды қабылдайды және қысқа URL-ды қайтарады.
* Қысқа URL бойынша өткенде, бастапқы адресқа қайта бағыттайды.
* Нәтижені алмасу буферіне көшіру батырмасы.

# **Сенің міндетің:**

## Сенің тапсырмаң:

# 1. **Кастомды қысқа сілтемелер:**
> * ## **Бэкенд**: `/api/shorten` эндпоинтін өзгерт, ол пайдаланушыдан қажетті қысқа кодты опционалды түрде қабылдай алатын болсын. Егер код бос емес болса, қате қайтар.
> * ## **Фронтенд**: Кастомды қысқа кодты енгізу үшін міндетті емес өріс қос.

# 2. **Басуларды санау:**
> * ## **Бэкенд**: `url_db` құрылымын өзгерт. `{"short": "long"}` орнына `{"short": {"long_url": "...", "clicks": 0}}` пайдалан. Әр редирект кезінде `clicks` санауышын арттыр.
> * ## **Фронтенд**: Қысқа сілтеме жасалғаннан кейін басулар саны туралы ақпаратты көрсет (бастапқыда 0).

# 3. **Сілтемелердің жарамдылық мерзімі (күрделі):**
> * ## **Бэкенд**: Сілтемені жасау кезінде онымен бірге жасалған уақыт белгісін қос. Редирект кезінде жасалған сәттен бастап N күннен артық уақыт өтпегенін тексер. Егер өтсе — 404 қатесін қайтар.

---

# **IMPORTANT: TASKS FOR STUDENTS!**

These are practical assignments to consolidate your skills. Don't be afraid of mistakes; they are part of the learning process!

---

# **Project 4/10: URL Shortener**

A simple web application for shortening URLs. This project demonstrates how to handle HTTP redirects in FastAPI and use a Python dictionary as a quick key-value database.

---

**🚀 Technologies**

* **Backend**: FastAPI
* **Frontend**: Next.js, React, Axios
* **Key Concept**: `RedirectResponse` in FastAPI for performing redirects.

**✨ Functionality**

* Accepts a long URL and returns a short one.
* Redirects to the original address when navigating to the short URL.
* Button to copy the result to the clipboard.

# **Your Task:**

## Your Mission:

# 1. **Custom Short Links:**
> * ## **Backend**: Modify the `/api/shorten` endpoint to optionally accept a desired short code from the user. If the code is already taken, return an error.
> * ## **Frontend**: Add an optional field for entering a custom short code.

# 2. **Click Counting:**
> * ## **Backend**: Change the structure of `url_db`. Instead of `{"short": "long"}`, use `{"short": {"long_url": "...", "clicks": 0}}`. Increment the `clicks` counter on each redirect.
> * ## **Frontend**: After creating a short link, display information about the number of clicks (initially 0).

# 3. **Link Expiration (Advanced):**
> * ## **Backend**: When creating a link, add a `created_at` timestamp with it. On redirect, check if more than N days have passed since creation. If so, return a 404 error.

---

# **ВАЖНО: ЗАДАЧИ ДЛЯ СТУДЕНТОВ!**

Перед тобой практические задания для закрепления навыков. Не бойся ошибок, это часть обучения!

---

# **Проект 4/10: Сокращатель Ссылок**

Простое веб-приложение для сокращения URL. Этот проект демонстрирует, как обрабатывать HTTP-редиректы в FastAPI и использовать словарь Python в качестве быстрой базы данных "ключ-значение".

---

**🚀 Технологии**

* **Бэкенд**: FastAPI
* **Фронтенд**: Next.js, React, Axios
* **Ключевая концепция**: `RedirectResponse` в FastAPI для выполнения перенаправлений.

**✨ Функционал**

* Принимает длинный URL и возвращает короткий.
* При переходе по короткому URL перенаправляет на исходный адрес.
* Кнопка для копирования результата в буфер обмена.

# **Твоя задача:**

## Твоя миссия:

# 1. **Кастомные короткие ссылки:**
> * ## **Бэкенд**: Измени эндпоинт `/api/shorten`, чтобы он мог опционально принимать желаемый короткий код от пользователя. Если код уже занят, возвращай ошибку.
> * ## **Фронтенд**: Добавь необязательное поле для ввода кастомного короткого кода.

# 2. **Подсчет кликов:**
> * ## **Бэкенд**: Измени структуру `url_db`. Вместо `{"short": "long"}` используй `{"short": {"long_url": "...", "clicks": 0}}`. При каждом редиректе увеличивай счетчик `clicks`.
> * ## **Фронтенд**: После создания короткой ссылки отображай информацию о количестве кликов (изначально 0).

# 3. **Срок действия ссылок (сложное):**
> * ## **Бэкенд**: При создании ссылки добавляй временную метку `created_at`. При редиректе проверяй, не прошло ли с момента создания больше N дней. Если прошло — возвращай ошибку 404.

# Next.js және FastAPI орнату: Жылдам бастау нұсқаулығы

**НАЗАР АУДАРЫҢЫЗ\! Осы жобаны іске қосу үшін қазір бірден ЕКІ БӨЛЕК ТЕРМИНАЛ (пәрмен жолы) ТЕРЕЗЕСІН ашуыңыз керек\!**

**Екі терминалды ашыңыз және әрқайсысы үшін төмендегі нұсқауларды орындаңыз.**

-----

## Терминал №1: FRONT-END (Next.js) іске қосу

1.  **Front-end қалтасына өту:**

    ```bash
    cd frontend
    ```

2.  **JavaScript тәуелділіктерін орнату (БІР РЕТ немесе жобаны жаңартқанда орындаңыз):**

    ```bash
    pnpm install
    ```

3.  **Front-end серверін іске қосу:**

    ```bash
    pnpm dev
    ```

      * **Егер `pnpm dev` "next танылмады" деген қате берсе**, мына пәрменді қолданыңыз:
        ```bash
        .\node_modules\.bin\next dev --turbopack
        ```
      * **Бұл терминалды жаппаңыз.** Front-end онда жұмыс істеуін жалғастырады.

-----

## Терминал №2: BACK-END (FastAPI) іске қосу

1.  **Back-end қалтасына өту:**

    ```bash
    cd backend
    ```

2.  **Python ортасын орнату (БІР РЕТ немесе жобаны жаңартқанда орындаңыз):**

    -----

    **МАҢЫЗДЫ PYTHON НҰСҚАСЫ ТУРАЛЫ ЕСКЕРТУ:**

      * **Егер Python нұсқасы сәйкес келсе**, жай ғана бар `venv` (3-қадам) белсендіріңіз және тәуелділіктерді орнатыңыз (`pip install -r requirements.txt`). Егер `venv` жобада бұрыннан бар болса, оны көшіру қажет емес.
      * **Егер Python нұсқасы әртүрлі болса**, міндетті түрде жаңа `venv` жасаңыз: `python -m venv venv`. Содан кейін оны белсендіріңіз және тәуелділіктерді орнатыңыз.
      * `venv` Python-ның нақты нұсқасына байланысты. `python --version` арқылы тексеріңіз.

    -----

      * **Виртуалды ортаны жасау (Python venv, Conda емес):**
        ```bash
        python -m venv venv
        ```
      * **Ортаны белсендіру:**
          * **Windows үшін (PowerShell):**
            ```bash
            .\venv\Scripts\activate
            ```
          * **macOS / Linux үшін (Bash/Zsh):**
            ```bash
            source venv/bin/activate
            ```
      * **`requirements.txt` файлынан Python тәуелділіктерін орнату:**
        ```bash
        pip install -r requirements.txt
        ```
        [cite\_start]`aiofiles` [cite: 1, 2] [cite\_start]және `httpx` [cite: 4] орнатылғанына көз жеткізіңіз.
      * **Ортаны белсенділігін тоқтату (орнатқаннан кейін):**
        ```bash
        deactivate
        ```

3.  **Виртуалды ортаны белсендіру (әр серверді іске қоспас бұрын):**

      * **Windows үшін (PowerShell):**
        ```bash
        .\venv\Scripts\activate
        ```
      * **macOS / Linux үшін (Bash/Zsh):**
        ```bash
        source venv/bin/activate
        ```

4.  **FastAPI Back-end серверін іске қосу:**

    ```bash
    fastapi dev main.py
    ```

      * **Бұл терминалды жаппаңыз.** Back-end онда жұмыс істеуін жалғастырады. API құжаттамасы: `http://127.0.0.1:8000/docs`.

-----

**Екі терминал да өз серверлерінің іске қосылғанын көрсеткеннен кейін, веб-шолғышты ашып, мына мекенжайға өтіңіз:**

**`http://localhost:3000`**

**Дәл осы жерде сіз жобаның жұмыс істеп тұрған Front-end бөлігін көресіз.**

-----

# Setting Up Next.js and FastAPI: A Quick Start Guide

**ATTENTION\! To run this project, you need to open TWO SEPARATE TERMINAL (command prompt) WINDOWS RIGHT NOW\!**

**Open two terminals and follow the instructions below for each one.**

-----

## Terminal №1: Starting the FRONT-END (Next.js)

1.  **Navigate to the Front-end folder:**

    ```bash
    cd frontend
    ```

2.  **Install JavaScript dependencies (perform ONCE, or when updating the project):**

    ```bash
    pnpm install
    ```

3.  **Start the Front-end server:**

    ```bash
    pnpm dev
    ```

      * **If `pnpm dev` throws an "next is not recognized" error**, use this command:
        ```bash
        .\node_modules\.bin\next dev --turbopack
        ```
      * **Do not close this terminal.** The Front-end will continue to run in it.

-----

## Terminal №2: Starting the BACK-END (FastAPI)

1.  **Navigate to the Back-end folder:**

    ```bash
    cd backend
    ```

2.  **Set up the Python environment (perform ONCE, or when updating the project):**

    -----

    **IMPORTANT PYTHON VERSION WARNING:**

      * **If your Python version matches**, simply activate the existing `venv` (step 3) and install dependencies (`pip install -r requirements.txt`). Copying `venv` is not needed if it's already in the project.
      * **If your Python version differs**, you **must** create a new `venv`: `python -m venv venv`. Then activate it and install dependencies.
      * `venv` is tied to a specific Python version. Check `python --version`.

    -----

      * **Create a virtual environment (Python venv, not Conda):**
        ```bash
        python -m venv venv
        ```
      * **Activate the environment:**
          * **For Windows (PowerShell):**
            ```bash
            .\venv\Scripts\activate
            ```
          * **For macOS / Linux (Bash/Zsh):**
            ```bash
            source venv/bin/activate
            ```
      * **Install Python dependencies from `requirements.txt`:**
        ```bash
        pip install -r requirements.txt
        ```
        [cite\_start]Ensure that `aiofiles` [cite: 1, 2] [cite\_start]and `httpx` [cite: 4] are installed.
      * **Deactivate the environment (after installation):**
        ```bash
        deactivate
        ```

3.  **Activate the virtual environment (before each server start):**

      * **For Windows (PowerShell):**
        ```bash
        .\venv\Scripts\activate
        ```
      * **For macOS / Linux (Bash/Zsh):**
        ```bash
        source venv/bin/activate
        ```

4.  **Start the FastAPI Back-end server:**

    ```bash
    fastapi dev main.py
    ```

      * **Do not close this terminal.** The Back-end will continue to run in it. API Documentation: `http://127.0.0.1:8000/docs`.

-----

**Once both terminals show their servers are running, open your web browser and navigate to:**

**`http://localhost:3000`**

**This is where you will see the running Front-end of the project.**

-----

# Настройка Next.js и FastAPI: Руководство по быстрому старту

**ВНИМАНИЕ\! Для запуска проекта тебе нужно открыть ДВА ОТДЕЛЬНЫХ ОКНА ТЕРМИНАЛА (командной строки) ПРЯМО СЕЙЧАС\!**

**Открой два терминала и следуй инструкциям ниже для каждого из них.**

-----

## Терминал №1: Запуск FRONT-END (Next.js)

1.  **Переход в папку Front-end:**

    ```bash
    cd frontend
    ```

2.  **Установка JavaScript-зависимостей (выполнить ОДИН РАЗ, или при обновлении проекта):**

    ```bash
    pnpm install
    ```

3.  **Запуск Front-end сервера:**

    ```bash
    pnpm dev
    ```

      * **Если `pnpm dev` выдает ошибку "next не распознан"**, используй эту команду:
        ```bash
        .\node_modules\.bin\next dev --turbopack
        ```
      * **Не закрывай этот терминал.** Front-end будет продолжать работать в нем.

-----

## Терминал №2: Запуск BACK-END (FastAPI)

1.  **Переход в папку Back-end:**

    ```bash
    cd backend
    ```

2.  **Настройка Python-окружения (выполнить ОДИН РАЗ, или при обновлении проекта):**

    -----

    **ВАЖНОЕ ПРЕДУПРЕЖДЕНИЕ О ВЕРСИЯХ PYTHON:**

      * **Если версия Python совпадает**, просто активируй существующее `venv` (шаг 3) и установи зависимости (`pip install -r requirements.txt`). Копирование `venv` не требуется, если оно уже в проекте.
      * **Если версия Python отличается**, **обязательно** создай новое `venv`: `python -m venv venv`. Затем активируй его и установи зависимости.
      * `venv` привязан к конкретной версии Python. Проверяй `python --version`.

    -----

      * **Создание виртуального окружения (Python venv, не Conda):**
        ```bash
        python -m venv venv
        ```
      * **Активация окружения:**
          * **Для Windows (PowerShell):**
            ```bash
            .\venv\Scripts\activate
            ```
          * **Для macOS / Linux (Bash/Zsh):**
            ```bash
            source venv/bin/activate
            ```
      * **Установка Python-зависимостей из `requirements.txt`:**
        ```bash
        pip install -r requirements.txt
        ```
        [cite\_start]Убедись, что `aiofiles` [cite: 1, 2] [cite\_start]и `httpx` [cite: 4] установлены.
      * **Деактивация окружения (после установки):**
        ```bash
        deactivate
        ```

3.  **Активация виртуального окружения (перед каждым запуском сервера):**

      * **Для Windows (PowerShell):**
        ```bash
        .\venv\Scripts\activate
        ```
      * **Для macOS / Linux (Bash/Zsh):**
        ```bash
        source venv/bin/activate
        ```

4.  **Запуск Back-end сервера FastAPI:**

    ```bash
    fastapi dev main.py
    ```

      * **Не закрывай этот терминал.** Back-end будет продолжать работать в нем. Документация API: `http://127.0.0.1:8000/docs`.

-----

**Как только оба терминала покажут, что их серверы запущены, открой веб-браузер и перейди по адресу:**

**`http://localhost:3000`**

**Именно здесь ты увидишь работающий Front-end проекта.**

# Проект 4/10: Сокращатель Ссылок

Простое веб-приложение для сокращения URL. Этот проект демонстрирует, как обрабатывать HTTP-редиректы в FastAPI и использовать словарь Python в качестве быстрой базы данных "ключ-значение".

## 🚀 Технологии

* **Бэкенд:** FastAPI
* **Фронтенд:** Next.js, React, Axios
* **Ключевая концепция:** `RedirectResponse` в FastAPI для выполнения перенаправлений.

## ✨ Функционал

* Принимает длинный URL и возвращает короткий.
* При переходе по короткому URL перенаправляет на исходный адрес.
* Кнопка для копирования результата в буфер обмена.

## 🎓 Задание для студентов

### Ваша миссия:

1.  **Кастомные короткие ссылки:**
    * **Бэкенд:** Измените эндпоинт `/api/shorten`, чтобы он мог опционально принимать желаемый короткий код от пользователя. Если код уже занят, возвращайте ошибку.
    * **Фронтенд:** Добавьте необязательное поле для ввода кастомного короткого кода.

2.  **Подсчет кликов:**
    * **Бэкенд:** Измените структуру `url_db`. Вместо `{"short": "long"}` используйте `{"short": {"long_url": "...", "clicks": 0}}`. При каждом редиректе увеличивайте счетчик `clicks`.
    * **Фронтенд:** После создания короткой ссылки отображайте информацию о количестве кликов (изначально 0).

3.  **Срок действия ссылок (сложное):**
    * **Бэкенд:** При создании ссылки добавляйте временную метку `created_at`. При редиректе проверяйте, не прошло ли с момента создания больше N дней. Если прошло — возвращайте ошибку 404.

## ⚙️ Локальный запуск

1.  Клонируйте репозиторий.
2.  **Бэкенд:** в папке `backend` выполните `pip install "fastapi[all]"` и `uvicorn main:app --reload`.
3.  **Фронтенд:** в папке `frontend` выполните `pnpm install` и `pnpm dev`.
