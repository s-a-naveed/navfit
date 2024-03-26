from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.cache import cache


@receiver(user_logged_in, sender=User)
def getip(sender, request, user, **kwargs):
    ct = cache.get('count', 0, version=user.pk)
    newct = ct + 1
    cache.set('count', newct, 60*60*24, version=user.pk)
    # print('-'*50)
    # print('IP tracked successfully... Here is your ip')
    # ip = request.META.get('REMOTE_ADDR')
    # print('Your IP is: ', ip)
    # request.session['ip'] = ip