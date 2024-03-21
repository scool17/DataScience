import pandas as pd
import json


class CaseStudy(object):

    def __init__(self):
        self.data = None

    def read_csv_data(self, case_study_name):
        f = open("CaseStudyData/data.json")
        case_study_mapping = json.load(f)
        self.data = pd.read_csv(case_study_mapping.get(case_study_name))
        f.close()
