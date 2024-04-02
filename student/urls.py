
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from student.views import *
urlpatterns = [
    path ("",home,name="home" ),
    path ("about/",about,name="about" ),
    path ("registration/",registration,name="registration" ),
    path ("python/",python,name="python" ),
    path ("java/",java,name="java" ),
    path ("aws/",aws,name="aws" ),
    path ("placement/",placement,name="placement" ),
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)