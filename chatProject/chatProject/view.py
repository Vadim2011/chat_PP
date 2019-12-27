from django.shortcuts import redirect


def redirect_blog(request):
    return redirect('mainApp:posts_list', permanent=True)
# permanent=True