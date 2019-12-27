from django import forms
from .models import Tags, Posts
from django.core.exceptions import ValidationError

class TagsForm(forms.ModelForm):
    class Meta:
        model = Tags
        fields = ['title']
        #fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
           
        }# 'slug': forms.TextInput(attrs={'class': 'form-control'})
  
    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower() #self.cleaned_data.get('title')
        if new_slug == 'create':
            raise ValidationError('Slug may not be "create"')
        #if Tags.objects.filter(slug__iexact=new_slug).count():
        #    raise ValidationError('Slug mast be unique. We have that slug "{}"'.format(new_slug))
        return new_slug

   
class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'body', 'tags']
        #fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
        #'slug': forms.TextInput(attrs={'class': 'form-control'}),
  
    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower() #self.cleaned_data.get('title')
        if new_slug == 'create':
            raise ValidationError('Slug may not be "create"')
        return new_slug




# class TagsForm(forms.Form):
#     title = forms.CharField(max_length=50)
#     slug = forms.CharField(max_length=50)
#     title.widget.attrs.update({'class': 'form-control'})
#     slug.widget.attrs.update({'class': 'form-control'})

#     def clean_slug(self):
#         new_slug = self.cleaned_data['slug'].lower() #self.cleaned_data.get('title')
#         if new_slug == 'create':
#             raise ValidationError('Slug may not be "create"')
#         if Tags.objects.filter(slug__iexact=new_slug).count():
#             raise ValidationError('Slug mast be unique. We have that slug "{}"'.format(new_slug))
#         return new_slug

#     def save(self):
#         if self.is_valid():
#             new_tag = Tags.objects.create(title=self.cleaned_data['title'],
#                                     slug=self.cleaned_data['slug'])
#             return new_tag
#         else:
#             raise ValidationError('do not valid')

#AttributeError
#ValidationError

# class Tags(models.Model):
#     title = models.CharField(max_length=50)
#     slug = models.SlugField(max_length=50, unique=True)

#     def get_absolute_url(self):
#         return reverse('mainApp:tags_detail_url', kwargs={'slug': self.slug})

#     def __str__(self):
#         return self.title

