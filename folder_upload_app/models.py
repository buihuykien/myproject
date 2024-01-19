# models.py
from django.db import models

def student_upload_path(instance, filename):
    # File will be uploaded to MEDIA_ROOT/student_id/filename
    return f"{instance.student_id}/{filename}"

class Submission(models.Model):
    room_no = models.CharField(max_length=100)
    student_id = models.CharField(max_length=100)
    word_file = models.FileField(upload_to=student_upload_path, blank=True, null=True)
    excel_file = models.FileField(upload_to=student_upload_path, blank=True, null=True)
    python_file = models.FileField(upload_to=student_upload_path, blank=True, null=True)
    compressed_file = models.FileField(upload_to=student_upload_path, blank=True, null=True)
