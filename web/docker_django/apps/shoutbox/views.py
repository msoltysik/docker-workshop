from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import Shout
from redis import Redis

redis = Redis(host='redis', port=6379)


def home(request):
    if request.method == 'POST':
        message = request.POST['item_text']
        email = request.POST['email_address']

        Shout.objects.create(text=message, email_address=email)

        send_mail('Mail from Docker', 'Message: {}.'.format(
            message), 'from@docker.workshop', [email, ], fail_silently=False)

        return redirect('/')
    items = Shout.objects.all()
    counter = redis.incr('counter')
    return render(request, 'index.html', {'items': items, 'counter': counter})
