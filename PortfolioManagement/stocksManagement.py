import pandas as pd


class StocksManagement(object):

    def __init__(self):
        self.imported_data = None
        self.formulated_data = None
        self.data = None
        pass

    def load_data(self, filename):
        self.imported_data = pd.read_csv(filename)
        self.data = self.imported_data

    def formulate_data(self):
        pass

    def drop_columns(self, columns):
        self.data.drop(columns=columns, inplace=True)

