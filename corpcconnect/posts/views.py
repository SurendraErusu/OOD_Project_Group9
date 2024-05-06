from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import FileResponse, JsonResponse, HttpResponse
from .models import Profile, Post, Document
from Login.models import CustomUser

@login_required
def get_profile(request):
    user_id = str(request.user.user_id)
    return redirect('/posts/user/'+user_id)
@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile = get_object_or_404(Profile, user=request.user)
        profile.bio = request.POST.get('bio')
        profile.profile_picture = request.FILES.get('profile_picture')
        profile.save()
        return redirect('posts:get_profile')

    return render(request, 'posts/edit_profile.html')

@login_required
def get_posts(request, user_id):
    if str(request.user.user_id) == user_id:
        posts = Post.objects.filter(author=request.user)
    else:
        user = CustomUser.objects.filter(user_id = user_id)[0]
        posts = Post.objects.filter(author=user)

    return render(request, 'posts/user_posts.html', {'posts': posts})

@login_required
def create_post(request):
    if request.method == 'POST':
        author = request.user
        abstract = request.POST.get('abstract')
        document = request.FILES.get('document')
        access_level = request.POST.get('access_level')
        access_teams = request.POST.get('access_teams')

        new_document = Document.objects.create(pdf_file=document)

        post = Post.objects.create(
            author=author,
            abstract=abstract,
            document=new_document,
            access_level=access_level,
            access_teams=access_teams
        )
        return redirect(reverse('posts:user_posts', args=[str(author.user_id)]))

    return render(request, 'posts/create_post.html')  # Create a template for the form

def view_pdf(request, document_id):
    document = get_object_or_404(Document, pk=document_id)
    return FileResponse(document.pdf_file, as_attachment=False)



def like_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.likes += 1
    post.save()
    #return JsonResponse(post)
    return HttpResponse(post.likes)
def dislike_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.dislikes += 1
    post.save()
    return HttpResponse(post.dislikes)

