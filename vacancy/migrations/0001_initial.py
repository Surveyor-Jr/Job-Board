# Generated by Django 4.1.5 on 2023-01-11 18:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0005_auto_20220424_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Company/Organization Name')),
                ('logo', models.ImageField(blank=True, default='default/company_logo.png', null=True, upload_to='company_logo/')),
                ('about_company', models.TextField()),
                ('number_of_staff', models.CharField(choices=[('less_than_ten', 'Less than 10'), ('eleven_to_hundred', '11 - 100')], max_length=250)),
                ('location_street', models.CharField(blank=True, help_text='Street Level. Enter the House Number (or Apartment Number) and Street Name', max_length=250, null=True, verbose_name='Address')),
                ('location_city', models.CharField(blank=True, max_length=250, null=True)),
                ('location_country', django_countries.fields.CountryField(max_length=2)),
                ('year_established', models.DateField(blank=True, null=True)),
                ('website_url', models.URLField(blank=True, null=True)),
                ('linkedin', models.SlugField(blank=True, null=True)),
                ('twitter', models.SlugField(blank=True, null=True)),
                ('facebook', models.SlugField(blank=True, null=True)),
                ('phone_number', models.CharField(help_text='Please include country code. Example: +263776887606', max_length=10)),
                ('slug', models.SlugField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Company Information',
            },
        ),
        migrations.CreateModel(
            name='JobCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Category Name')),
            ],
            options={
                'verbose_name': 'Job Category',
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posted_on', models.DateTimeField(auto_created=True)),
                ('job_title', models.CharField(max_length=250, verbose_name='Title of the Position')),
                ('employee_type', models.CharField(choices=[('full_time', 'Full Time'), ('part_time', 'Part Time'), ('consultant', 'Consultant'), ('volunteer', 'Volunteer')], max_length=250)),
                ('position_type', models.CharField(choices=[('junior', 'junior'), ('senior', 'Senior')], max_length=250)),
                ('remote_job', models.BooleanField(default=False)),
                ('job_description', models.TextField(help_text='Give a general overview of the job')),
                ('responsibility', models.TextField()),
                ('minimum_qualification', models.CharField(choices=[('not_required', 'Not Required'), ('o_level', 'O - Level'), ('a_level', 'A - Level'), ('certificate', 'Certificate'), ('diploma', 'Diploma'), ('bachelor_degree', 'Bachelor Degree'), ('masters_degree', 'Masters Degree'), ('phd', 'PhD')], max_length=250)),
                ('qualification', models.TextField()),
                ('skill_experience', models.TextField()),
                ('years_of_experience', models.CharField(choices=[('zero', 'No experience required'), ('one_to_three', '1 - 3 years'), ('four_to_five', '4 - 5 years'), ('six_to_ten', '6 - 10 years'), ('eleven_plus', '11 + years')], max_length=250, verbose_name='Minimum Years of Experience')),
                ('location_city', models.CharField(blank=True, help_text='OPTIONAL: If applicable to the opportunity', max_length=250, null=True, verbose_name='City')),
                ('location_country', django_countries.fields.CountryField(max_length=2)),
                ('how_to_apply', models.TextField(help_text='Explain the hiring process. Links, Emails and documents that should be sent can be explained here')),
                ('external_link', models.URLField(help_text='If this job was copied from another site, paste the original URL here', verbose_name='Link to Source')),
                ('due_date', models.DateField(blank=True, help_text='Date when this listing is set to expire', null=True)),
                ('slug', models.SlugField()),
                ('company_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vacancy.company')),
                ('job_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacancy.jobcategory', verbose_name='Category')),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Vacancy Information',
            },
        ),
        migrations.CreateModel(
            name='CompanyGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_image', models.ImageField(upload_to='company_gallery/')),
                ('caption', models.TextField(help_text='Say something about this image')),
                ('company_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacancy.company')),
            ],
        ),
    ]