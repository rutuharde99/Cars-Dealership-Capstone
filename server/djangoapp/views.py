import json

from django.http import JsonResponse
from .models import Dealer
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login_user(request):
    if request.method != "POST":
        return JsonResponse(
            {"status": "error", "message": "POST method required"},
            status=405,
        )

    try:
        data = json.loads(request.body)
    except (json.JSONDecodeError, UnicodeDecodeError):
        return JsonResponse(
            {"status": "error", "message": "Invalid JSON"},
            status=400,
        )

    username = data.get("userName") or data.get("username", "")
    password = data.get("password", "")

    user = authenticate(
        request,
        username=username,
        password=password,
    )

    if user is None:
        return JsonResponse(
            {"status": "error", "message": "Invalid username or password"},
            status=401,
        )

    login(request, user)

    return JsonResponse({
        "userName": user.get_username(),
        "status": "Authenticated",
    })


@csrf_exempt
def logout_user(request):
    from django.contrib.auth import logout

    if request.method != "GET":
        return JsonResponse(
            {"status": "error", "message": "GET method required"},
            status=405,
        )

    logout(request)
    return JsonResponse({"userName": ""})


def get_dealer_reviews(request, dealer_id):
    from django.http import JsonResponse
    from .models import DealerReview

    if request.method != "GET":
        return JsonResponse(
            {"status": "error", "message": "GET method required"},
            status=405,
        )

    reviews = DealerReview.objects.filter(
        dealer_id=dealer_id
    ).order_by("id")

    return JsonResponse({
        "dealer_id": dealer_id,
        "reviews": [
            {
                "reviewer": item.reviewer,
                "review": item.review,
            }
            for item in reviews
        ],
    })


def get_all_dealers(request):
    from .models import Dealer

    if request.method != "GET":
        return JsonResponse(
            {"status": "error", "message": "GET method required"},
            status=405,
        )

    dealers = Dealer.objects.all().order_by("id")

    return JsonResponse({
        "dealers": [
            {
                "id": dealer.id,
                "name": dealer.name,
                "city": dealer.city,
                "state": dealer.state,
                "address": dealer.address,
            }
            for dealer in dealers
        ]
    })


def get_dealer_by_id(request, dealer_id):
    from .models import Dealer
    from django.http import JsonResponse

    if request.method != "GET":
        return JsonResponse({"error": "GET method required"}, status=405)

    try:
        dealer = Dealer.objects.get(id=dealer_id)
    except Dealer.DoesNotExist:
        return JsonResponse({"error": "Dealer not found"}, status=404)

    return JsonResponse({
        "id": dealer.id,
        "name": dealer.name,
        "city": dealer.city,
        "state": dealer.state,
        "address": dealer.address,
    })
from django.http import JsonResponse
from .models import Dealer

def get_dealers_by_state(request, state):
    dealers = Dealer.objects.filter(state__iexact=state)
    data = [
        {
            "id": dealer.id,
            "name": dealer.name,
            "city": dealer.city,
            "state": dealer.state,
            "address": dealer.address,
        }
        for dealer in dealers
    ]
    return JsonResponse({"dealers": data})
def get_dealers_by_state(request, state):
    dealers = Dealer.objects.filter(state__iexact=state)
    data = [
        {
            "id": d.id,
            "name": d.name,
            "city": d.city,
            "state": d.state,
            "address": d.address,
        }
        for d in dealers
    ]
    return JsonResponse({"dealers": data})

def get_all_car_makes(request):
    from django.http import JsonResponse
    makes = [
        {"id": 1, "name": "Audi"},
        {"id": 2, "name": "BMW"},
        {"id": 3, "name": "Ford"},
        {"id": 4, "name": "Honda"},
        {"id": 5, "name": "Toyota"},
    ]
    return JsonResponse({"CarMakes": makes})


@csrf_exempt
def analyze_review(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST method required"}, status=405)

    try:
        data = json.loads(request.body)
        review = data.get("text", "")
    except (json.JSONDecodeError, UnicodeDecodeError):
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    positive_words = ["fantastic", "excellent", "great", "good", "amazing"]
    sentiment = "positive" if any(
        word in review.lower() for word in positive_words
    ) else "neutral"

    return JsonResponse({
        "text": review,
        "sentiment": sentiment
    })
