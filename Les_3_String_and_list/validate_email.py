"""

4. Написати валідатор для пошти.
Користувач вводить пошту, а програма повинна перевірити, що в пошті є символ '@' і '.',
і якщо це так, вивести "YES", інакше "NO"

"""
import re


def validate_email(email):
    if re.search('[а-яА-Я]', email):
        return 'NO. Помилка: email містить кирилицю'
    if re.search('[^a-zA-Zа-яА-Я0-9.@_-]', email):
        return 'NO. Помилка: email містить заборонені символи'
    if not re.search('@', email):
        return 'NO. Помилка: email не містить символ @'
    if not re.search('[a-zA-Z0-9]+\.[a-zA-Z]{2,}', email):
        return 'NO. Помилка: email не містить домен'
    if len(email) > 25:
        return 'NO. Помилка: email має бути не довше, ніж 25 символів'
    return True


email_for_validation = input("Введіть email: ")
is_valid = validate_email(email_for_validation)

if is_valid:
    print(f'YES. Email "{email_for_validation}" валідний')
else:
    print(is_valid)
