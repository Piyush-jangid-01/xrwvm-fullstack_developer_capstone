from django.http import JsonResponse
from django.contrib.auth import login, authenticate
from django.views.decorators.csrf import csrf_exempt
import json

# ---------------- AUTH ----------------

@csrf_exempt
def login_user(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("userName")
        password = data.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({"userName": username, "status": "Authenticated"})

        return JsonResponse({"userName": username, "status": "Failed"})


@csrf_exempt
def logout_user(request):
    return JsonResponse({"userName": ""})


# ---------------- DEALERS ----------------

def fetchDealers(request):
    return JsonResponse({
        "status": 200,
        "dealers": [
            {
                "id": 1,
                "city": "Kansas City",
                "state": "Kansas",
                "zip": "66101",
                "lat": 39.114,
                "long": -94.627,
                "short_name": "Toyota KS",
                "full_name": "Toyota Dealer Kansas"
            },
            {
                "id": 2,
                "city": "Dallas",
                "state": "Texas",
                "zip": "75001",
                "lat": 32.7767,
                "long": -96.7970,
                "short_name": "Honda TX",
                "full_name": "Honda Dealer Texas"
            }
        ]
    })


def fetchDealer(request, dealer_id):
    return JsonResponse({
        "status": 200,
        "dealer": {
            "id": dealer_id,
            "city": "Kansas City",
            "state": "Kansas",
            "zip": "66101",
            "lat": 39.114,
            "long": -94.627,
            "short_name": "Toyota KS",
            "full_name": "Toyota Dealer Kansas"
        }
    })


def fetchDealersByState(request, state):
    return JsonResponse({
        "status": 200,
        "dealers": [
            {
                "id": 1,
                "city": "Kansas City",
                "state": state,
                "zip": "66101",
                "lat": 39.114,
                "long": -94.627,
                "short_name": "Toyota KS",
                "full_name": "Toyota Dealer Kansas"
            }
        ]
    })


# ---------------- REVIEWS ----------------

def fetchReviews(request, dealer_id):
    return JsonResponse({
        "status": 200,
        "reviews": [
            {
                "id": 1,
                "name": "John Doe",
                "dealership": dealer_id,
                "review": "Great service",
                "purchase": True,
                "purchase_date": "2024-01-10",
                "car_make": "Toyota",
                "car_model": "Corolla",
                "car_year": 2022
            }
        ]
    })


# ---------------- CARS ----------------

def get_cars(request):
    return JsonResponse({
        "CarModels": [
            {
                "make": "Toyota",
                "model": "Corolla"
            },
            {
                "make": "Honda",
                "model": "Civic"
            }
        ]
    })


# ---------------- SENTIMENT ----------------

def analyze(request, text):
    return JsonResponse({
        "review": text,
        "sentiment": "positive"
    })