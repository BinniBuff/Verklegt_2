from django.shortcuts import render, get_object_or_404
from job.models import Job


# Create your views here.
def index(request):
    return render(request, 'job/index.html', {
        'jobs': Job.objects.all().order_by('date_offer')
    })

def get_job_by_id(request, id):
    return render(request, 'job/job_details.html', {
        'job': get_object_or_404(Job, pk=id)
    })