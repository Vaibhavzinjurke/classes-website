from django.urls import path
from myaccount.views import *
urlpatterns = [
    path ("login/", login, name="login" ),
    path ("dashboard/",dashboard, name="dashboard" ),
    path ("logout/",logout, name="logout" ),
    path ("record/<id>",single_student_record, name="record" ),
    path ("delete/<id>",delete, name="delete" ),
    
]
