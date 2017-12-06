#!/usr/bin/env python3


from pathlib import Path

import pandas as pd
# import pymc3 as pm


def load_data(filepath):
    cols = ['annual_inc', 'dti', 'revol_util', 'int_rate', 'loan_amnt',
            'term', 'purpose', 'loan_status', 'total_rec_prncp']
    df = (pd.read_csv(filepath, header=0, usecols=cols)
          .dropna())
    df = df[df['loan_status'].isin(['Fully Paid', 'Charged Off'])]
    df.loc[:, 'term'] = (df['term']
                         .str.lower()
                         .str.replace(' months', '')
                         .astype('float64')) / 12
    df.loc[:, 'int_rate'] = (df['int_rate']
                             .str.replace('%', '')
                             .astype('float64'))
    df.loc[:, 'revol_util'] = (df['revol_util']
                               .str.replace('%', '')
                               .astype('float64'))
    return df


if __name__ == '__main__':
    filepath = Path('LoanStats3a.csv')
    df = load_data(filepath)
    print(df.shape)
    print(df.term.head())
