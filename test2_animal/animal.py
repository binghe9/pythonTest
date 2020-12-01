import yaml


class Animal:
    def __init__(self,name,color,age,sex):
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex

    def speak(self):
        print(f"{self.name}在叫")

    def run(self):
        print(f"{self.name}在跑")

class Cat(Animal):
    def __init__(self,name,color,age,sex,hair='短毛'):
        super().__init__(name,color,age,sex)
        self.hair = hair
        self.hair = '短毛'
    def cat_skill(self):
        print("抓到了老鼠")

    def speak(self):
        print(f"{self.name}喵喵叫")

class Dog(Animal):
    def __init__(self,name,color,age,sex,hair='长毛'):
        super().__init__(name,color,age,sex)
        self.hair = hair

    def speak(self):
        print(f"{self.name}汪汪叫")

    def dog_skill(self):
        print('在看家')


def get_data():
    with open('data.yml',encoding='utf-8') as f :
        datas = yaml.safe_load(f)
    return datas

if __name__ == '__main__':
    cat = Cat(get_data()['cat']['name'],get_data()['cat']['color'],get_data()['cat']['age'],get_data()['cat']['sex'])
    print(f"它叫做{cat.name},今年{cat.age}岁了，是一只{cat.color}{cat.hair}的小猫，它今天")
    cat.cat_skill()

    dog = Dog(get_data()['dog']['name'],get_data()['dog']['color'],get_data()['dog']['age'],get_data()['dog']['sex'])
    print(f"它叫做{dog.name},今年{dog.age}岁了，是一只{dog.color}{dog.hair}的小狗，它今天")
    dog.dog_skill()
