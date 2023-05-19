"""

 3. Користувач водить рядок. Якщо він починається на 'abc', замінити їх на 'www', інакше додати в кінець рядка 'zzz'.

"""

text = input("Введіть текст: ")

if text.startswith("abc"):
    text = text.replace("abc", "www")
else:
    text += "zzz"

print(text)
