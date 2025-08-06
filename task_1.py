class OnlineSalesRegisterCollector:
    def __init__(self):
        self.__name_items = ['кола', 'молоко']
        self.__number_items = len(self.__name_items)
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    #1. Напиши геттеры
    @property
    def name_items(self):
        return self.__name_items
    
    @property
    def number_items(self):
        return self.__number_items
    
    @property
    def item_price(self):
        return self.__item_price
    
    @property
    def tax_rate(self):
        return self.__tax_rate
    
    #2. Добавь товар в чек
    def set_add_item_to_cheque(self, name):
        if len(name) == 0 or len(name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        elif name not in list(self.__item_price.keys()):
            raise NameError('Позиция отсутствует в товарном справочнике')
        else:
            self.__name_items.append(name)
            self.__number_items += 1

    #3. Удали товар из чека
    def delete_item_from_check(self, name):
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')
        else:
            self.__name_items.remove(name)
            self.__number_items -= 1

    #4. Посчитай общую стоимость товаров
    def check_amount(self):
        total = []
        for item in self.__name_items:
            total.append(self.__item_price[item])
        if self.__number_items > 10:
            total_price = sum(total) * 0.9
        else:
            total_price = sum(total)
        return total_price

    #5. Вычисли НДС для товаров со ставкой 20%
    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []
        for item in self.__name_items:
            if self.__tax_rate[item] == 20:
                twenty_percent_tax.append(self.__tax_rate[item])
                total.append(self.__item_price[item])
        if self.__number_items > 10:
            total_price = sum(total) * 0.9
        else:
            total_price = sum(total)
        total_tax = total_price * 0.2
        return total_tax

    #6. Вычисли НДС для товаров со ставкой 10%
    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = []
        for item in self.__name_items:
            if self.__tax_rate[item] == 10:
                ten_percent_tax.append(self.__tax_rate[item])
                total.append(self.__item_price[item])
        if self.__number_items > 10:
            total_price = sum(total) * 0.9
        else:
            total_price = sum(total)
        total_tax = total_price * 0.1
        return total_tax
    
    #7. Посчитай общую сумму налогов
    def total_tax(self):
        total_tax = self.ten_percent_tax_calculation() + self.twenty_percent_tax_calculation()
        return total_tax

    #8. Верни номер телефона покупателя
    def get_telephone_number(self, phone_number):
        self.__phone_number = phone_number
        if not isinstance(self.__phone_number, int):  # Проверка на целое число
            raise ValueError('Необходимо ввести цифры')
        elif len(str(self.__phone_number)) > 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
        
        return f"+7{self.__phone_number}"
    
#Проверка и вывод в консоль
item = OnlineSalesRegisterCollector()
print("***", "1. Напиши геттеры", sep='\n')
print(item.name_items)
print(item.number_items)
print(item.item_price)
print(list(item.item_price.keys()))  #ключи в список
print(item.tax_rate)

test_name = "чипсы"
print("***", "2. Добавь товар в чек", sep='\n')
item.set_add_item_to_cheque(test_name)
print(item.name_items)
print(item.number_items)
print(item.item_price)
print(item.tax_rate)

print("***", "4. Посчитай общую стоимость товаров", sep='\n')
print(item.check_amount())

print("***", "5. Вычисли НДС для товаров со ставкой 20%", sep='\n')
print(item.twenty_percent_tax_calculation())

print("***", "6. Вычисли НДС для товаров со ставкой 10%", sep='\n')
print(item.ten_percent_tax_calculation())

print("***", "7. Посчитай общую сумму налогов", sep='\n')
print(item.total_tax())

print("***", "8. Верни номер телефона покупателя", sep='\n')
print(item.get_telephone_number(1234567890))

print("***", "3. Удали товар из чека", sep='\n')
item.delete_item_from_check(test_name)
print(item.name_items)
print(item.number_items)
print(item.item_price)
print(item.tax_rate)