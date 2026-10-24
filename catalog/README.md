# mr_Django
![Python Version](https://img.shields.io/badge/python-3.13+-blue)
![Django](https://img.shields.io/badge/django-6.1-green)
![Status](https://img.shields.io/badge/status-development-blue)
![Version](https://img.shields.io/badge/version-0.1.0-blue)

**mr_Django** — веб-приложение на Django для хранения и продажи плагинов, шаблонов и примеров кода.

## Содержание
- [Технологии](#технологии)
- [Установка](#установка)
- [Deploy и CI/CD](#deploy-и-ci/cd)
- [Contributing](#contributing)
- [To do](#to-do)
- [Команда проекта](#команда-проекта)


## Технологии
- **Python 3.13+** — язык программирования
- **Django 6.1** — веб-фреймворк
- **Poetry** — управление зависимостями
- **Bootstrap** — CSS-фреймворк для вёрстки
- **SQLite** — база данных (по умолчанию для разработки)

## Установка

```bash
# Клонировать репозиторий
git clone <repository-url>
cd /папка_с_прооектом/mr_Django
# Установить зависимости через poetry
poetry install
# Активировать виртуальное окружение
eval $(poetry env activate)
# Применить миграции
python manage.py migrate
```

## Использование
Расскажите как установить и использовать ваш проект, покажите пример кода:

### Запуск программы
```bash
python manage.py runserver
```


## Разработка

### Требования
- Python 3.12+
- Poetry

### Установка зависимостей
Для установки зависимостей, выполните команду:
```bash
poetry install --no-root
```

## Deploy и CI/CD
На текущем этапе CI/CD отсутствует.

## Contributing
По вопросам и предложениям писать на почту.

## FAQ 
Ответы на вопросы...

### Зачем вы разработали этот проект?
Чтобы был.

## To do

- [x] Настройка проекта и виртуального окружения
- [x] Создание приложения catalog и его регистрация
- [x] Настройка маршрутизации
- [x] Создание шаблонов home.html и contacts.html
- [x] Подключение Bootstrap
- [x] Контроллеры home и contacts
- [x] Форма обратной связи и её обработка
- [ ] ...

## Команда проекта
MC

## Источники
...