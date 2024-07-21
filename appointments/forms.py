from django import forms
from searchS.models import Medicine
from searchS.models import Hospital

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = '__all__'

class LabForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = '__all__'
