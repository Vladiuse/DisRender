from faker import Faker
import random as r
faker = Faker()


class Lorem:

    def __init__(self):
        self.i = 0
        self.max = self._get_max()

    def _get_max(self):
        return r.randint(5,15)


    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.max:
            self.max = self._get_max()
            self.i = 0
            raise StopIteration
        next = faker.paragraph()
        self.i += 1
        return next

    def __str__(self):
        return faker.paragraph()


lorem = Lorem()
if __name__ == '__main__':
    lorem = Lorem()
    for i in lorem:
        print(i)
    print('end')
    for i in lorem:
        print(i)