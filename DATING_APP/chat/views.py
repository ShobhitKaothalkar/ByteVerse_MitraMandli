from django.shortcuts import render
from chat.models import Thread
from django.contrib.auth.decorators import login_required


@login_required
def messages_page(request):
    threads = Thread.objects.by_user(user=request.user).prefetch_related('chatmessage_thread').order_by('timestamp')
    # threads = Thread.objects.by_user(user=request.user).prefetch_related('chatmessage_thread')
    context = {
        'Threads' : threads
    }
    return render(request,'chat/messages.html', context)
