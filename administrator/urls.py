"""project_FDG URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='admin/login.html', redirect_authenticated_user=True)),
    path('logout/', auth_views.LogoutView.as_view()),
    path('schemas/', views.schema_view, name="schema_base"),
    path('new_schema/', views.new_schema, name="new_schema"),
    path('data_sets/', views.submit_schema, name="submit_schema"),
    path('data_sets/<int:schema_pk>/', views.data_set_view, name="data_set_view"),
    path('edit_schema/', views.edit_schema, name="edit_schema"),
    path('delete_schema/', views.delete_schema, name="delete_schema"),
    path('add_column/', views.add_column, name="add_column"),
    path('delete_column/', views.delete_column, name="delete_column"),
    path('download/', views.download_data_set, name="download_data_set"),
]
