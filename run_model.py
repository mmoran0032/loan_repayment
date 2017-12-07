#!/usr/bin/env python3


from pathlib import Path

# import pymc3 as pm

from data import Data


def prepare_data(filepath):
    data = Data(filepath)
    data.prepare()
    target_paid = data.split_target('total_rec_prncp') / data['loan_amnt']
    target_fullypaid = data.split_target('loan_status')
    print(data.df.shape, target_paid.shape, target_fullypaid.shape, sep='\n')
    print(data.df.head(), target_paid.head(), target_fullypaid.head(), sep='\n')


if __name__ == '__main__':
    filepath = Path('LoanStats3a.csv')
    prepare_data(filepath)
