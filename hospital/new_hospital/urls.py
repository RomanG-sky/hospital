from django.urls import path, include
from new_hospital import views

urlpatterns = [
    path('', views.base_page),
    path('main_doctor', views.m_doctor_page),
    path('contacts', views.contact_page),
    path('doctors', views.all_doctors),
    path('departments', views.dep_show),
    path('<slug:project_id>', views.doctor_show,name='doctor details'),
    path('department/<slug:project_id>', views.dep_show_id,name='dep show')
]
