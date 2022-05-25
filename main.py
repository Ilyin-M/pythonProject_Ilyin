from termcolor import colored
import random
from user import check_password
from user import User
from item_category import Category, Item

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

    category_1 = Category('Пиломатериалы', [Item('Брус 100*100*6000 е.в., сорт 3-4', 1140, 2), Item('Брус 100*100*6000 е.в., сорт 1-2', 1599, 3), Item('Брус 100*150*6000 е.в., сорт 3-4', 1980, 3), Item('Брус 100*150*6000 е.в., сорт 1-2', 2400, 3), Item('Брус 150*150*6000 е.в., сорт 3-4', 3280, 4), Item('Брус 150*150*6000 е.в., сорт 1-2', 3600, 4), Item('Брус 200*200*6000 е.в., сорт 3-4', 6500, 4.5), Item('Брус 200*200*6000 е.в., сорт 1-2', 7045, 4), Item('Брус 140*160*6000 стр., сорт 3-4', 7400, 2), Item('Брус 140*160*6000 стр., сорт 1-2', 7900, 2), Item('Брус 90*90*6000 стр., сорт 3-4', 2200, 2), Item('Брус 90*90*6000 стр., сорт 1-2', 2800, 2), Item('Брус 100*150*3000 е.в., сорт 3-4', 980, 3), Item('Брус 100*150*3000 е.в., сорт 1-2', 1200, 3), Item('Брус 150*150*3000 е.в., сорт 3-4', 1680, 4), Item('Брус 150*150*3000 е.в., сорт 1-2', 1800, 4), Item('Брус 200*200*3000 е.в., сорт 3-4', 3250, 4.5), Item('Брус 200*200*3000 е.в., сорт 1-2', 3505, 4), Item('Брус 140*160*3000 стр., сорт 3-4', 3700, 2), Item('Брус 140*160*3000 стр., сорт 1-2', 3850, 2)])
    category_2 = Category('Плитка', [Item('Плитка облицовочная Axima белая 300*200*7', 332, 3), Item('Плитка облицовочная Axima белая 350*250*7', 332, 3), Item('Плитка облицовочная Cersanit белая 300*200*7', 503, 3), Item('Плитка облицовочная Cersanit серая 300*200*7', 400, 3), Item('Плитка облицовочная Unitile белая 300*200*7', 440, 4), Item('Плитка облицовочная Unitile серая 300*200*7', 300, 4), Item('Плитка облицовочная Евро-Керамика тоскана-бежевая 400*270*7', 740, 4.5), Item('Плитка облицовочная Евро-Керамика белая 400*270*7', 740, 5), Item('Плитка облицовочная Cersanit Pudra многоцветная 440*200*8', 989, 4), Item('Плитка облицовочная Cersanit Atlas многоцветная 600*200*8', 1300, 4), Item('Плитка напольная Madison коричневая 400*400*8', 809, 4), Item('Плитка напольная Madison серая 400*400*8', 809, 4), Item('Плитка напольная Нефрит коричневая 385*385*8', 809, 4), Item('Плитка напольная Нефрит белая с крошкой 385*385*8', 809, 4), Item('Плитка напольная Unitile Pudra белая 440*200*7', 440, 4.5), Item('Плитка напольная Unitile Pudra серая 440*200*7', 300, 5), Item('Плитка напольная Unitile Alrami белая 440*200*7', 800, 4), Item('Плитка напольная Unitile Alrami черная 440*200*7', 700, 3), Item('Плитка напольная Керамин Гламур белая 480*250*10', 1110, 4), Item('Плитка напольная Керамин Гламур красная 480*250*10', 1200, 3)])
    category_3 = Category('Гвозди', [Item('Гвозди финишные омедненные 1,4*25мм (50 шт.)', 36, 3), Item('Гвозди финишные омедненные 1,4*35мм (40 шт.)', 37, 3), Item('Гвозди финишные омедненные 1,4*30мм (50 шт.)', 41, 3), Item('Гвозди финишные омедненные 1,4*40мм (40 шт.)', 41, 3), Item('Гвозди финишные омедненные 1,4*45мм (40 шт.)', 45, 3), Item('Гвозди финишные омедненные 1,2*20мм (100 шт.)', 39, 3), Item('Гвозди финишные омедненные 1,2*25мм (100 шт.)', 39, 3), Item('Гвозди финишные омедненные 1,2*30мм (100 шт.)', 45, 3), Item('Гвозди финишные омедненные 1,2*35мм (100 шт.)', 45, 3), Item('Гвозди финишные омедненные 1,2*40мм (100 шт.)', 60, 3), Item('Гвозди финишные оцинкованные 1,4*25мм (50 шт.)', 36, 3), Item('Гвозди финишные оцинкованные 1,4*35мм (40 шт.)', 37, 3), Item('Гвозди финишные оцинкованные 1,4*30мм (50 шт.)', 41, 3), Item('Гвозди финишные оцинкованные 1,4*40мм (40 шт.)', 41, 3), Item('Гвозди финишные оцинкованные 1,4*45мм (40 шт.)', 45, 3), Item('Гвозди финишные оцинкованные 1,2*20мм (100 шт.)', 39, 3), Item('Гвозди финишные оцинкованные 1,2*25мм (100 шт.)', 39, 3), Item('Гвозди финишные оцинкованные 1,2*30мм (100 шт.)', 45, 3), Item('Гвозди финишные оцинкованные 1,2*35мм (100 шт.)', 45, 3), Item('Гвозди финишные оцинкованные 1,2*40мм (100 шт.)', 60, 3)])
    category_4 = Category('Саморезы и шурупы', [Item('Саморезы ГД 19*3,5мм (40 шт.)', 49, 3), Item('Саморезы ГД 30*3,5мм (30 шт.)', 45, 3), Item('Саморезы ГД 41*3,5мм (25 шт.)', 45, 3), Item('Саморезы ГД 55*3,5мм (13 шт.)', 40, 3), Item('Саморезы ГД 65*3,8мм (11 шт.)', 42, 3), Item('Саморезы ГД 75*4,2мм (10 шт.)', 42, 3), Item('Саморезы ГД 90*4,2мм (6 шт.)', 45, 3), Item('Саморезы ГД 110*4,8мм (3 шт.)', 35, 3), Item('Саморезы ГД 127*4,8мм (3 шт.)', 35, 3), Item('Саморезы ГД 152*4,8мм (2 шт.)', 55, 3), Item('Саморезы ГМ 19*3,5мм (40 шт.)', 89, 5), Item('Саморезы ГМ 30*3,5мм (30 шт.)', 85, 5), Item('Саморезы ГМ 41*3,5мм (25 шт.)', 85, 5), Item('Саморезы ГМ 55*3,5мм (13 шт.)', 80, 5), Item('Саморезы ГМ 65*3,8мм (11 шт.)', 82, 5), Item('Саморезы ГМ 75*4,2мм (10 шт.)', 82, 5), Item('Саморезы ГМ 90*4,2мм (6 шт.)', 85, 5), Item('Саморезы ГМ 110*4,8мм (3 шт.)', 65, 5), Item('Саморезы ГМ 127*4,8мм (3 шт.)', 65, 5), Item('Саморезы ГМ 152*4,8мм (2 шт.)', 120, 5)])
    mag = Shop([category_1, category_2, category_3, category_4])
    mag.start()
