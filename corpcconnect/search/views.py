from django.shortcuts import render
#from .models import SearchUser, SearchPost
from .forms import SearchForm
from Login.models import CustomUser as SearchUser
from posts.models import Post as SearchPost


def search(request):
    form = SearchForm()
    return render(request, 'search/search.html', {'form': form})

def search_results(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search_option = form.cleaned_data['search_option']
            keyword = form.cleaned_data['search_query']
            # Perform search based on selected option and keyword
            if search_option == 'usernames':
                users = SearchUser.objects.filter(username__icontains=keyword)
                print(users, keyword)
                for user in users:
                    print(user.user_id)
                return render(request, 'search/search_results.html', {'users': users})
            elif search_option == 'teams':
                users = SearchUser.objects.filter(user__team__icontains=keyword)
                return render(request, 'search/search_results.html', {'users': users})
            elif search_option == 'posts':
                posts = SearchPost.objects.filter(post__abstract__icontains=keyword)
                return render(request, 'search/search_results.html', {'posts': posts})
            elif search_option == 'posts_user':
                posts = SearchPost.objects.filter(post__author__username__icontains=keyword)
                return render(request, 'search/search_results.html', {'posts': posts})
    return render(request, 'search/search.html', {'form': form})

