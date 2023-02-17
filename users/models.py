from django.db import models
from vacancy.models import TYPE_OF_INDUSTRY, MINIMUM_QUALIFICATION, EMPLOYEE_TYPE
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# 3rd-Party
from taggit.managers import TaggableManager
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField


def get_upload_to(instance, filename):
    """Provides a path to upload the profile picture"""
    return f"{instance.created_by.username}/{filename}"


def get_default_image():
    """provides a default profile picture image"""
    return "default/profile_picture.webp"


def model_str_with_username(model_instance):
    """Just returns the UserID and their Username"""
    return f"{model_instance.id}: {model_instance.created_by.username}"


def user_resume_upload_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/resume/<filename>
    return f'user_{instance.user.id}/resume/{filename}'


def user_cover_letter_upload_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/cover_letter/<filename>
    return f'user_{instance.user.id}/cover_letter/{filename}'


class UserProfile(models.Model):
    created_by = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to=get_upload_to, default=get_default_image)
    job_title = models.CharField(max_length=250)
    public_profile = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id}: {self.created_by.username}"


"""
********************* ~ CANDIDATE PROFILE INFORMATION ~ **************************
 """


class CandidateStatement(models.Model):
    created_by = models.OneToOneField(User, on_delete=models.CASCADE, related_name='candidate_statement')
    about = models.TextField(verbose_name='Personal Statement', help_text='Write your professional/about statement here')

    def __str__(self):
        return model_str_with_username(self)


class Education(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='candidate_education')
    institution = models.CharField(max_length=250)
    qualification_type = models.CharField(choices=MINIMUM_QUALIFICATION, max_length=250)
    qualification_title = models.CharField(max_length=250, help_text='Name of the qualification (e.g. BSc Hons in '
                                                                     'Surveying and Geomatics)')
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    additional = models.TextField(help_text='Any additional information about this qualification', blank=True,
                                  null=True)

    def __str__(self):
        return f"{self.institution} - {self.qualification_title} "


class Experience(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='candidate_experience')
    position = models.CharField(max_length=250)
    work_type = models.CharField(choices=EMPLOYEE_TYPE, max_length=250)
    organisation_type = models.CharField(choices=TYPE_OF_INDUSTRY, max_length=250)
    organisation = models.CharField(max_length=250),
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True, help_text='Leave blank if this is your current work-place')
    role_description = models.TextField()  # TODO: Make WYSIWYG Editor

    def __str__(self):
        return f"{self.position} @ {self.organisation}"


class Documents(models.Model):
    created_by = models.OneToOneField(User, on_delete=models.CASCADE, related_name='candidate_document')
    resume = models.FileField(upload_to=user_resume_upload_path, blank=True, null=True)
    cover_letter = models.FileField(upload_to=user_cover_letter_upload_path, blank=True, null=True)

    def __str__(self):
        return model_str_with_username(self)


class Skill(models.Model):
    created_by = models.OneToOneField(User, on_delete=models.CASCADE, related_name='candidate_skill')
    skill = TaggableManager(help_text="Type a skill and separate by comma (,). An example: ArcGIS Suite, QGIS, "
                                      "Microsoft Office...")

    def __str__(self):
        return model_str_with_username(self)


class Interest(models.Model):
    created_by = models.OneToOneField(User, on_delete=models.CASCADE, related_name='candidate_interest')
    interest = TaggableManager(help_text="Type an interest and separate by comma (,). An example: Sporting, Traveling "
                                         "Singing...")

    def __str__(self):
        return model_str_with_username(self)


class Language(models.Model):
    created_by = models.OneToOneField(User, on_delete=models.CASCADE, related_name='candidate_language')
    language = TaggableManager(help_text="Type a language and separate by comma (,) to add more. Example: English, "
                                         "French, Spanish, Russian")

    def __str__(self):
        return model_str_with_username(self)


class Contact(models.Model):
    created_by = models.OneToOneField(User, on_delete=models.CASCADE, related_name='candidate_contact')
    email = models.EmailField(help_text="Make sure to use a personal email that you always have access to")
    location_city = models.CharField(max_length=250)
    location_country = CountryField()
    phone_number = PhoneNumberField(help_text='Always enter with Country-Code')
    linkedin_url = models.URLField(help_text='Paste the profile URL here. A profile url is in the format: '
                                             'https://linkedin.com/in/xxx-xxx')

    def __str__(self):
        return model_str_with_username(self)
