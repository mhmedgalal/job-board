from django.shortcuts import redirect, render,get_object_or_404
from django.urls import reverse

from job.filter import JobFilter
from .models import Job
from django.core.paginator import Paginator
from .forms import ApplyForm, JobForm
from django.contrib.auth.decorators import login_required

def job_list(request):
    jobs = Job.objects.all()
    my_filter = JobFilter(request.GET, queryset=jobs)
    jobs = my_filter.qs
    paginator = Paginator(jobs, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'jobs': page_obj,'job':jobs, 'my_filter': my_filter}
    return render(request, 'job_list.html', context)
@login_required
def job_details(request, slug):
    job = get_object_or_404(Job, slug=slug)
    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job
            myform.save()
            return redirect(reverse('jobs:job_list'))
    else:
        form = ApplyForm()
    context = {'job': job, 'form': form}
    return render(request, 'job_details.html', context) 

@login_required
def add_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))
    else:
        form = JobForm()
    return render(request, 'add_job.html', {'form': form})
