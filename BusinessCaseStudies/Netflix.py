import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from BusinessCaseStudies.CaseStudy import CaseStudy


class Netflix(CaseStudy):

    def __init__(self) -> None:
        super().__init__()
        self.read_csv_data('Netflix')

    def display_data(self):
        print(self.data)
