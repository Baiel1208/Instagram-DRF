# import requests
# from bs4 import BeautifulSoup


# url = "https://blablacar.ru/"  
# response = requests.get(url)
# print(response)
# soup = BeautifulSoup(response.text, features="html.parser")

# print(soup)

books_list = [
"Марк Мэнсон:","тонкое искусство пофигизма", "Харв Экер:","думай как миллионер", " Роберт Кийосаки и Шэрон Л Лектер:","богатый папа бедный папа","Джордж Самюэль Клейсон:", "самый богатый человек в вавилоне", "Ларри Кинг:","как разговаривать с кем угодно когда угодно и где угодно","Наполеон Хилл:" , "думай и богатей", "Джеймс Рапсон и Крейг Инглиш:", "похвалите меня","Келли Макгонигал:", "сила воли", "Джэн Синсеро:", "не ной", "Саидмурад Давлатов:1", "я и деньги", "Луиза Хей:", "Исцели себя сам"
]
number_of_books_read = 11
book = input("Введите название книги: ")

if book in books_list:
    print(True)
else:
    print(False)