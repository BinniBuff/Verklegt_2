from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Job, JobApplication
from .forms import ContactInformationForm, CoverLetterForm, ExperienceForm, ReferencesForm

# Create your views here.


@login_required
def apply_step_1(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if JobApplication.objects.filter(user=request.user, job=job).exists():
        return redirect('application_status', job_id=job_id)

    if request.method == 'POST':
        form = ContactInformationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.job = job
            application.save()
            return redirect('apply_step_2', job_id=job_id)
    else:
        form = ContactInformationForm()

    return render(request, 'apply_step_1.html', {'form': form, 'job': job})


@login_required
def apply_step_2(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    application = get_object_or_404(JobApplication, user=request.user, job=job)

    if request.method == 'POST':
        form = CoverLetterForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect('apply_step_3', job_id=job_id)
    else:
        form = CoverLetterForm(instance=application)

    return render(request, 'apply_step_2.html', {'form': form, 'job': job})


@login_required
def apply_step_3(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    application = get_object_or_404(JobApplication, user=request.user, job=job)

    if request.method == 'POST':
        form = ExperienceForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect('apply_step_4', job_id=job_id)
    else:
        form = ExperienceForm(instance=application)

    return render(request, 'apply_step_3.html', {'form': form, 'job': job})


@login_required
def apply_step_4(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    application = get_object_or_404(JobApplication, user=request.user, job=job)

    if request.method == 'POST':
        form = ReferencesForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            application.status = 'submitted'
            application.save()
            return redirect('application_success')
    else:
        form = ReferencesForm(instance=application)

    return render(request, 'apply_step_4.html', {'form': form, 'job': job})


@login_required
def application_status(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    application = get_object_or_404(JobApplication, user=request.user, job=job)
    return render(request, 'application_status.html', {'application': application, 'job': job})


def application_success(request):
    return render(request, 'application_success.html')
