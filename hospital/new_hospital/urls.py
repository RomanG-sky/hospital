from django.urls import path, include
from new_hospital import views

urlpatterns = [
    path('', views.base_page),
    path('main_doctor', views.m_doctor_page),
    path('contacts', views.contact_page),
    path('doctors', views.all_doctors),
    path('doctors/exp[3,100]', views.all_doctors_exp3andmore),
    path('doctors/exp[0,3]', views.all_doctors_explessthan3),
    path('doctors/birth', views.all_doctors_bybd),
    path('doctors/dep', views.all_doctors_by_dep),
    path('departments', views.dep_show),
    path('<slug:project_id>', views.doctor_show,name='doctor details'),
    path('department/<slug:project_id>', views.dep_show_id,name='dep show')
]
