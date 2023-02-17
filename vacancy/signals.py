from django.db.models.signals import post_save
from django.dispatch import receiver

from vacancy.models import CompanyManagement, Company


@receiver(post_save, sender=Company)
def create_company_management(sender, instance, created, **kwargs):
    """
    Create a CompanyManagement object when a new Company object is created
    and add the user that created the company as the first user with full permissions.
    """
    if created:
        company_management = CompanyManagement(
            user=instance.created_by,
            company=instance,
            is_owner=True,
            can_edit=True,
            can_delete=True,
            can_add_users=True,
            added_by=instance.created_by
        )
        company_management.save()
