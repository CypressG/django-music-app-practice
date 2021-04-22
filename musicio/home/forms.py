from django import forms
from .models import Genre


class AddSong(forms.Form):
    name = forms.CharField( label="Name")
    composer = forms.CharField(label="Composer")
    author = forms.CharField( label="Author")
    description = forms.CharField(widget=forms.Textarea)
    song_url = forms.CharField(label="Spotify link")
    genre = forms.ChoiceField(choices = [])

    def __init__(self, *args, **kwargs):
        super(AddSong, self).__init__(*args, **kwargs)
        self.fields['genre'].choices = [(x.pk, x.name) for x in Genre.objects.all()]

class SongInfo(forms.Form):
    price = forms.FloatField(label="Price")

class Search(forms.Form):
    item = forms.CharField()
