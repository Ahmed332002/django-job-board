from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('job_list/', views.job_list, name='job_list'),
    path('<slug:slug>/', views.job_detail, name='job_detail'),
    path('<int:job_id>/', views.apply_job, name='apply_job'),


]