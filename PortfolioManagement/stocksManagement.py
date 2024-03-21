import pandas as pd


class StocksManagement(object):

    def __init__(self):
        self.imported_data = None
        self.formulated_data = None
        pass

    def load_data(self, filename):
        self.imported_data = pd.read_csv(filename)

    def formulate_data(self):
        pass

