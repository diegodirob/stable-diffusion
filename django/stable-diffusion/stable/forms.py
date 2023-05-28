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

        service = self.cleaned_data.pop('type')
        return {'request_data': self.cleaned_data, 'response_data': response, 'type': service}


class TextToImageForm(StableDiffusionForm):
    type = forms.CharField(widget=forms.HiddenInput(), required=False, initial='text-to-image')

    def get_response(self) -> dict:
        return StableDiffusion().text_to_image(**self.cleaned_data).json()


class ImageToImageForm(StableDiffusionForm):
    init_image = forms.URLField(required=True)
    type = forms.CharField(widget=forms.HiddenInput(), required=False, initial='image-to-image')

    def get_response(self) -> dict:
        return StableDiffusion().text_to_image(**self.cleaned_data).json()
