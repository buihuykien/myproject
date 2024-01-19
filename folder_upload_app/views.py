# views.py
import os
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import SubmissionForm

def submit_exam(request):
    if request.method == 'POST':
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            # Get data from the form
            room_no = form.cleaned_data['room_no']
            student_id = form.cleaned_data['student_id']

            # Create a folder for the student
            student_folder = os.path.join(settings.MEDIA_ROOT, room_no, student_id)
            os.makedirs(student_folder, exist_ok=True)

            # Handle Method 1: Upload three files
            if form.cleaned_data['word_file']:
                word_file = form.cleaned_data['word_file']
                fs = FileSystemStorage(location=student_folder)
                fs.save(word_file.name, word_file)

            if form.cleaned_data['excel_file']:
                excel_file = form.cleaned_data['excel_file']
                fs = FileSystemStorage(location=student_folder)
                fs.save(excel_file.name, excel_file)

            if form.cleaned_data['python_file']:
                python_file = form.cleaned_data['python_file']
                fs = FileSystemStorage(location=student_folder)
                fs.save(python_file.name, python_file)

            # Handle Method 2: Upload a single compressed file
            if form.cleaned_data['compressed_file']:
                compressed_file = form.cleaned_data['compressed_file']
                fs = FileSystemStorage(location=student_folder)
                fs.save(compressed_file.name, compressed_file)

            return redirect('success')  # Assuming you have a success view

    else:
        form = SubmissionForm()

    return render(request, 'folder_upload_app/submit_exam.html', {'form': form})

# Rest of the views.py file

def success(request):
    return render(request, 'folder_upload_app/success.html')
