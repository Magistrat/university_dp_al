from typing import Literal


class ClientWebStore:
    Count = 0

    def __init__(
            self,
            user_name: str = 'default_user_name',
            age: int = 20,
            gender: Literal['woman', 'man'] = 'men',
            login: str = 'default_login',
            password: str = '1234qwerty'
    ):
        """
        Конструктор клиента интернет-магазина

        :param user_name: Имя пользователя
        :param age: Возраст
        :param gender: Пол
        :param login: Логин
        :param password: Пароль
        """

        if age < 18:
            raise ValueError(f'Пользователь должен быть старше 18, текущий возраст: {age}')

        ClientWebStore.Count += 1

        self.__id = ClientWebStore.Count
        self.user_name = user_name
        self.age = age
        self.gender = gender
        self.login = login
        self.__password = password

    @property
    def password(self) -> str:
        """
        Метод для получения пароля
        :return: Текущий пароль
        """
        return self.__password

    @password.setter
    def password(self, new_password: str) -> None:
        """
        Метод для изменения пароля на новый
        :param new_password: Новый пароль
        :return:
        """
        self.__password = new_password

    @property
    def id(self) -> int:
        """
        Метод для получения ID Пользователя
        :return: ID Пользователя
        """
        return self.__id

    @id.setter
    def id(self, new_id: int) -> None:
        """
        Метод для изменения/присвоения ID Пользователя
        :param new_id: Новый ID Пользователя
        :return:
        """
        self.__id = new_id

    @staticmethod
    def print_object(client: object) -> None:
        """
        Статический метод. Выводит информацию об экземпляре класса

        :param client: Экземпляр класса
        :return:
        """
        for attr, value in client.__dict__.items():
            print('Значение поля ' + attr + ' = ' + str(value))
        print()


if __name__ == '__main__':
    client_one = ClientWebStore()
    ClientWebStore.print_object(client_one)

    client_two = ClientWebStore(
        user_name='Max',
        age=22,
        gender='man',
        login='max_',
        password='Password123'
    )
    ClientWebStore.print_object(client_two)

    try:
        ClientWebStore(age=10)
    except ValueError:
        print('Нельзя создать с возрастом 10')
