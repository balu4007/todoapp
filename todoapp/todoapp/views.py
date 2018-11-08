from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def api_root(request, format=None):
    return Response(
        {
            'admin': reverse('todos:list', request=request, format=format),
            'api': reverse('users:list', request=request, format=format)
        }
    )
