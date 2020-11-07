import random
import datetime
import logging
import os

from django.http import HttpResponse
from django.shortcuts import render
from django.template.context import RequestContext
from django.shortcuts import get_object_or_404

from test_captcha.models import Submission
from test_captcha.forms import SubmissionForm

logger = logging.getLogger('django.base.log')


def show_form(request):
    print(f"{datetime.date.today()} -  sess  {request.headers['Cookie'].split('; ')[1]} opened.")
    logger.info(f"{datetime.date.today()} -  sess {request.headers['Cookie'].split('; ')[1]} opened.")
    form = SubmissionForm(request.POST or None)
    if form.is_valid():
        form.save()
        print(f'{datetime.date.today()} -  sess closed')
        logger.info(f'{datetime.date.today()} -  sess closed')
        return HttpResponse('Thank you for your feedback!')
    return render(request, 'test_form.html', {'form': form, })


def log_user_image_click(request):
    print('click_happend aaaaa')
    print(request.POST['item_text'])
    print(request.headers['Cookie'].split('; ')[1])
    logger.info(f"click_happend from sess {request.headers['Cookie'].split('; ')[1]}")
    return HttpResponse(status=204)
