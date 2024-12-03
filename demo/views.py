from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from demo.models import User
from demo.serializers import UserSerializer

# Create your views here.

@csrf_exempt
def user_route(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        # TODO: Implement creating a new user
        name = data.get("name")
        username = data.get("username")
        balance = data.get("balance", 0.0)
        user = User.objects.create(name=name, username=username, balance=balance)
        #try: 

        #if name, username, balance do not exist, error message

        #need to return something, also define serializor for the user just created and return as json

        #task 2: request and also have id 
        #try: 
            #user = user....get... 
        #if fail: 
            #serializor 
            #return 

        

    
@csrf_exempt
def transaction_route(request):
    # TODO: EXTRA CREDIT: Get all of a user's transactions
    pass