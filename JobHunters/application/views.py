from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Job, JobApplication
from application.forms.application_form import ContactInformationForm, CoverLetterForm, ExperienceForm, ReferencesForm

# Create your views here.

def store_in_session(request, form_data, step):
    session_data = request.session.get('application_data', {})
    session_data[step] = form_data
    request.session['application_data'] = session_data


def get_from_session(request, step):
    session_data = request.session.get('application_data', {})
    return session_data.get(step, {})


def clear_session(request):
    if 'application_data' in request.session:
        del request.session['application_data']


@login_required
def apply_step_1(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if request.method == 'POST':
        form = ContactInformationForm(request.POST)
        if form.is_valid():
            store_in_session(request, form.cleaned_data, 'step_1')
            return redirect('apply_step_2', job_id=job_id)
    else:
        form_data = get_from_session(request, 'step_1')
        form = ContactInformationForm(initial=form_data)

    return render(request, 'application/apply_step_1.html', {'form': form, 'job': job})


@login_required
def apply_step_2(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if request.method == 'POST':
        form = CoverLetterForm(request.POST)
        if form.is_valid():
            store_in_session(request, form.cleaned_data, 'step_2')
            return redirect('apply_step_3', job_id=job_id)
    else:
        form_data = get_from_session(request, 'step_2')
        form = CoverLetterForm(initial=form_data)

    return render(request, 'application/apply_step_2.html', {'form': form, 'job': job})


@login_required
def apply_step_3(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            store_in_session(request, form.cleaned_data, 'step_3')
            return redirect('apply_step_4', job_id=job_id)
    else:
        form_data = get_from_session(request, 'step_3')
        form = ExperienceForm(initial=form_data)

    return render(request, 'application/apply_step_3.html', {'form': form, 'job': job})


@login_required
def apply_step_4(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if request.method == 'POST':
        form = ReferencesForm(request.POST)
        if form.is_valid():
            store_in_session(request, form.cleaned_data, 'step_4')
            application_data = request.session.get('application_data', {})

            application = JobApplication(
                user=request.user,
                job=job,
                name=application_data['step_1']['name'],
                street_name=application_data['step_1']['street_name'],
                house_number=application_data['step_1']['house_number'],
                city=application_data['step_1']['city'],
                country=application_data['step_1']['country'],
                postal_code=application_data['step_1']['postal_code'],
                cover_letter=application_data['step_2']['cover_letter'],
                experience=application_data['step_3']['experience'],
                references=application_data['step_4']['references']
            )
            application.save()
            clear_session(request)
            return redirect('application_success')
    else:
        form_data = get_from_session(request, 'step_4')
        form = ReferencesForm(initial=form_data)

    return render(request, 'application/apply_step_4.html', {'form': form, 'job': job})


@login_required
def application_status(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    application = get_object_or_404(JobApplication, user=request.user, job=job)
    return render(request, 'application/application_status.html', {'application': application, 'job': job})


def application_success(request):
    return render(request, 'application/application_success.html')
