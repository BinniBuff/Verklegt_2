from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.db.models import Q

from job.forms.job_form import JobForm, JobUpdateForm
from job.models import Job, Category
from company.models import Company
from .models import JobApplication

# Create your views here.
def index(request):
    jobs = Job.objects.all()

    search_filter = request.GET.get('search_filter')
    if search_filter:
        jobs = jobs.filter(
            Q(name__icontains=search_filter) |
            Q(company__name__icontains=search_filter) |
            Q(category__name__icontains=search_filter)
        ).distinct()

    category_ids = request.GET.getlist('category_ids')
    company_ids = request.GET.getlist('company_ids')
    if category_ids:
        jobs = jobs.filter(category__id__in=category_ids)
    if company_ids:
        jobs = jobs.filter(company__id__in=company_ids)

    order_by = request.GET.get('order_by', 'date_offer')  # Default ordering by date offered
    jobs = jobs.order_by(order_by)

    context = {
        'jobs': jobs,
        'categories': Category.objects.all(),
        'companies': Company.objects.all()
    }
    return render(request, 'job/index.html', context)

def get_job_by_id(request, id):
    return render(request, 'job/job_details.html', {
        'job': get_object_or_404(Job, pk=id)
    })

@login_required
def create_job(request):
    if request.method == 'POST':
        form = JobForm(data=request.POST)
        if form.is_valid():
            job = form.save()
            return redirect('job-index')
    else:
        form = JobForm()
    return render(request, 'job/create_job.html', {
        'form': form
    })

@login_required
def delete_job(request, id):
    job = get_object_or_404(Job, pk=id)
    job.delete()
    return redirect('job-index')

@login_required
def update_job(request, id):
    instance = get_object_or_404(Job, pk=id)
    if request.method == 'POST':
        form = JobUpdateForm(data=request.POST ,instance=instance)
        if form.is_valid():
            form.save()
            return redirect('get-job', id)
    else:
        form = JobUpdateForm(instance=instance)
    return render(request, 'job/update_job.html', {
        'form': form,
        'id': id
    })

@login_required
def user_applications(request):
    applications = JobApplication.objects.filter(user=request.user).select_related('job')
    return render(request, 'job/user_applications.html', {'applications': applications})