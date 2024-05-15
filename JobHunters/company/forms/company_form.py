from django.forms import ModelForm, widgets
from company.models import Company

class CompanyUpdateForm(ModelForm):
    class Meta:
        model = Company
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'category': widgets.Select(attrs={'class': 'form-control'}),
            'company': widgets.Select(attrs={'class': 'form-control'}),
            'date_expired': widgets.DateInput(attrs={'class': 'form-control'})
        }
class CompanyForm(ModelForm):
    class Meta:
        model = Company
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'category': widgets.Select(attrs={'class': 'form-control'}),
            'company': widgets.Select(attrs={'class': 'form-control'}),
            'date_expired': widgets.DateInput(attrs={'class': 'form-control'})
        }