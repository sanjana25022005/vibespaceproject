# base/tasks.py
from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from .models import Task

@shared_task
def test_task():
    print("Simple task executed!")

@shared_task
def send_task_reminders():
    now = timezone.now()
    upcoming_tasks = Task.objects.filter(
        due_date__gte=now, due_date__lte=now + timezone.timedelta(days=1), completed=False
    )
    print("Number of tasks found:", upcoming_tasks.count())
    for task in upcoming_tasks:
        send_mail(
            "Reminder: Task Due Soon",
            f"Your task '{task.title}' is due on {task.due_date}.",
            "noreply@vibespace.com",
            ["sanjanavellanki2005@gmail.com"]
        )

