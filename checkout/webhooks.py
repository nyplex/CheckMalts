from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import Order

from checkout.webhooks_handlers import StripeWH_Handler

import stripe
import os
import json
if os.path.exists("env.py"):
    import env
    

@require_POST
@csrf_exempt
def webhook(request):
    print('hhhhheeeeeeellllllooooooo')
    print('hhhhhhhheeeeerrrreeee')
    endpoint_secret = os.environ.get('STRIPE_WH_ENDPOINT_SECRET')
    event = None

    payload = request.body
    sig_header = request.headers['STRIPE_SIGNATURE']

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        raise e
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        raise e
    # Handle the event
    # Set up a webhook handler
    handler = StripeWH_Handler(request)

    # Map webhook events to relevant handler functions
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': handler.handle_payment_intent_payment_failed,
    }

    # Get the webhook type from Stripe
    event_type = event['type']

    # If there's a handler for it, get it from the event map
    # Use the generic one by default
    event_handler = event_map.get(event_type, handler.handle_event)

    # Call the event handler with the event
    response = event_handler(event)
    return JsonResponse({"success": True})