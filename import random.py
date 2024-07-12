import string
#Kullanıcıdan Özel karakterlerden oluşmasını istediğimiz şifre almak.
print("""Merhaba! Lütfen büyük-küçük harf, özel karekter ve sayı içeren bir sayı giriniz.""")

def check_password_complexity(password):
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    return has_uppercase and has_lowercase and has_digit and has_special

while True:
    user_password = input("Lütfen bir şifre girin: ")

    if check_password_complexity(user_password):
        print("Şifre kabul edildi!")
        break
    else:
        print("Şifre karmaşıklık kriterlerine uymuyor. Lütfen tekrar deneyin.")


