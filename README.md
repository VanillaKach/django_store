# 🛍️ Django Store - Интернет-магазин с блогом
https://screenshots/shell_commands/screen_00.png

Полнофункциональный интернет-магазин с системой пользователей, блогом и кешированием на Django + Redis.

## 🌟 Основные возможности
Каталог товаров с категориями и фильтрацией

Блог с публикациями и комментариями

Система пользователей с ролями (админ, модератор, контент-менеджер)

Кеширование страниц через Redis

Модерация контента (товаров и постов блога)

Адаптивный дизайн на Bootstrap 5

## 🚀 Технологический стек
```
https://img.shields.io/badge/Django-092E20?logo=django&logoColor=white
https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=white
https://img.shields.io/badge/Redis-DC382D?logo=redis&logoColor=white
https://img.shields.io/badge/Bootstrap-7952B3?logo=bootstrap&logoColor=white
```


## 📂 Структура проекта

```
django_store/
├── blog/               # Приложение блога
├── catalog/            # Приложение каталога товаров
│   ├── fixtures/       # Тестовые данные
│   ├── management/     # Кастомные команды
│   ├── templates/      # Шаблоны
│   ├── services.py     # Бизнес-логика
├── users/              # Приложение пользователей
├── django_store/       # Настройки проекта
├── media/              # Загружаемые файлы
└── screenshots/        # Скриншоты для документации
```

## ⚙️ Установка и запуск
```
1. Установка зависимостей
pip install -r requirements.txt
2. Настройка Redis
sudo apt update
sudo apt install redis-server
sudo systemctl enable redis-server
sudo systemctl start redis-server
3. Настройка базы данных
python manage.py migrate
python manage.py create_groups  # Создает группы с правами
python manage.py loaddata catalog/fixtures/*.json  # Загружает тестовые данные
4. Создание суперпользователя
python manage.py createsuperuser
5. Запуск сервера
python manage.py runserver
```

## 🔧 Основные команды
Команда	Описание
```
python manage.py create_groups	Создает группы пользователей
python manage.py clear_cache	Очищает кеш Redis
python manage.py load_products	Загружает тестовые товары
```

## 🌐 Доступные маршруты
Маршрут	Описание
```
/	Главная страница с товарами
/category/<slug>/	Товары по категориям
/product/<pk>/	Страница товара
/blog/	Список постов блога
/users/register/	Регистрация
/users/login/	Авторизация
/users/profile/	Профиль пользователя
/admin/	Админ-панель
```

## 🛠 Настройки кеширования
Проект использует Redis для кеширования:

Страницы товаров - 5 минут

Списки товаров - 30 минут

Товары по категориям - 1 час

Настройки в settings.py:

```
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
```

## 📌 Шаблоны каталога

Основные:
```
base.html - базовый шаблон
menu.html - навигационное меню
```
Товары:
```
home.html - главная страница (аналог product_list.html)
product_detail.html - детали товара
product_form.html - форма создания/редактирования
product_confirm_delete.html - подтверждение удаления
category_products.html - товары по категориям
```
Пользователи:
```
login.html - авторизация
register.html - регистрация
profile.html - профиль
```

## 🔥 Дополнительные функции

Модерация товаров (статусы: опубликовано/на модерации/отклонено)

Права доступа (владельцы, модераторы, контент-менеджеры)

Валидация форм (запрещенные слова, проверка цен)

Загрузка изображений (с проверкой формата и размера)

### 📝 Лицензия
MIT License. Смотрите файл LICENSE для подробностей.

<div align="center"> <sub>Создано с ❤️ для вашего интернет-магазина</sub> </div>
