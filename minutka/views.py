from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from minutka.models import Review


@csrf_exempt
def post_review(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        text = request.POST.get('text', '')
        review = Review(name=name, text=text)
        review.save()
        return HttpResponse('{"ok": true}', content_type="application/json",)
