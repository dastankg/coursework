from django.shortcuts import redirect
from django.views.decorators.http import require_POST
from django.views.generic import FormView

from .forms import FeedbackForm
from .models import Subscribe, Feedback


class FeedbackView(FormView):
    template_name = 'contact/contact.html'
    form_class = FeedbackForm
    success_url = '/contact/'
    model = Feedback
    context_object_name = 'contact'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


@require_POST
def subscribe(request):
    sub = Subscribe()
    sub.email = request.POST.get('email')
    sub.save()
    return redirect('homepage')
