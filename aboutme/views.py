from django.shortcuts import render


def main_view(request):
    # FIXME: look up render args
    return render(request, 'aboutme/main.html')
