from django import forms
from .models import Genre


class AddSong(forms.Form):
    name = forms.CharField( label="Name")
    composer = forms.CharField(label="Composer")
    author = forms.CharField( label="Author")
    description = forms.CharField(widget=forms.Textarea)
    song_url = forms.CharField(label="Spotify link")
    genre = forms.ModelChoiceField(queryset=Genre.objects.all().values_list('name', flat=True), initial=0)
    class Meta:
        models = Genre
        fields = [
            "id", "name","description"
        ]

class SongInfo(forms.Form):
    price = forms.FloatField(label="Price")

    