from django import forms

class SearchForm(forms.Form):
    SEARCH_OPTIONS = (
        ('usernames', 'Usernames'),
        ('teams', 'Teams'),
        ('posts', 'Posts'),
        ('posts_related_to_user', 'Posts Related to User'),
    )

    search_option = forms.ChoiceField(choices=SEARCH_OPTIONS)
    search_query = forms.CharField(max_length=100)

