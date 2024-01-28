from django.http.response import JsonResponse
from core.tasks import create_random_posts


def post_generator(request):
    create_random_posts.delay()
    return JsonResponse({"success": True})
