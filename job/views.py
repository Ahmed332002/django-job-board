from django.shortcuts import render
from django.http import HttpResponse
from .models import Job
from django.core.paginator import Paginator
from .form import ApplyForm


# Create your views here.

def index(request):
    pass

def job_list(request):
    job_list = Job.objects.all()
    pagination = Paginator(job_list, 2) # Show 2 jobs per page.
    page_number = request.GET.get('page')
    job_list = pagination.get_page(page_number)
    return render(request, 'job/job_list.html', 
         {'jobs': job_list}
         )

def job_detail(request, slug):
    job = Job.objects.get(slug=slug)
    return render(request, 'job/job_details.html', 
         {'job': job}
         )

def apply_job(request, job_id):
    job = Job.objects.get(id=job_id)
    return render(request, 'job/job_details.html', 
         { 'form': ApplyForm()}
         )