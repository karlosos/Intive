from django.shortcuts import render
from django.views import generic
from django.template import loader
from django.http import HttpResponse
from jchart import Chart

from .models import Salary
from cognitive import charts


class IndexView(generic.TemplateView):
    template_name = 'cognitive/index.html'


def salary_view(request):
    salary_list = Salary.objects.order_by('worked_years')
    context = {'salary_list': salary_list, 'bar_chart': charts.BarChart(salary_list)}

    return render(request, 'cognitive/salary.html', context)


def salary_filter_view(request):
    salary_list = Salary.objects.order_by('worked_years')

    worked_years_start = request.POST['worked_years_start']
    worked_years_stop = request.POST['worked_years_stop']
    salary_brutto_start = request.POST['salary_brutto_start']
    salary_brutto_stop = request.POST['salary_brutto_stop']

    if worked_years_start:
        salary_list = salary_list.filter(worked_years__gt=worked_years_start)
    if worked_years_stop:
        salary_list = salary_list.filter(worked_years__lt=worked_years_stop)
    if salary_brutto_start:
        salary_list = salary_list.filter(salary__gt=salary_brutto_start)
    if salary_brutto_stop:
        salary_list = salary_list.filter(salary__lt=salary_brutto_stop)

    context = {'salary_list': salary_list, 'bar_chart': charts.BarChart(salary_list)}

    return render(request, 'cognitive/salary.html', context)

