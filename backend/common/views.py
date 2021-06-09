import pandas as pd
from real_estate.dataset import Dataset
from real_estate.housing import Housing


class Controller(object):
    dataset: object = Dataset()
    housing: object = Housing()

    def preprocess(self, KBhousing):
        housing = self.housing
        this = self.dataset
        this.KBhousing = housing.new_model(KBhousing)
        self.print_this(this)
        return this

    @staticmethod
    def print_this(this):
        print('*' * 100)
        print(f'1. exel type is {type(this.KBhousing)}')
        print(f'2. exel colums is \n{this.KBhousing.columns}')
        print(f'3. exel TOP is \n{this.KBhousing.head()}')
        print(f'4. exel number of null is \n{this.KBhousing.isnull().sum()}')

    @staticmethod
    def main():
        while 1:
            m = input('0. EXIT 1. make model 2. make Dataframe ')
            if m == '0':
                pass
            elif m == '1':
                Controller().preprocess('housing.xlsx')
            elif m == '2':
                pass
            else:
                continue


Controller.main()
