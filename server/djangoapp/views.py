from django.http import JsonResponse
from django.contrib.auth import login, authenticate
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def login_user(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("userName")
        password = data.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({
                "userName": username,
                "status": "Authenticated"
            })

        return JsonResponse({
            "userName": username,
            "status": "Failed"
        })


@csrf_exempt
def logout_user(request):
    return JsonResponse({
        "userName": ""
    })


def get_dealers(request):
    return JsonResponse({
        "dealers": [
            {"id": 1, "name": "Toyota Dealer", "state": "Kansas"},
            {"id": 2, "name": "Honda Dealer", "state": "Texas"}
        ]
    })


def get_dealer_by_id(request, dealer_id):
    return JsonResponse({
        "id": dealer_id,
        "name": "Toyota Dealer",
        "state": "Kansas"
    })


def get_dealers_by_state(request, state):
    return JsonResponse({
        "dealers": [
            {"id": 1, "name": "Toyota Dealer", "state": state}
        ]
    })


def get_dealer_reviews(request, dealer_id):
    return JsonResponse({
        "dealer_id": dealer_id,
        "reviews": [
            {"review": "Great service", "sentiment": "positive"}
        ]
    })