"""thedatalab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.conf.urls.static import static
from frontend import views
from frontend.models import Topic
from frontend.models import Blog
from frontend.models import Paper
from frontend.models import Tool
from frontend.models import Software
from frontend.models import Dataset
from frontend.models import Author


urlpatterns = [
    path('admin/', admin.site.urls),
    path('paper/<slug:slug>/', views.show_thing, {'thing_type': Paper}, name='show_paper'),
    path('blog/<slug:slug>/', views.show_thing, {'thing_type': Blog}, name='show_blog'),
    path('tool/<slug:slug>/', views.show_thing, {'thing_type': Tool}, name='show_tool'),
    path('software/<slug:slug>/', views.show_thing, {'thing_type': Software}, name='show_software'),
    path('dataset/<slug:slug>/', views.show_thing, {'thing_type': Dataset}, name='show_dataset'),
    path('topic/<slug:slug>/', views.show_thing, {'thing_type': Topic}, name='show_topic'),
    path('person/<slug:slug>/', views.show_thing, {'thing_type': Author}, name='show_author'),

    path('papers/', views.thing_index, {'thing_type': Paper}, name='paper_index'),
    path('blogs/', views.thing_index, {'thing_type': Blog}, name='blog_index'),
    path('tools/', views.thing_index, {'thing_type': Tool}, name='tool_index'),
    path('software/', views.thing_index, {'thing_type': Software}, name='software_index'),
    path('datasets/', views.thing_index, {'thing_type': Dataset}, name='dataset_index'),
    path('topics/', views.thing_index, {'thing_type': Topic}, name='topic_index'),
    path('people/', views.thing_index, {'thing_type': Author}, name='author_index'),

    path('imagefit/', include('imagefit.urls')),
    path('markdownx/', include('markdownx.urls')),
]


if settings.DEBUG is True:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)