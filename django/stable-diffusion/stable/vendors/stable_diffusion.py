import json
from typing import Optional

import requests
from commons.models import SiteConfiguration


class StableDiffusion:
    url = 'https://stablediffusionapi.com/api/v3'
    text_to_image_path = '/text2img'
    image_to_image_path = '/img2img'
    key = SiteConfiguration.objects.get().stability_api_key

    def text_to_image(self, prompt: str, negative_prompt: Optional[str], **kwargs):
        payload = json.dumps({
            'key': self.key,
            'prompt': prompt, 'negative_prompt': negative_prompt,
            'width': kwargs.get('width', '512'),
            'height': kwargs.get('height', '512'),
            'samples': kwargs.get('samples', '1'),
            'num_inference_steps': kwargs.get('num_inference_steps', '20'),
            'safety_checker': kwargs.get('safety_checker', 'yes'),
            'guidance_scale': kwargs.get('guidance_scale', 7.5),
            'seed': kwargs.get('seed'),
            'webhook': kwargs.get('webhook'),
            'track_id': kwargs.get('track_id'),
        })

        return requests.request(
            'POST',
            url=self.url + self.text_to_image_path,
            headers={'Content-Type': 'application/json'},
            data=payload
        )

    def image_to_image(self, prompt: str, init_image: str, negative_prompt: Optional[str], **kwargs):
        payload = json.dumps({
            'key': self.key,
            'prompt': prompt, 'negative_prompt': negative_prompt,
            'init_image': init_image,
            'width': kwargs.get('width', '512'),
            'height': kwargs.get('height', '512'),
            'samples': kwargs.get('samples', '1'),
            'num_inference_steps': kwargs.get('num_inference_steps', '20'),
            'safety_checker': kwargs.get('safety_checker', 'yes'),
            'guidance_scale': kwargs.get('guidance_scale', 7.5),
            'seed': kwargs.get('seed'),
            'webhook': kwargs.get('webhook'),
            'track_id': kwargs.get('track_id'),
        })

        return requests.request(
            'POST',
            url=self.url + self.image_to_image_path,
            headers={'Content-Type': 'application/json'},
            data=payload
        )
