from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormView

from stable.forms import TextToImageForm
from stable.models import StableRecord


class StableRecordListView(ListView):
    model = StableRecord
    template_name = 'list.html'
    queryset = StableRecord.objects.order_by('?')


class ResultView(DetailView):
    model = StableRecord
    template_name = 'result.html'

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
        return reverse('stable-result', kwargs={'pk': self.instance.id})
