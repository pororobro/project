from common.models import Models
import pandas as pd

class Housing(object):

    models = Models()

    def new_model(self, payload):
        this = self.models
        this.context = './data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)

    def new_model_excel(self, payload):
        this = self.models
        this.context = './data/'
        this.fname = payload
        return pd.read_excel(this.context + this.fname, sheet_name='YainSoft_Excel')

    def print_this(this):
        print('*' * 100)
        print(f'1. exel type is {type(this.cctv_in_seoul)}')
        print(f'2. exel colums is \n{this.cctv_in_seoul.columns}')
        print(f'3. exel TOP is \n{this.cctv_in_seoul.head()}')
        print(f'4. exel number of null is \n{this.cctv_in_seoul.isnull().sum()}')