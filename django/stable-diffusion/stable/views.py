from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormView

from stable.forms import TextToImageForm, ImageToImageForm
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


class StableFormView(FormView):
    available_form_choices = {
        'text-to-image': TextToImageForm,
        'image-to-image': ImageToImageForm,
    }
    template_name = 'texttoimage.html'
    instance = None

    def get_form_class(self, *args, **kwargs):
        choice = self.request.resolver_match.kwargs.get('service', 'text-2-image')
        return self.available_form_choices.get(choice, TextToImageForm)

    def form_valid(self, form):
        self.instance = StableRecord.objects.create(user=self.request.user, **form.get_image())
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('stable-result', kwargs={'pk': self.instance.id})
