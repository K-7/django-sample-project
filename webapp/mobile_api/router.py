from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def api_router(request, api_version='v1', operation=None):
    mod = __import__('mobile_api.' + str(api_version) + '.api_class',
                     globals(), locals(), ['Api' + str(api_version)])
    if operation:
        version_class = getattr(mod, 'Api' + str(api_version))
        return getattr(version_class(), operation)(request)

    status, return_obj = 401, {'message': 'Requested for Invalid API operation'}
    return JsonResponse(data=return_obj, status=status)

