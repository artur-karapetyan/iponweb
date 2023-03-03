import json

from django.http import HttpResponse


def data_status(data):
    return HttpResponse(
        json.dumps(data),
        status=200,
        content_type='application/json',
    )
