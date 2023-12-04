class Phone:

    def __init__(
            self,
            mark: str,
            model: str,
            count: int,
            is_new: bool
    ):
        """
        Конструктор приложения, хранящего информацию о сотовых телефонах

        :param mark: Марка
        :param model: Модель
        :param count: Количество
        :param is_new: Флаг что телефон новый, а не Б/У
        """

        self.mark = mark
        self.model = model
        self.count = count
        self.is_new = is_new

    @staticmethod
    def print_object(phone_obj: object) -> None:
        """
        Статический метод. Выводит информацию об экземпляре класса

        :param phone_obj: Экземпляр класса
        :return:
        """
        for attr, value in phone_obj.__dict__.items():
            print('Значение поля ' + attr + ' = ' + str(value))
        print()


if __name__ == '__main__':
    phone_one = Phone(mark='Sony', model='Ericsson', count=10, is_new=True)
    Phone.print_object(phone_one)

    phone_two = Phone(mark='Nokia', model='3310', count=3, is_new=False)
    Phone.print_object(phone_two)
