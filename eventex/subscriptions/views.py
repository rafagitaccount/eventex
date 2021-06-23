from eventex.subscriptions.mixins import EmailCreateView
from django.views.generic.detail import DetailView
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


new = EmailCreateView.as_view(model=Subscription,
                              form_class=SubscriptionForm,
                              email_subject='Confirmação de Inscrição')

detail = DetailView.as_view(model=Subscription)
