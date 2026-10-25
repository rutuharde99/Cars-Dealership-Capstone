import json

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

    username = data.get("username", "")
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
        "status": "success",
        "message": "Login successful",
        "username": user.get_username(),
    })


@csrf_exempt
def logout_user(request):
    from django.contrib.auth import logout

    if request.method != "POST":
        return JsonResponse(
            {"status": "error", "message": "POST method required"},
            status=405,
        )

    logout(request)

    return JsonResponse({
        "status": "success",
        "message": "Logout successful",
    })
