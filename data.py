

import pandas as pd


class Data:
    def __init__(self, filepath=None):
        self.filepath = filepath
        self.df = None

    def __getitem__(self, name):
        if self.df is not None:
            return self.df[name]

    def prepare(self):
        self.load()
        self.restrict()
        self.transform()

    def load(self):
        cols = ['annual_inc', 'dti', 'revol_util', 'int_rate', 'loan_amnt',
                'term', 'purpose', 'loan_status', 'total_rec_prncp']
        self.df = pd.read_csv(self.filepath, header=1, usecols=cols).dropna()
        return self

    def restrict(self):
        keep = ['Fully Paid', 'Charged Off']
        self.df = self.df[self.df['loan_status'].isin(keep)]
        return self

    def transform(self):
        self.df['loan_status'] = ((self.df['loan_status'] == 'Fully Paid')
                                  .astype(int))
        self.df.loc[:, 'term'] = (self.df['term']
                                  .str.lower()
                                  .str.replace(' months', '')
                                  .astype('float64')) / 12
        self.df.loc[:, 'int_rate'] = (self.df['int_rate']
                                      .str.replace('%', '')
                                      .astype('float64'))
        self.df.loc[:, 'revol_util'] = (self.df['revol_util']
                                        .str.replace('%', '')
                                        .astype('float64'))
        dummies = pd.get_dummies(self.df['purpose'])
        self.df = (pd.concat([self.df, dummies], axis=1)
                   .drop('purpose', axis=1))
        return self

    def split_target(self, target=None):
        if not target:
            target = self.target_name
        y = self.df.loc[:, target]
        self.df = self.df.drop(target, axis=1)
        return y
