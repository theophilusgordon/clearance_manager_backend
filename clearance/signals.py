from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Student, Department, DepartmentClearance
from django.utils import timezone

@receiver(post_save, sender=Student)
def create_department_clearance(sender, instance, created, **kwargs):
    if created:
        departments = Department.objects.all()
        for department in departments:
            DepartmentClearance.objects.create(
                clearance_start_date=timezone.now(),  # Use the current time or another appropriate field
                description=f"Clearance for {instance.full_name}",
                department=department,
                user=instance,
                status='pending'
            )