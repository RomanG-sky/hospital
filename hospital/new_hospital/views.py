from django.shortcuts import HttpResponse, render, get_object_or_404, HttpResponseRedirect, get_list_or_404
from new_hospital.models import Doctor, Profession, Medical_speciality, Hospital
from django.core.paginator import Paginator
from django.db.models import Q

def base_page(request):
    queryset = Doctor.objects.all()
    queryset2 = Hospital.objects.all()
    queryset3 = Medical_speciality.objects.all()
    context = {
        'title': 'st. Andrew hospital',
        'object_listD': queryset,
        'object_listH': queryset2,
        'object_listM': queryset3,

        'filter': 'House',
    }
    return render(request, 'base_clinic.html', context)


def doctor_show(request, project_id):
    instance = get_object_or_404(Doctor, slug=project_id)
    context = {
        'title': 'Doctor detail',
        'object_listD': instance
    }
    return render(request, 'doctor_show.html', context)

def dep_show(request):
    queryset = Medical_speciality.objects.all()
    context = {
        'title': 'Department',
        'objectM': queryset,
    }
    return render(request, 'departments.html', context)


def dep_show_id(request, project_id):
    instance = get_object_or_404(Medical_speciality, slug=project_id)
    queryset2 = Hospital.objects.all()
    context = {
        'title': 'Doctors',
        'object': instance,
        'objectD': queryset2
    }
    return render(request, 'doctors_dep.html', context)

def contact_page(request):
    context = {
        'title': 'Contacts',
    }
    return render(request, 'contact_page.html', context)

def m_doctor_page(request):
    queryset = Doctor.objects.all()
    context = {
        'title': 'Main doctor',
        'object_listD': queryset,
        'filter': 'm. dr.',
    }
    return render(request, 'main_doctor.html', context)


def all_doctors(request):
    queryset = Hospital.objects.all()
    paginator = Paginator(queryset, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'title': 'Doctors',
        'object': page_obj,

    }
    return render(request, 'doctors.html', context)


def all_doctors_by_age(request):
    queryset = Hospital.objects.order_by('doctor__date_of_birth')
    paginator = Paginator(queryset, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'title': 'Doctors',
        'object': page_obj,

    }
    return render(request, 'doctors.html', context)

def all_doctors_by_sex(request):
    queryset = Hospital.objects.order_by('-doctor__sex')
    paginator = Paginator(queryset, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'title': 'Doctors',
        'object': page_obj,

    }
    return render(request, 'doctors.html', context)
def all_doctors_by_dep(request):
    queryset = Hospital.objects.order_by('hospital_department')
    paginator = Paginator(queryset, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'title': 'Doctors',
        'object': page_obj,

    }
    return render(request, 'doctors.html', context)
def all_doctors_by_exp_less_3(request):
    queryset = Hospital.objects.filter(doctor__experience__range=['0','2'])
    paginator = Paginator(queryset, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'title': 'Doctors',
        'object': page_obj,

    }
    return render(request, 'doctors.html', context)

def all_doctors_by_exp_more_3(request):
    queryset = Hospital.objects.filter(doctor__experience__range=['3','99'])
    paginator = Paginator(queryset, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'title': 'Doctors',
        'object': page_obj,

    }
    return render(request, 'doctors.html', context)

#
# def author_add(request):
#     form = AuthorForm(request.POST  or None)
#
#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.save()
#         return HttpResponseRedirect('http://127.0.0.1:8000/shop/author/')
#
#
#     context = {
#         'title': 'AUTHOR CREATE ',
#         'form': form
#
#     }
#     return render(request, 'author_add.html',context)
