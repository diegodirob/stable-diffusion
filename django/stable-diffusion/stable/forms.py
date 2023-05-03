from django import forms


from stable.vendors.stable_diffusion import StableDiffusion


class TextToImageForm(forms.Form):
    prompt = forms.CharField()  # widget=forms.Textarea)
    negative_prompt = forms.CharField(required=False)  # widget=forms.Textarea)

    def get_image(self) -> dict:
        try:
            response = StableDiffusion().text_to_image(**self.cleaned_data).json()
        except Exception as e:
            response = {'error': str(e)}
        return {
            'request_data': self.cleaned_data,
            'response_data': response
        }
