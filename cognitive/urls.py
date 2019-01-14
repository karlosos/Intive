from django.urls import path

from . import views

app_name = 'cognitive'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('salary/', views.salary_view, name='salary'),
    path('salary/filter/', views.salary_filter_view, name='salary_filter'),
]
