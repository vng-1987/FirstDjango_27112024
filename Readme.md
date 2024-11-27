# Django_27112024

## Инструкция по развертыванию проекта

1. Создать виртуальное окружение:
	'python3 -m venv django_venv'
2. Активировать виртуальное окружение:
	'source django_venv/bin/activate'
3. Установить нужные пакеты:
	'python -m pip install -r requirements.txt'
4. Применить все миграции для создания таблицы в БД:
	'python ./manage.py migrate'
5. Запустить сервер:
	'python ./manage.py runserver'

## Запуск 'ipython' в контексте приложений проекта 'django'
'''
python ./manage.py shell_plus --ipython
'''