import json

#
from django.http import HttpResponse
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist

#
from ..models import StoreCategory

#
from ..tools.data_status import data_status
from ..tools.ok_status import ok_status


class StoreCategoryView(View):

    @staticmethod
    def get(request):
        categories = StoreCategory.objects.all()
        print(categories)
        data = []
        for category in categories:
            category_data = {
                'id': category.id,
                'name': category.name,
                'picture': request.build_absolute_uri(category.picture.url) if category.picture else None,
            }
            data.append(category_data)
        return data_status(data)

    @staticmethod
    def post(request):
        data = json.loads(request.body)
        category = StoreCategory.objects.create(
            name=data['name']
        )
        category.save()
        return ok_status()

    @staticmethod
    def get_single(request, id):

        try:
            category = StoreCategory.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        return data_status({
            "id": category.id,
            "name": category.name,
            'picture': request.build_absolute_uri(category.picture.url) if category.picture else None,
        })

    @staticmethod
    def delete(request, id):

        try:
            category = StoreCategory.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})

        category.delete()
        return ok_status()

    @staticmethod
    def edit(request, id):

        data = json.loads(request.body)

        try:
            category = StoreCategory.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        if "name" in data:
            category.name = data['name']
        category.save()
        return ok_status()

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return StoreCategoryView.get_single(request, id)
        if request.method == "DELETE":
            return StoreCategoryView.delete(request, id)
        if request.method == "PATCH":
            return StoreCategoryView.edit(request, id)
