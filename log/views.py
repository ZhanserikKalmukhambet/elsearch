from django.http import HttpResponse
import logging


def index(request):
    logger = logging.getLogger("signal")
    message = {
        'message': "user visits index()"
    }
    logger.info(message)

    return HttpResponse("hello")
