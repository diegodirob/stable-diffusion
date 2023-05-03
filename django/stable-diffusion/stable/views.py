from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import FormView

from stable.forms import TextToImageForm
from stable.models import StableRecord


class ResultView(DetailView):
    template_name = 'result.html'

    model = StableRecord

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TextToImageFormView(FormView):
    template_name = 'texttoimage.html'
    form_class = TextToImageForm
    instance = None

    def form_valid(self, form):
        self.instance = StableRecord.objects.create(user=self.request.user, **form.get_image())
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('result', kwargs={'pk': self.instance.id})
