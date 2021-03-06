"""bodin_edition URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from aligner.views import home_view, ack_view, chapter_choices

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aligner/', include('aligner.urls'), name='word_list_view'),
    path('acknowledgements/', ack_view, name='acknowledgements'),
    path('chapter_view/',chapter_choices, name='chapter_choices'),
    path('',home_view ,name='home')
]
