from django.db import models
from django.urls import reverse

Sex_type = [('MR', "man"), ('MS', "woman")]


class Profession(models.TextChoices):
    main_doctor = 'm. dr.',
    doctor = 'dr.',
    nurse = 'n.',
    intern = 'i.'

    def __str__(self):
        return self.name


class Medical_speciality(models.Model):
    List_specialties_choices = [
        ('Allergy and immunology', 'Allergy and immunology'),
        ('Anesthesiology', 'Anesthesiology'),
        ('Dermatology', 'Dermatology'),
        ('Diagnostic radiology', 'Diagnostic radiology'),
        ('Emergency medicine', 'Emergency medicine'),
        ('Family medicine', 'Family medicine'),
        ('Internal medicine', 'Internal medicine'),
        ('Medical genetics', 'Medical genetics'),
        ('Neurology', 'Neurology'),
        ('Nuclear medicine', 'Nuclear medicine'),
        ('Obstetrics and gynecology', 'Obstetrics and gynecology'),
        ('Ophthalmology', 'Ophthalmology'),
        ('Pathology', 'Pathology'),
        ('Pediatrics', 'Pediatrics'),
        ('Preventive medicine', 'Preventive medicine'),
        ('Psychiatry', 'Psychiatry'),
        ('Radiation oncology', 'Radiation oncology'),
        ('Surgery', 'Surgery'),
        ('Urology', 'Urology'), ]
    slug = models.SlugField(unique=True, db_index=True, max_length=255, verbose_name="URL")
    speciality = models.CharField(choices=List_specialties_choices, blank=False, max_length=50)

    def __str__(self):
        return self.speciality

    def get_absolute_url(self):
        return reverse("dep show", args=[self.slug])


class Doctor(models.Model):
    slug = models.SlugField(unique=True, db_index=True, max_length=255, verbose_name="URL")
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    rang = models.CharField(choices=Profession.choices, max_length=50, default='intern')
    sex = models.CharField(choices=Sex_type, blank=False, max_length=20)
    date_of_birth = models.DateField(blank=False)
    email = models.EmailField(default='123@clinic.com')
    education = models.ManyToManyField('Medical_speciality')
    experience = models.IntegerField(default=0, blank=False)
    photo = models.ImageField(upload_to='static/img', blank=True)

    def __str__(self):
        return '{0} {1} {2} {3} EXP: {4} years '.format(self.rang, self.sex, self.first_name, self.last_name,
                                                        self.experience,
                                                        )

    def get_absolute_url(self):
        return reverse("doctor details", args=[self.slug])


class Hospital(models.Model):
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE)
    hospital_department = models.ManyToManyField('Medical_speciality')
    cabinet = models.TextField(max_length=5, default=111)
    description = models.CharField(max_length=100, blank=True,
                                   help_text='Information about doctor')

    def __str__(self):
        return f'{self.doctor.rang, self.doctor.last_name} added to  {self.hospital_department.all()}  '
