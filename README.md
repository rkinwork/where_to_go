# Куда пойти — Москва глазами Артёма

## Описание
Сайт о самых интересных местах в Москве. Авторский проект Артёма. Сервис разработан для публикации мест контент менеджером. Сайт имеет адаптивный фронт-енд, который хорошо смотрится как с мобильных устройств, так и с десктопа. Можно легко добавлять точки, и легко редактировать контент используя WYSIWYG редактор. Можно ознакомится с [боевой версией](http://rkinwork.pythonanywhere.com/) или [докой фронт-енда](https://github.com/devmanorg/where-to-go-frontend)

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
Тестовые данные взяты с сайта [KudaGo](https://kudago.com).

## Предварительные требования
Бэкенд был разработан используя `python==3.8`, при установке рекомендуется использовать эту версию.

Важно что бы был установлены следующие программы:
* [git](https://git-scm.com/)
* [pyenv](https://github.com/pyenv/pyenv)
* [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)

## Установка

### Подготовка окружения
```bash
git clone git@github.com:rkinwork/where_to_go.git
pyenv install 3.8.2
cd where_to_go
pyenv virtualenv 3.8.2 where_to_go
pyenv activate where_to_go
```

### Установка зависимостей Python

Здесь и далее мы остаемся в корне папки с проектом `where_to_go`
```bash
pip3 install -r requirements.txt
```

### Подготовка
Наполним переменные окружения
```bash
echo -e 'SECRET_KEY=YOUR_SUPER_SECRET_KEY
DEBUG=True' > .env
```

Сделаем миграции
```bash
python manage.py migrate
```

### Первичное наполнение данными

```bash
python manage.py load_place 
```

### Подготовка админки
Что бы войти в админку нужно будет создать супер пользователя.
```bash
python manage.py createsuperuser
```

Если забыли пароль, то потом можно будет его сбросить так
```bash
python manage.py changepassword <user_name>
```

## Запуск сайта
```bash
python manage.py runserver
```

* [главная страница](http://127.0.0.1:8000/)
* [админка](http://127.0.0.1:8000/admin)


## Создатели

* **Roman Kazakov**
* **DVMN.ORG team**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
