from django import forms
from .models import StudentRecord

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentRecord
        fields = "__all__"