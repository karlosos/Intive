from django.shortcuts import render
from django.views import generic
from django.template import loader
from django.http import HttpResponse

from .models import Salary


class IndexView(generic.TemplateView):
    template_name = 'cognitive/index.html'


class SalaryView(generic.ListView):
    template_name = 'cognitive/salary.html'
    context_object_name = 'salary_list'

    def get_queryset(self):
        """
        Return the list of salaries
        """
        return Salary.objects.all()


def SalaryFilterView(request):
    salary_list = Salary.objects.order_by('worked_years')

    worked_years_start = request.GET['worked_years_start']
    worked_years_stop = request.GET['worked_years_stop']
    salary_brutto_start = request.GET['salary_brutto_start']
    salary_brutto_stop = request.GET['salary_brutto_stop']

    if worked_years_start:
        salary_list = salary_list.filter(worked_years__gt=worked_years_start)
    if worked_years_stop:
        salary_list = salary_list.filter(worked_years__lt=worked_years_stop)
    if salary_brutto_start:
        salary_list = salary_list.filter(salary__gt=salary_brutto_start)
    if salary_brutto_stop:
        salary_list = salary_list.filter(salary__lt=salary_brutto_stop)

    context = {'salary_list': salary_list}
    return render(request, 'cognitive/salary.html', context)

