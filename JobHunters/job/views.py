from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.db.models import Q

from job.forms.job_form import JobForm, JobUpdateForm
from job.models import Job, Category


# Create your views here.
def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        jobs = Job.objects.filter(
            Q(name__icontains=search_filter) |
            Q(company__name__icontains=search_filter) |
            Q(category__name__icontains=search_filter)
        ).distinct().order_by('date_offer')
        job_data = [{
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'category': x.category.name,
            'company': x.company.name,
            'full_part_time': x.full_part_time,
            'expires': x.date_expired.strftime('%Y-%m-%d'),
            'logo': x.company.logo.url if x.company.logo else None
        } for x in jobs]
        return JsonResponse({'data': job_data})
    else:
        return render(request, 'job/index.html', {
            'jobs': Job.objects.all().order_by('date_offer')
        })

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