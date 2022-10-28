class Animal:

    count = 0

    def __init__(self,
                 age: int = 0
                 ):
        """

        Args:
            age (int, optional): 동물의 나이. 기본값은 0.
        """

        self.age = age

        self.name = f"{Animal.count}번"

        Animal.count = Animal.count + 1

        return

    def eat(self):
        print(f"동물 {self.name}이 음식을 먹었습니다.")

    def get_age(self):
        print(f"동물 '{self.name}'의 나이는 {self.age}살 입니다.")

    @classmethod
    def get_count(cls):
        print(f"동물이 {cls.count}마리 생성되었습니다.")

    @staticmethod
    def hello():
        print(f"동물 농장에 오신 것을 환영합니다.")
