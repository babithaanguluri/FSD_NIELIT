from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Member


@api_view(['GET', 'POST'])
def hello_api(request):

    if request.method == 'GET':
        return Response({
            "message": "Hello from Django!",
            "method": "GET"
        })

    if request.method == 'POST':

        firstname = request.data.get('firstname')
        lastname = request.data.get('lastname')
        email = request.data.get('email')
        phonenumber = request.data.get('phonenumber')

        member = Member.objects.create(
            firstname=firstname,
            lastname=lastname,
            email=email,
            phonenumber=phonenumber
        )

        return Response({
            "message": "Member created successfully!",
            "data": {
                "id": member.id,
                "firstname": member.firstname,
                "lastname": member.lastname,
                "email": member.email,
                "phonenumber": member.phonenumber
            }
        }, status=status.HTTP_201_CREATED)