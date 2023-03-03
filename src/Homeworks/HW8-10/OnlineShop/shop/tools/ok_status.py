import json

from django.http import HttpResponse


def ok_status():
    return HttpResponse(
        json.dumps({"status": "ok"}), status=200, content_type="application/json"
    )