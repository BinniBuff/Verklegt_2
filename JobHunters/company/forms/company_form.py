from django import forms
from company.models import Company




class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'year_of_start', 'logo']  # Only include fields that actually exist in your model
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'year_of_start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            # 'logo' does not need a widget definition since the default is usually fine, but you can specify if needed.
        }

class CompanyUpdateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'year_of_start', 'logo']  # Adjusted to match the actual model
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'year_of_start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            # Same note on 'logo' as above
        }
