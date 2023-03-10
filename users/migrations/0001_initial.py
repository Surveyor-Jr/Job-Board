# Generated by Django 4.1.5 on 2023-02-17 17:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import phonenumber_field.modelfields
import taggit.managers
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0005_auto_20220424_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(default=users.models.get_default_image, upload_to=users.models.get_upload_to)),
                ('job_title', models.CharField(max_length=250)),
                ('public_profile', models.BooleanField(default=False)),
                ('created_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='candidate_skill', to=settings.AUTH_USER_MODEL)),
                ('skill', taggit.managers.TaggableManager(help_text='Type a skill and separate by comma (,). An example: ArcGIS Suite, QGIS, Microsoft Office...', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='candidate_language', to=settings.AUTH_USER_MODEL)),
                ('language', taggit.managers.TaggableManager(help_text='Type a language and separate by comma (,) to add more. Example: English, French, Spanish, Russian', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='candidate_interest', to=settings.AUTH_USER_MODEL)),
                ('interest', taggit.managers.TaggableManager(help_text='Type an interest and separate by comma (,). An example: Sporting, Traveling Singing...', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=250)),
                ('work_type', models.CharField(choices=[('full_time', 'Full Time'), ('part_time', 'Part Time'), ('consultant', 'Consultant'), ('volunteer', 'Volunteer')], max_length=250)),
                ('organisation_type', models.CharField(choices=[('private', 'Private'), ('government', 'Government'), ('ngo', 'NGO')], max_length=250)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, help_text='Leave blank if this is your current work-place', null=True)),
                ('role_description', models.TextField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidate_experience', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.CharField(max_length=250)),
                ('qualification_type', models.CharField(choices=[('not_required', 'Not Required'), ('o_level', 'O - Level'), ('a_level', 'A - Level'), ('certificate', 'Certificate'), ('diploma', 'Diploma'), ('bachelor_degree', 'Bachelor Degree'), ('masters_degree', 'Masters Degree'), ('phd', 'PhD')], max_length=250)),
                ('qualification_title', models.CharField(help_text='Name of the qualification (e.g. BSc Hons in Surveying and Geomatics)', max_length=250)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('additional', models.TextField(blank=True, help_text='Any additional information about this qualification', null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidate_education', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.FileField(blank=True, null=True, upload_to=users.models.user_resume_upload_path)),
                ('cover_letter', models.FileField(blank=True, null=True, upload_to=users.models.user_cover_letter_upload_path)),
                ('created_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='candidate_document', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(help_text='Make sure to use a personal email that you always have access to', max_length=254)),
                ('location_city', models.CharField(max_length=250)),
                ('location_country', django_countries.fields.CountryField(max_length=2)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(help_text='Always enter with Country-Code', max_length=128, region=None)),
                ('linkedin_url', models.URLField(help_text='Paste the profile URL here. A profile url is in the format: https://linkedin.com/in/xxx-xxx')),
                ('created_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='candidate_contact', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CandidateStatement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(help_text='Write your professional/about statement here', verbose_name='Personal Statement')),
                ('created_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='candidate_statement', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
