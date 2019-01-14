from django.urls import path

from . import views

app_name = 'cognitive'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('salary/', views.SalaryView.as_view(), name='salary'),
    path('salary/filter/', views.SalaryFilterView, name='salary_filter'),
]
