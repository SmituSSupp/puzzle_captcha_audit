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


def index(request):

    try:
        # print(request.headers['Cookie'].split('; ')[1])
        ipaddr = request.META.get('REMOTE_ADDR')
        if ipaddr:
            logger.info(f"{datetime.date.today()} {datetime.datetime.now().strftime('%H:%M:%S.%f')[:-4]} Session opened from {ipaddr} agent - {request.headers['User-Agent']} "
                        f"on item page index")
        else:
            logger.info(f"{datetime.date.today()} {datetime.datetime.now().strftime('%H:%M:%S.%f')[:-4]} Session opened from {request.headers['Host']} agent - "
                        f"{request.headers['User-Agent']} on page index")

    except Exception as e:
        logger.info('Cookie error check it')
        logger.info(request.META)
        logger.info(request.headers)

    return render(request, 'frame3.html')


def show_form(request):

    try:
        # print(request.headers['Cookie'].split('; ')[1])
        ipaddr = request.META.get('REMOTE_ADDR')
        if ipaddr:
            logger.info(f"{datetime.date.today()} {datetime.datetime.now().strftime('%H:%M:%S.%f')[:-4]} Session opened from {ipaddr} agent - {request.headers['User-Agent']} "
                        f"on page captcha")
        else:
            logger.info(f"{datetime.date.today()} {datetime.datetime.now().strftime('%H:%M:%S.%f')[:-4]} Session opened from {request.headers['Host']} agent - "
                        f"{request.headers['User-Agent']} on page captcha")

    except Exception as e:
        logger.info('Cookie error check it')
        logger.info(request.META)
        logger.info(request.headers)

    form = SubmissionForm(request.POST or None)

    if form.is_valid():

        try:
            # print(request.headers['Cookie'].split('; ')[1])
            ipaddr = request.META.get('REMOTE_ADDR')
            if ipaddr:
                logger.info(f"{datetime.date.today()} {datetime.datetime.now().strftime('%H:%M:%S.%f')[:-4]} Session closed from {ipaddr} agent - {request.headers['User-Agent']} "
                            f"on page captcha")
            else:
                logger.info(f"{datetime.date.today()} {datetime.datetime.now().strftime('%H:%M:%S.%f')[:-4]} Session closed from {request.headers['Host']} agent - "
                            f"{request.headers['User-Agent']} on page captcha")

        except Exception as e:
            logger.info('Cookie error check it')
            logger.info(request.META)
            logger.info(request.headers)

        return HttpResponse('Thank you for your feedback!')

    return render(request, 'test_form.html', {'form': form, })


def log_user_image_click(request):
    item_tag = request.POST['item_text']

    try:
        #print(request.headers['Cookie'].split('; ')[1])
        ipaddr = request.META.get('REMOTE_ADDR')
        if ipaddr:
            logger.info(f"{datetime.date.today()} {datetime.datetime.now().strftime('%H:%M:%S.%f')[:-4]} click from sess {ipaddr} agent - {request.headers['User-Agent']} "
                        f"on item {item_tag}")
        else:
            logger.info(f"{datetime.date.today()} {datetime.datetime.now().strftime('%H:%M:%S.%f')[:-4]} click from sess {request.headers['Host']} agent - "
                        f"{request.headers['User-Agent']} on item {item_tag}")

    except Exception as e:
        logger.info('Cookie error check it')
        logger.info(request.META)
        logger.info(request.headers)

    return HttpResponse(status=204)


def log_index_input(request):
    index_res = request.POST['item_text']

    try:
        #print(request.headers['Cookie'].split('; ')[1])
        ipaddr = request.META.get('REMOTE_ADDR')
        if ipaddr:
            logger.info(f"{datetime.date.today()} {datetime.datetime.now().strftime('%H:%M:%S.%f')[:-4]} Submit values for index from sess {ipaddr} agent - {request.headers['User-Agent']} "
                        f"are {index_res}")
        else:
            logger.info(f"{datetime.date.today()} {datetime.datetime.now().strftime('%H:%M:%S.%f')[:-4]} Submit values for index from sess {request.headers['Host']} agent - "
                        f"{request.headers['User-Agent']} are {index_res}")

    except Exception as e:
        logger.info('Cookie error check it')
        logger.info(request.META)
        logger.info(request.headers)

    return HttpResponse(status=204)
