from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

author = {
	"Имя": "Иван",
	"Отчество": "Петрович",
	"Фамилия": "Иванов",
	"телефон": "8-923-600-01-02",
	"email": "vasya@mail.ru"
}

items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]

# Create your views here.
def home(request):
	text = """
		<h1>"Изучаем django"</h1>
		<strong>Автор</strong>: <i>Иванов И.П.</i>
	"""
	return HttpResponse(text)

def about(request):
	text = f"""
		<h2>Информация об авторе</h2>
		Имя: <b>{author['Имя']}</b><br>
		Отчество: <b>{author['Отчество']}</b><br>
		Фамилия: <b>{author['Фамилия']}</b><br>
		Телефон: <b>{author['телефон']}</b><br>
		Email: <b>{author['email']}</b><br>
	"""
	return HttpResponse(text)

def get_item(request, item_id:int):
	"""Функция по item_id нужного элемента вернет имя и кол-во."""
	for item in items:
		if item["id"] == item_id:
			result = f"""
				<h2>Имя: {item['name']}</h2>
				<p>Количество: {item['quantity']}</p>
			"""
			return HttpResponse(result)

	# Если элемент не найден - нужно вернуть соответствующий ответ (response)
	return HttpResponseNotFound(f"Item with id={item_id} not found")