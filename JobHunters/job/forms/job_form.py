from django.forms import ModelForm, widgets
from job.models import Job
class JobForm(ModelForm):
    class Meta:
        model = Job
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'category': widgets.Select(attrs={'class': 'form-control'}),
            'company': widgets.Select(attrs={'class': 'form-control'}),
            'date_expired': widgets.DateInput(attrs={'class': 'form-control'})
        }