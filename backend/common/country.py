class Country(object):
    """super class"""

    name = '국가명'
    population = ''
    capital = ''

    def show(self):
        print('국가 클래스의 메소드입니다.')


class Korea(Country):
    """sub class"""

    def __init__(self,name):
        self.name = name

    def show_name(self):
        print('국가 이름은 : ', self.name)

def execute():
    k = Korea()
    k.show


main()
