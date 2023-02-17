from django.contrib import admin
from .models import Experience, UserProfile, CandidateStatement, Education, Documents, Skill, Interest, Language, \
    Contact

# 3rd-Party
from django_summernote.admin import SummernoteModelAdmin


class ExperienceAdmin(SummernoteModelAdmin):
    list_display = ('position', 'organisation', 'start_date', 'end_date')
    summernote_fields = ('role_description',)


class UserProfileAdmin(admin.ModelAdmin):
    pass


class CandidateStatementAdmin(admin.ModelAdmin):
    pass


class EducationAdmin(admin.ModelAdmin):
    pass


class DocumentsAdmin(admin.ModelAdmin):
    pass


class SkillAdmin(admin.ModelAdmin):
    pass


class InterestAdmin(admin.ModelAdmin):
    pass


class LanguageAdmin(admin.ModelAdmin):
    pass


class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'location_city', 'location_country', 'phone_number', 'linkedin_url')


admin.site.register(Experience, ExperienceAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(CandidateStatement, CandidateStatementAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Documents, DocumentsAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Interest, InterestAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Contact, ContactAdmin)

