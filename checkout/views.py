from decimal import Decimal

import stripe
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from notes.models import Purchase, StudyNote


@login_required
def create_checkout_session(request, pk):
    note = get_object_or_404(StudyNote, pk=pk, is_active=True)

    if request.method != "POST":
        return redirect(note.get_absolute_url())

    if Purchase.objects.filter(user=request.user, note=note).exists():
        messages.info(request, "You already own this study note.")
        return redirect("notes:purchases")

    if not settings.STRIPE_SECRET_KEY:
        messages.error(
            request,
            "Stripe is not configured. Add your test API keys first.",
        )
        return redirect(note.get_absolute_url())

    stripe.api_key = settings.STRIPE_SECRET_KEY
    success_url = request.build_absolute_uri(reverse("checkout:success"))
    success_url += "?session_id={CHECKOUT_SESSION_ID}"
    cancel_url = request.build_absolute_uri(
        reverse("checkout:cancel", args=[note.pk])
    )

    session = stripe.checkout.Session.create(
        mode="payment",
        customer_email=request.user.email or None,
        line_items=[
            {
                "price_data": {
                    "currency": "gbp",
                    "product_data": {"name": note.title},
                    "unit_amount": int(note.price * Decimal("100")),
                },
                "quantity": 1,
            }
        ],
        metadata={
            "user_id": str(request.user.pk),
            "note_id": str(note.pk),
        },
        success_url=success_url,
        cancel_url=cancel_url,
    )
    return redirect(session.url, code=303)


@login_required
def payment_success(request):
    session_id = request.GET.get("session_id", "")
    if not session_id or not settings.STRIPE_SECRET_KEY:
        messages.error(request, "We could not verify this payment.")
        return redirect("notes:browse")

    stripe.api_key = settings.STRIPE_SECRET_KEY

    try:
        session = stripe.checkout.Session.retrieve(session_id)
    except stripe.error.StripeError:
        messages.error(request, "Stripe could not verify this payment.")
        return redirect("notes:browse")

    user_matches = session.metadata.get("user_id") == str(request.user.pk)
    note_id = session.metadata.get("note_id")

    if session.payment_status != "paid" or not user_matches or not note_id:
        messages.error(request, "Payment has not been confirmed.")
        return redirect("notes:browse")

    note = get_object_or_404(StudyNote, pk=note_id)
    amount_paid = Decimal(session.amount_total or 0) / Decimal("100")

    Purchase.objects.get_or_create(
        user=request.user,
        note=note,
        defaults={
            "stripe_session_id": session.id,
            "amount_paid": amount_paid,
        },
    )

    return render(request, "checkout/success.html", {"note": note})


@login_required
def payment_cancel(request, pk):
    note = get_object_or_404(StudyNote, pk=pk)
    messages.warning(
        request,
        "Payment was cancelled. You have not been charged.",
    )
    return render(request, "checkout/cancel.html", {"note": note})
