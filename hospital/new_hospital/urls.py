from django.urls import path, include
from new_hospital import views

urlpatterns = [
    path('', views.base_page),
    path('main_doctor', views.m_doctor_page),
    path('contacts', views.contact_page),
    path('doctors', views.all_doctors),
    path('doctors/by_age', views.all_doctors_by_age),
    path('doctors/by_sex', views.all_doctors_by_sex),
    path('doctors/by_department', views.all_doctors_by_dep),
    path('doctors/by_exp_less_3', views.all_doctors_by_exp_less_3),
    path('doctors/by_exp_more_3', views.all_doctors_by_exp_more_3),
    path('departments', views.dep_show),
    path('<slug:project_id>', views.doctor_show,name='doctor details'),
    path('department/<slug:project_id>', views.dep_show_id,name='dep show')
]
