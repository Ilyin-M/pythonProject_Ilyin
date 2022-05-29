from termcolor import colored
import random
from user import check_password
from user import User
from category_db import DB

class Shop:
    def __init__(self, categories):
        self.categories = categories

    def start(self):
        print('Добро пожаловать в строительный магазин "ВсевСАД"')
        login = input('Введите, пожалуйста, Ваш логин: ')
        password = input('Введите, пожалуйста, Ваш пароль: ')
        if not check_password(login, password):
            print(colored('Вход недоступен!', 'red', attrs=['underline']))
            return
        self.user = User(login, password)
        ans = True
        while ans:
            print("**************************************************************************")
            print('Выберите категорию:')
            self.show_all_category()
            while True:
                try:
                    current_cat = int(input('Введите, пожалуйста, требуемую категория: '))-1
                    if current_cat > len(self.categories) - 1 or current_cat < 0:
                        raise ValueError
                    break
                except ValueError:
                    print(colored('Ошибка!', 'red', attrs=['underline']))
                    print(f"Введите целое число от 1 до {len(self.categories)}")
            self.show_category_by_ID(current_cat)
            while True:
                try:
                    current_item = int(input('Введите, пожалуйста, номер требуемого товара: '))-1
                    if current_item > len(self.categories[current_cat].list_of_items) - 1 or current_item < 0:
                        raise ValueError
                    break
                except ValueError:
                    print(colored('Ошибка!', 'red', attrs=['underline']))
                    print(f"Введите целое число от 1 до {len(self.categories[current_cat].list_of_items)}")
            self.add_item_to_basket(current_cat, current_item)
            print("**************************************************************************")
            print('Список товаров в корзине:')
            self.user.show_all_in_basket()
            print("**************************************************************************")
            print('Если хотите продолжить покупки- введите Y(y); если хотите закончить покупки- введите любой другой символ:')
            if input().lower() == 'y':
                ans = True
            else:
                ans = False
        summa = self.user.sum_price_all_in_basket()
        ch = random.randrange(1000, 9999, 1)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(f"****************************** Заявка № {ch} *****************************")
        print("**************************************************************************")
        print("Товары:")
        self.user.print_all_in_basket()
        print("**************************************************************************")
        print(f"Итог: {summa} руб.")
        print(f"Сумма НДС 20%= {summa/5} руб.")
        print('OOO "ВсевСАД"')
        print('Адрес для претензий: 192207, г.С-Пб, Лиговский проспект, д.153, литера А ')
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    def show_all_category(self):
        for n, category in enumerate(self.categories):
            print(f'{n+1}: {category.name_cat}')

    def show_category_by_ID(self, category_ID):
        print("**************************************************************************")
        print(f'Выбранная для просмотра категория: {self.categories[category_ID].name_cat}')
        for n, item in enumerate(self.categories[category_ID].list_of_items):
            print(f'{n+1}: {item.name}; цена за 1 шт.: {item.price} руб.; (рейтинг товара:{item.rating})')

    def add_item_to_basket(self, category_ID, item_ID):
        item = self.categories[category_ID].list_of_items[item_ID]
        self.user.add_item_to_basket(item)


if __name__ == '__main__':

    mag = Shop(DB)
    mag.start()
