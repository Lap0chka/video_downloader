from celery import shared_task
from django.conf import settings
from django.core.cache import cache
from django.core.mail import send_mail


@shared_task
def send_email_verification(username, email, confirm_link, token):
    redis_key = settings.MYVARRIABLE_USER_CONFIRMATION_KEY.format(token=token)
    cache.set(redis_key, {'user_name': username}, timeout=settings.MYVARRIABLE_USER_TIMEOUT_KEY)
    message = f'Thank you for registration : {username}\n' \
              f'Please follow this link\n' \
              f'{confirm_link}'
    subject = 'Confirm email'
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
