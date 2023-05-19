"""

2. Користувач вводить текст і слово, яке потрібно знайти, якщо це слово є в тексті, вивести 'YES', інакше 'NO'

"""
import re


text = input("Введіть текст: ")
search_word = input("Введіть слово: ")
text = re.sub(r'[^\w\s-]', ' ', text)

if search_word in text.split():
    print("YES")
else:
    print("NO")