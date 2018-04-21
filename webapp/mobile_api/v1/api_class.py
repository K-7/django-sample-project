import json

from django.http import JsonResponse
from django.contrib.auth import authenticate, login


class Apiv1():
    def login(self, request):
        return_obj = {}
        try:
            params = json.loads(request.body)
            username = params.get("username", None)
            password = params.get("password", None)

            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return_obj.update(user.to_json)
                status = 200
            else:
                status, return_obj['message'] = 401, 'Invalid Credentials'
        except Exception as ex:
            status, return_obj['message'] = 401, ex

        return JsonResponse(data=return_obj, status=status)
