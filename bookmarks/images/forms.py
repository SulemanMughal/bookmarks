from django import forms
from .models import Image
# from urllib import request
from urllib.request import Request, urlopen
from django.core.files.base import ContentFile
from django.utils.text import slugify


class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'url', 'description')
        widgets = {
        'url': forms.HiddenInput,
        }

        def clean_url(self):
            url = self.cleaned_data['url']
            valid_extensions = ['jpg', 'jpeg']
            extension = url.rsplit('.', 1)[1].lower()
            if extension not in valid_extensions:
                raise forms.ValidationError('The given URL does not match valid image extensions.')
            return url

    def save(self, force_insert=False, force_update=False, commit=True):
        image = super(ImageCreateForm, self).save(commit=False)
        image_url = self.cleaned_data['url']
        image_name = '{}.{}'.format(slugify(image.title),
        
        image_url.rsplit('.', 1)[1].lower())
        req = Request(
            url=image_url, 
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        # print(image_url)
        # download image from the given URL
        print("form save method")
        response = urlopen(req)

        print("request opened")
        image.image.save(image_name,
        ContentFile(response.read()),
        save=False)
        if commit:
            image.save()
        return image