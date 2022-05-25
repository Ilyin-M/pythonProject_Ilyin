users_list = {'Misha': '0000', 'Masha': '1111', 'Olga': '2222'}

def check_password(login, password):
    try:
        if users_list[login] == password:
            print(f'Здравствуйте, {login}!')
            return True
        print('Пароль введен не верно.')
        return False
    except KeyError:
        print('Данного пользователя не существует. Пройдите регистрацию.')
        return False


class Basket:
    def __init__(self):
        self.list_of_items = []


class User:
    def __init__(self, login: str, password: str):
        self.__login = login
        self.__password = password
        self.__basket = Basket()

    def add_item_to_basket(self, item):
        self.__basket.list_of_items.append(item)

    def show_all_in_basket(self):
        for n, item in enumerate(self.__basket.list_of_items):
            print(f'{n+1}: {item.name} - 1 шт.; цена: {item.price} руб.; (рейтинг товара:{item.rating})')

    def print_all_in_basket(self):
        for n, item in enumerate(self.__basket.list_of_items):
            print(f'{n+1}: {item.name} - 1 шт.; цена: {item.price} руб.')

    def sum_price_all_in_basket(self):
        sum = 0
        for n, item in enumerate(self.__basket.list_of_items):
            sum = sum + item.price
        return sum