from django.contrib.auth.models import User
from django.db import models
from PIL import Image

# Third-Party Packages
from taggit.managers import TaggableManager
from django_countries.fields import CountryField

YEARS_OF_EXPERIENCE = (
    ('zero', 'No experience required'),
    ('one_to_three', '1 - 3 years'),
    ('four_to_five', '4 - 5 years'),
    ('six_to_ten', '6 - 10 years'),
    ('eleven_plus', '11 + years'),
)

MINIMUM_QUALIFICATION = (
    ('not_required', 'Not Required'),
    ('o_level', 'O - Level'),
    ('a_level', 'A - Level'),
    ('certificate', 'Certificate'),
    ('diploma', 'Diploma'),
    ('bachelor_degree', 'Bachelor Degree'),
    ('masters_degree', 'Masters Degree'),
    ('phd', 'PhD'),
)

TYPE_OF_INDUSTRY = (
    ('private', 'Private'),
    ('government', 'Government'),
    ('ngo', 'NGO'), # Todo: Add more
)

EMPLOYEE_TYPE = (
    ('full_time', 'Full Time'),
    ('part_time', 'Part Time'),
    ('consultant', 'Consultant'),
    ('volunteer', 'Volunteer'),
)

POSITION_TYPE = (
    ('junior', 'junior'),
    ('senior', 'Senior'),
)

NUMBER_OF_EMPLOYEE_RANGE = (
    ('less_than_ten', 'Less than 10'),
    ('eleven_to_hundred', '11 - 100'),
)


class JobCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name='Category Name')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Job Category'


class Company(models.Model):
    name = models.CharField(max_length=250, verbose_name='Company/Organization Name')
    logo = models.ImageField(default='default/company_logo.png', upload_to='company_logo/', blank=True, null=True)
    about_company = models.TextField()
    number_of_staff = models.CharField(max_length=250, choices=NUMBER_OF_EMPLOYEE_RANGE)
    location_street = models.CharField(max_length=250,
                                       help_text='Street Level. Enter the House Number (or Apartment Number) and Street Name',
                                       verbose_name='Address', blank=True, null=True)
    location_city = models.CharField(max_length=250, blank=True, null=True)
    location_country = CountryField()
    year_established = models.DateField(blank=True, null=True)
    website_url = models.URLField(blank=True, null=True)
    linkedin = models.SlugField(blank=True, null=True)
    twitter = models.SlugField(blank=True, null=True)
    facebook = models.SlugField(blank=True, null=True)
    phone_number = models.CharField(max_length=10, help_text='Please include country code. Example: +263776887606')
    # Meta-data
    slug = models.SlugField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Company Information'


class CompanyGallery(models.Model):
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE)
    gallery_image = models.ImageField(upload_to='company_gallery/')  # TODO: Check Database if 4 images exist and
    # restrict
    caption = models.TextField(help_text='Say something about this image')


class CompanyManagement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    is_owner = models.BooleanField(default=False)
    can_edit = models.BooleanField(default=False)
    can_delete = models.BooleanField(default=False)
    can_add_users = models.BooleanField(default=False)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='added_by') # Who added the person?

    def __str__(self):
        return f"{self.user.username} ({self.company.name})"



class Vacancy(models.Model):
    job_title = models.CharField(max_length=250, verbose_name='Title of the Position')
    job_category = models.ForeignKey(JobCategory, on_delete=models.CASCADE, verbose_name='Category')
    employee_type = models.CharField(max_length=250, choices=EMPLOYEE_TYPE)
    position_type = models.CharField(max_length=250, choices=POSITION_TYPE)
    remote_job = models.BooleanField(default=False)
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    job_description = models.TextField(help_text='Give a general overview of the job')
    responsibility = models.TextField()
    minimum_qualification = models.CharField(max_length=250, choices=MINIMUM_QUALIFICATION)
    qualification = models.TextField()
    skill_experience = models.TextField()
    years_of_experience = models.CharField(max_length=250, choices=YEARS_OF_EXPERIENCE,
                                           verbose_name='Minimum Years of Experience')
    location_city = models.CharField(max_length=250, blank=True, null=True,
                                     help_text='OPTIONAL: If applicable to the opportunity', verbose_name='City')
    location_country = CountryField()
    tags = TaggableManager()
    how_to_apply = models.TextField(
        help_text='Explain the hiring process. Links, Emails and documents that should be sent can be explained here')
    external_link = models.URLField(verbose_name='Link to Source',
                                    help_text='If this job was copied from another site, paste the original URL here')
    due_date = models.DateField(help_text='Date when this listing is set to expire', null=True, blank=True)
    # Metadata
    slug = models.SlugField()
    posted_on = models.DateTimeField(auto_created=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.job_title

    class Meta:
        verbose_name = 'Vacancy Information'
