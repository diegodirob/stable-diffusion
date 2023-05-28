from django import forms


from stable.vendors.stable_diffusion import StableDiffusion


class StableDiffusionForm(forms.Form):
    prompt = forms.CharField(widget=forms.Textarea(attrs={'rows': '3'}))
    negative_prompt = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': '3'}))

    def get_response(self) -> dict:
        raise NotImplementedError

    def get_image(self) -> dict:
        try:
            response = self.get_response()
        except Exception as e:
            response = {'error': str(e)}
        return {'request_data': self.cleaned_data, 'response_data': response}


class TextToImageForm(StableDiffusionForm):
    def get_response(self) -> dict:
        return StableDiffusion().text_to_image(**self.cleaned_data).json()


class ImageToImageForm(StableDiffusionForm):
    init_image = forms.URLField(required=True)

    def get_response(self) -> dict:
        return StableDiffusion().text_to_image(**self.cleaned_data).json()
