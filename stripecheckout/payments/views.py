import stripe
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from stripecheckout import settings


class HomePage(TemplateView) :
    template_name = 'payments/home.html'

class SuccessPage(TemplateView):
    template_name = 'payments/success.html'

class CancelPage(TemplateView):
    template_name = 'payments/cancel.html'

@csrf_exempt
def get_publishable_key(request):
    if request.method == 'GET':
        publishing_key = {'publish_key': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(publishing_key, safe=False)

@csrf_exempt
def create_checkout(request):
    if request.method == 'GET':
        domain_url = 'http://127.0.0.1:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                    # client_reference_id=request.user.id if request.user.is_authenticated else None,
                    success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                    cancel_url=domain_url + 'cancelled/',
                    payment_method_types=['card'],
                    mode='payment',
                    line_items=[
                        {
                            'name': 'White Sneaker Shoe',
                            'quantity': 1,
                            'currency': 'inr',
                            'amount': 215500,
                        }
                    ]
                )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})