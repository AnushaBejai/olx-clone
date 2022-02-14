from django import forms
from .models import *


#class PostForm(forms.ModelForm):
    
    #class Meta:
        #model = Product
        #fields=['name', 'description', 'conditon', 'category','brand', 'price', 'image']
        #labels={
            #'description': 'Write a short summary of your product.',
            #'image': 'Choose an image that can be highlighted.',
        #}

#class AddImagesForm(forms.ModelForm):
    #class Meta:
        #model=ProductImages
        #fields=['image']
        

class PostForm(forms.ModelForm):
    class Meta:
        model = Product
        fields =['name', 'description', 'conditon', 'category','brand', 'price', 'image']
        labels={
            'description': 'Write a short summary of your product.',
            'image': 'Choose an image that can be highlighted.',
        } 

class PostFullForm(PostForm): #extending form
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta(PostForm.Meta):
        fields = PostForm.Meta.fields + ['images',]
        help_texts={
            
            'image': 'In the next image row upload multiple images to showcase your product.',
        } 
        