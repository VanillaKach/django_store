Django Store (Каталог товаров)
Проект представляет собой каталог товаров с категориями, реализованный на Django с использованием PostgreSQL.

📂 Структура проекта
bash
django_store/
├── .env                    # Конфигурационные переменные (БД, SECRET_KEY)
├── .gitignore              # Игнорируемые файлы
├── requirements.txt        # Зависимости Python
├── run.py                  # Главный скрипт для управления проектом
│
├── django_store/           # Основные настройки Django
│   ├── __init__.py
│   ├── settings.py         # Настройки проекта (БД, MEDIA, INSTALLED_APPS)
│   ├── urls.py            # Главные URL-маршруты
│   └── asgi.py            # ASGI-конфигурация (не используется)
│
├── catalog/               # Приложение "Каталог товаров"
│   ├── migrations/        # Миграции БД
│   ├── __init__.py
│   ├── admin.py           # Настройки админ-панели
│   ├── models.py          # Модели Product и Category
│   ├── views.py           # Логика страниц (главная)
│   └── templates/         # Шаблоны (опционально)
│       └── catalog/
│           └── home.html  # Шаблон главной страницы
│
└── media/                 # Загружаемые файлы (изображения товаров)
    └── products/
⚙️ Установка и запуск
1. Клонирование репозитория
bash
git clone https://github.com/ваш-username/django_store.git
cd django_store
2. Настройка окружения
Создайте файл .env в корне проекта:

bash
cp .env.example .env
Заполните его данными (пример в .env.example):

text
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=your-secret-key
DEBUG=True
3. Установка зависимостей
bash
python -m venv venv           # Создание виртуального окружения (опционально)
source venv/bin/activate      # Активация (Linux/macOS)
venv\Scripts\activate         # Активация (Windows)
pip install -r requirements.txt
4. Настройка PostgreSQL
Убедитесь, что PostgreSQL установлен и запущен.

Создайте БД и пользователя:

sql
CREATE DATABASE your_db_name;
CREATE USER your_db_user WITH PASSWORD 'your_db_password';
ALTER ROLE your_db_user SET client_encoding TO 'utf8';
GRANT ALL PRIVILEGES ON DATABASE your_db_name TO your_db_user;
5. Запуск проекта
bash
python run.py migrate          # Применение миграций
python run.py createsuperuser  # Создание админа
python run.py runserver        # Запуск сервера
🔹 После этого проект будет доступен по адресу: http://127.0.0.1:8000

🛠 Основные команды
Команда	Описание
python run.py runserver	Запуск сервера разработки
python run.py migrate	Применить миграции
python run.py makemigrations	Создать миграции
python run.py shell	Открыть Django shell (с ipython)
python run.py loaddata fixtures.json	Загрузить тестовые данные
🔧 Настройка админки
Перейдите в админ-панель: http://127.0.0.1:8000/admin

Войдите под суперпользователем (логин/пароль из createsuperuser).

Управляйте товарами и категориями через интерфейс.

📌 Особенности проекта
✅ PostgreSQL — вместо SQLite для продакшн-готовности.
✅ Медиафайлы — загрузка изображений товаров (/media/products/).
✅ Фильтрация в админке — поиск по названию и описанию товаров.
✅ .env — безопасное хранение секретных данных.

