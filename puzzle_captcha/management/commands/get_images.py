from pyquery import PyQuery
import urllib3
from io import StringIO
from django.core.management.base import BaseCommand
from django.core.files.uploadedfile import SimpleUploadedFile
from puzzle_captcha.models import Puzzle

root_url = 'http://www.public-domain-image.com'


def get_links(url, url_list):
    print
    "Getting images from %s" % url
    subcategory_links = []
    resp = urllib3.urlopen(url)
    page = PyQuery(resp.read())
    subcategory_list = page('#public_domain_images_center_middle .albums .album a')
    if subcategory_list:
        for item in subcategory_list:
            link_url = PyQuery(item).attr('href')
            if link_url not in url_list:
                url_list.append(link_url)
                get_links(link_url, url_list)
            else:
                print
                "Found duplicate %s" % link_url
    elif page('h1 strong img'):
        img_url = page('h1 strong img').attr('src')
        if img_url not in url_list:
            url_list.append(img_url)
            print
            "Found image %s" % img_url
            create_puzzle_from_url(img_url)
        else:
            print
            "Found duplicate %s" % img_url


def create_puzzle_from_url(url):
    img_response = urllib3.urlopen(root_url + url)
    filename = img_response.geturl().split('/')[-1]
    puzzle = Puzzle(key='')
    try:
        puzzle.image.save(filename, SimpleUploadedFile(filename, img_response.read(), content_type='image/jpg'),
                          save=True)
        puzzle.save()
    except Exception as ex:
        puzzle.delete()
        print
        ex


class Command(BaseCommand):
    help = "Pull all scores for each week record"

    def handle_noargs(self, **options):
        # create_puzzle_from_url('http://www.public-domain-image.com/cache/textures-and-patterns-public-domain-images-pictures/tree-bark-cortex-public-domain-images-pictures/trees-amber-sap_w725_h544.jpg')
        # return

        resp = urllib3.urlopen(root_url)
        home = PyQuery(resp.read())
        menu = home('.style6 .menu:first')
        menu_links = []
        for item in menu('a'):
            menu_links.append(PyQuery(item).attr('href'))
        url_list = []
        for menu_item in menu_links:
            get_links(menu_item, url_list)