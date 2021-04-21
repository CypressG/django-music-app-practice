from django import forms



class AddSong(forms.Form):
    name = forms.CharField( label="Name")
    composer = forms.CharField(label="Composer")
    author = forms.CharField( label="Author")
    description = forms.CharField(widget=forms.Textarea)
    song_url = forms.CharField(label="Spotify link")

class SongInfo(forms.Form):
    price = forms.FloatField(label="Price")

