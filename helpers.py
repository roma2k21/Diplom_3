import requests
import random
import string
from data import Urls


# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список


class CreateUser:
    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @staticmethod
    def register_new_user_and_return_login_password():
        # метод генерирует строку, состоящую только из букв нижнего регистра,
        # в качестве параметра передаём длину строки
        # создаём список, чтобы метод мог его вернуть
        login_pass = []  # генерируем логин, пароль
        email = CreateUser.generate_random_string(7) + f"@yandex.ru"
        password = CreateUser.generate_random_string(10)
        name = CreateUser.generate_random_string(5)
        payload = {"name": name, "email": email, "password": password}
        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post(Urls.URL + Urls.CREATE_USER,
                                 data=payload)  # если регистрация прошла успешно (код ответа 200),
        # добавляем в список логин и пароль
        if response.status_code == 200:
            login_pass.append(name)
            login_pass.append(email)
            login_pass.append(password)
        # возвращаем список
        return login_pass


class CreteOrder:
    def create_new_order(self, authorization_user):
        login_password = CreateUser.register_new_user_and_return_login_password()
        payload = {"email": login_password[0], "password": login_password[1]}
        response = requests.post(Urls.URL + Urls.LOGIN_USER, data=payload)
        response_ingridients = requests.get(Urls.URL + Urls.INGREDIENTS)
        payload_ingridients = {"ingredients": [response_ingridients.json()["data"][0]["_id"]]}
        response_order = requests.post(Urls.URL + Urls.CREATE_ORDER, data=payload_ingridients, headers={"Authorization": response.json()["accessToken"]})

