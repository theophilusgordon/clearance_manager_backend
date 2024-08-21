# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Student, DepartmentClearance

@receiver(post_save, sender=Student)
def create_department_clearance(sender, instance, created, **kwargs):
    if created:
        DepartmentClearance.objects.create(
            clearance_start_date=instance.date_joined,  # Assuming `date_joined` is a field in Student
            description=f"Clearance for {instance.full_name}",
            department=instance.department,
            user=instance,
            status='pending'
        )