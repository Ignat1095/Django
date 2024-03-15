from django.shortcuts import render
# Create your views here.
import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    first_page = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Главная страница</title>
        </head>
        <body>
        
        <h1>Главная страница</h1>
        <p> Какая-то главная инфа.
        </p>
        <p> <a href="about">О нас</a>
        </p>
        
        </body>
        </html>
        """
    return HttpResponse(first_page)


def about(request):
    about_us = """ <!doctype html>
               <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <meta name="viewport"
                        content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
                        <meta http-equiv="X-UA-Compatible" content="ie=edge">
                        <title>О нас</title>
                    </head>
                    <body>
                        <h1>
                            Это страница о нас.

                        </h1>		
                    </body>
               </html>"""
    return HttpResponse(about_us)
