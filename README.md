# 🛍️ Django Store - Каталог товаров

Проект представляет собой полнофункциональный каталог товаров с категориями, реализованный на Django с использованием PostgreSQL. Включает CRUD-операции, пагинацию, работу с изображениями и адаптивный интерфейс.

![Пример интерфейса](https://via.placeholder.com/800x400?text=Django+Store+Screenshot)

## 🌟 Особенности проекта

- **Полноценный каталог товаров** с категориями и изображениями
- **Пагинация** товаров на главной странице
- **Адаптивный дизайн** на Bootstrap 5
- **Защищенные формы** для добавления товаров
- **Поиск и фильтрация** в админ-панели
- **Система хранения** медиафайлов (изображения товаров)

## 🚀 Технологический стек

![Django](https://img.shields.io/badge/Django-092E20?logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?logo=bootstrap&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)

## 📂 Структура проекта

```bash
django_store/
├── .env                    # Конфигурационные переменные
├── .gitignore              # Игнорируемые файлы
├── requirements.txt        # Зависимости Python
├── manage.py               # Скрипт управления
│
├── django_store/           # Основные настройки
│   ├── settings.py         # Конфигурация проекта
│   ├── urls.py            # Главные маршруты
│   └── ...
│
├── catalog/                # Приложение каталога
│   ├── models.py          # Модели Product и Category
│   ├── views.py           # Контроллеры (главная, товар, добавление)
│   ├── forms.py           # Формы для товаров
│   ├── templates/         # Шаблоны
│   │   ├── base.html     # Базовый шаблон
│   │   ├── home.html     # Главная страница
│   │   └── product_detail.html # Страница товара
│   └── ...
│
└── media/                 # Медиафайлы
    └── products/          # Изображения товаров
⚙️ Установка и запуск
1. Клонирование репозитория
bash
git clone https://github.com/ваш-username/django_store.git
cd django_store
2. Настройка окружения
Создайте файл .env на основе примера:

bash
cp .env.example .env
Заполните его данными:

ini
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=your-secret-key
DEBUG=True
3. Установка зависимостей
bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
4. Настройка PostgreSQL
sql
CREATE DATABASE your_db_name;
CREATE USER your_db_user WITH PASSWORD 'your_db_password';
ALTER ROLE your_db_user SET client_encoding TO 'utf8';
GRANT ALL PRIVILEGES ON DATABASE your_db_name TO your_db_user;
5. Запуск проекта
bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
🌐 Доступные маршруты
Маршрут	Описание
/	Главная страница с товарами
/product/<int:pk>/	Страница товара
/add/	Форма добавления товара
/admin/	Админ-панель
🛠 Основные команды
Команда	Описание
python manage.py runserver	Запуск сервера
python manage.py makemigrations	Создание миграций
python manage.py migrate	Применение миграций
python manage.py createsuperuser	Создание админа
python manage.py shell	Django shell
📌 Дополнительные возможности
Добавление товаров через веб-интерфейс

Пагинация на главной странице

Валидация форм при добавлении товаров

Адаптивный дизайн для мобильных устройств

📝 Лицензия
MIT License. Смотрите файл LICENSE для подробностей.

<div align="center"> <sub>Создано с ❤️ для вашего проекта Django Store</sub> </div> ```