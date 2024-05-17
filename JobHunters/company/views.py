from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from company.models import Company
from company.forms.company_form import CompanyForm, CompanyUpdateForm
from django.shortcuts import render, redirect
from .forms import company_form



def add_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('company-list')
    else:
        form = CompanyForm()
    return render(request, 'company/add_company.html', {'form': form})

def index(request):
    return render(request, 'company/index.html', {
        'companies': Company.objects.all()
    })

def get_company_by_id(request, id):
    return render(request, 'company/company_details.html', {
        'companies': get_object_or_404(Company, pk=id)
    })

@login_required
def delete_company(request, id):
    company = get_object_or_404(Company, pk=id)
    company.delete()
    return redirect('company-index')

@login_required
def update_company(request, id):
    instance = get_object_or_404(Company, pk=id)
    if request.method == 'POST':
        form = CompanyUpdateForm(data=request.POST ,instance=instance)
        if form.is_valid():
            form.save()
            return redirect('get-company', id)
    else:
        form = CompanyUpdateForm(instance=instance)
    return render(request, 'company/update_company.html', {
        'form': form,
        'id': id
    })