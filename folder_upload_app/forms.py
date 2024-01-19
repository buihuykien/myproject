# forms.py
from django import forms
from .models import Submission

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['room_no', 'student_id', 'word_file', 'excel_file', 'python_file', 'compressed_file']
