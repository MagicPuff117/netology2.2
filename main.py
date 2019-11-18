class Animal:

    def __init__(self, name, weight, gender, type):
        self.name = name
        self.weight = weight
        self.gender = gender
        self.type = type  # Вводим вид животного (курица, гусь, овца, корова, утка)

    def voice_recognize(self):
        if self.type == 'гусь':
            print(self.name.title(), 'сказал "ГА-ГА-ГА"')
        elif self.type == "корова":
            print(self.name.title(), 'сказала "МУУУУ"')
        elif self.type == "утка":
            print(self.name.title(), 'сказала "КРЯ-КРЯ"')
        elif self.type == 'курица':
            print(self.name.title(), 'сказала "КУКАРЕКУ"')
        elif self.type == 'коза':
            print(self.name.title(), 'сказала "БЕЕЕ"')
        elif self.type == 'овца':
            print(self.name.title(), 'сказал "МЕЕЕЕ"')
        else:
            print("Таких животных на ферме Дядюшки Джо не водится")

    def feed(self):
        if self.gender == 'male':
            print(self.name.title(), 'накормлен')
        elif self.gender == 'female':
            print(self.name.title(), 'накормлена')
        else:
            print('У животных нет других полов')



class Birds(Animal):

    def take_eggs(self):
        if self.type == 'гусь' or self.type == 'курица' or self.type == 'утка':
            print(f'Яйца у {self.name.title()} собраны')
        else:
            print('Аккуратней!')




bird1 = Birds('Серый', 40, 'male', 'гусь')
bird2 = Birds('Белый', 37, 'male', 'гусь')
bird3 = Birds('Ко-ко', 6, 'female', 'курица')
bird4 = Birds('Кукареку', 7, 'female', 'курица')

bird1.take_eggs()
bird1.voice_recognize()
bird1.feed()
bird2.take_eggs()
bird2.voice_recognize()
bird2.feed()
bird3.take_eggs()
bird3.voice_recognize()
bird3.feed()
bird4.take_eggs()
bird4.voice_recognize()
bird4.feed()


class milk_giving(Animal):

    def get_milk(self):
        if self.type == 'корова' or self.type == 'коза':
            print(f'Молоко у {self.name.title()} сцежено')
        else:
            print('Ну головой-то подумай!')


mamle1 = milk_giving('Манька', 350, 'female', 'корова')
mamle2 = milk_giving('Рога', 85, 'female', 'коза')
mamle3 = milk_giving('Копыта', 79, 'female', 'коза')

mamle1.voice_recognize()
mamle1.feed()
mamle1.get_milk()
mamle2.voice_recognize()
mamle2.feed()
mamle2.get_milk()
mamle3.voice_recognize()
mamle3.feed()
mamle3.get_milk()


class wool_rich(Animal):
    def get_wool(self):
        if self.type == 'овца':
            print(self.name.title(), 'теперь мёрзнет')
        else:
            print('А ну положи бритву на стол!')


sheep1 = wool_rich('Барашек', 48, 'male', 'овца')
sheep2 = wool_rich('Кудрявый', 54, 'male', 'овца')
sheep1.feed()
sheep1.voice_recognize()
sheep1.get_wool()
sheep2.feed()
sheep2.voice_recognize()
sheep2.get_wool()



animals = [bird1, bird2,bird3, bird4 , mamle3, mamle2, mamle1, sheep2, sheep1]
print(f'Суммарный вес всех животных :{sum(sum_weight.weight for sum_weight in animals)} кг')

for animal in animals:
    if animal.weight == max(max_weight.weight for max_weight in animals):
        print(f'Самое тяжелое животное {animal.name}')







