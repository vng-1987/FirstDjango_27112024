from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from MainApp.models import Item

# Нужный тип исключения для функции get_item()
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def home(request):
	context = {
		'name': 'Петров Иван Николаевич',
		'email': 'my_email@mail.ru'
	}
	return render(request, 'index.html', context)

def about(request):
   author = {
      "name": "Иван",
		"middle_name": "Петрович",
		"last_name": "Иванов",
		"phone": "8-923-600-01-02",
		"email": "vasya@mail.ru"
   }
   
   text=f"""	
   	<header>
		/ <a href="/">Home</a> / <a href="/items">Items</a>/ <a href="/about">About</a>
	</header>
		<h2>Информация об авторе</h2>
		Имя: <b>{author['name']}</b><br>
		Отчество: <b>{author['middle_name']}</b><br>
		Фамилия: <b>{author['last_name']}</b><br>
		Телефон: <b>{author['phone']}</b><br>
		Email: <b>{author['email']}</b><br>
  """
   return HttpResponse(text)

def get_item(request, item_id: int):
	#""" Функция по item_id нужного элемента вернет имя и количество. """
   try:
      item = Item.objects.get(id=item_id)
   except ObjectDoesNotExist:
      # Если элемент не найден - нужно вернуть соответствующий ответ (response)
      return render(request, "errors.html", {'error': f"Item with id={item_id} not found."})
   else:
      context = {'item':item}
      return render(request, 'item_page.html', context)

def get_items(request):
   items = Item.objects.all()
   context = {'items': items}
   return render(request, 'items_list.html', context)