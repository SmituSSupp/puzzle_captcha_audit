import random
import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.template.context import RequestContext
from django.shortcuts import get_object_or_404

from test_captcha.models import Submission
from test_captcha.forms import SubmissionForm


def show_form(request):
    print(f'{datetime.date.today()} -  sess opened')
    form = SubmissionForm(request.POST or None)
    if form.is_valid():
        form.save()
        print(f'{datetime.date.today()} -  sess closed')
        return HttpResponse('Thank you for your feedback!')
    return render(request, 'test_form.html', {'form': form, })


def log_user_image_click(request):
    print('click_happend')
    print(request.POST['cookies'])
    return HttpResponse(status=204)
