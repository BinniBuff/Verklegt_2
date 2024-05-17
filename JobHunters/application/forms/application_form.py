from django import forms
from application.models import JobApplication

class ContactInformationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['name', 'street_name', 'house_number', 'city', 'country', 'postal_code']

class CoverLetterForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['cover_letter']

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['experience']

class ReferencesForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['references']
