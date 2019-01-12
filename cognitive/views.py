from django.shortcuts import render
from django.views import generic

from .models import Salary


class SalaryView(generic.ListView):
    template_name = 'cognitive/salary.html'
    context_object_name = 'salary_list'

    def get_queryset(self):
        """
        Return the list of salaries
        """
        return Salary.objects.all()
