"""
URL configuration for firstproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
from myapp import views


urlpatterns = [
    path('', views.index, name='index'),
    # path('', views.first, name='first'),
    # path('admin/', admin.site.urls),
    # path('blogs/', views.blogs),
    # path('about/', views.about, include('/about/')),
    # path('/', views.slash, name='/'),
    # path('<slug>/', views.slug, include('/<slug>/')),
    # path('<slug>/comment/', views.slug_comment, include('/<slug>/comment/')),
    # path('create/', views.create, include('/create/')),
    # path('<slug>/update/', views.slug_update, include('/<slug>/update/')),
    # path('<slug>/delete/', views.slug_delete, include('/<slug>/delete/')),
    # path('profile/<username>/', views.profile_username, include('/profile/<username>/')),
    # path('change_password/', views.change_password, include('/change_password/')),
    # path('register/', views.register, include('/register/')),
    # path('login/', views.login, include('/login/')),
    # path('logout/', views.logout, include('/logout/'))
]

