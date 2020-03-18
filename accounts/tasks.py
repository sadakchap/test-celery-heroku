from celery import task, shared_task
from django.core.mail import send_mail
from django.conf import settings
import random

@task
def test_mail():
    sub = 'This is subject celery.'
    msg = 'This is message'
    mail_sent = send_mail(sub, msg, settings.EMAIL_HOST_USER, ['taporichap@gmail.com'])
    return mail_sent


@task
def add(x, y):
    print(x+y)
    return x + y


@task
def mul(x, y):
    total = x * (y * random.randint(3, 100))
    print(total)
    return total


@task
def xsum(numbers):
    print(sum(numbers))
    return sum(numbers)
