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
        return self.__password

    @password.setter
    def password(self, new_password: str) -> None:
        self.__password = new_password

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, new_id: int) -> None:
        self.__id = new_id

    @staticmethod
    def print_object(client: object) -> None:
        print(client)

    def __str__(self) -> str:
        return f'Значение поля id = {self.__id}, значение поля user_name = {self.user_name}, ' \
               f'значение поля age = {self.age}, значение поля gender = {self.gender}, ' \
               f'значение поля login = {self.login}, значение поля password = {self.__password}'


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
