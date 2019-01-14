from jchart import Chart
from jchart.config import Axes, DataSet, rgba

class BarChart(Chart):
    chart_type = 'bar'

    def __init__(self, salary_list):
        super(BarChart, self).__init__()
        self.salary_list = salary_list

    def get_labels(self, **kwargs):
        return [salary.worked_years for salary in self.salary_list]

    def get_datasets(self, **kwargs):
        data = [salary.salary for salary in self.salary_list]

        return [DataSet(label="Salaries", data=data)]
