from django.contrib import admin
from vacancy.models import Vacancy, JobCategory, Company, CompanyGallery

# Third-Party Packages
from django_summernote.admin import SummernoteModelAdmin


class VacancyAdmin(SummernoteModelAdmin):
    list_display = ('job_title', 'job_category', 'employee_type', 'position_type')
    prepopulated_fields = {'slug': ('job_title', 'job_category', 'employee_type')}
    summernote_fields = ('responsibility', 'qualification', ' skill_experience', 'how_to_apply')


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'about_company', 'website_url')


class JobCategoryAdmin(admin.ModelAdmin):
    pass


class CompanyGalleryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(JobCategory, JobCategoryAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(CompanyGallery, CompanyGalleryAdmin)