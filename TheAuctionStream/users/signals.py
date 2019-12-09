from users.models import CustomUser
from django.db.models.signals import post_save
from django.dispatch import receiver
import random, string

ALPHANUMERIC_CHARS = string.ascii_lowercase + string.digits
STRING_LENGHT = 16

@receiver(post_save, sender=CustomUser)
def create_token(sender, instance, created, **kwargs):
    if created:
        instance.token = "".join(random.choice(ALPHANUMERIC_CHARS) for _ in range(STRING_LENGHT))
        instance.save()
