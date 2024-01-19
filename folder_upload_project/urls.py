from django.contrib import admin
from django.urls import include, path, re_path
from folder_upload_app.views import submit_exam, success  # Import the success view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('submit_exam/', submit_exam, name='submit_exam'),
    path('success/', success, name='success'),
    re_path(r'^$', submit_exam),  # Redirect root path to submit_exam view
]
