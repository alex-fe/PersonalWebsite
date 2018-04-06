from django.shortcuts import render

from personal_site import personal_info as pi


def main_view(request):
    """Get about_me_txt and pass to template."""
    with open(pi.path_to_about_me_txt, 'r', encoding='utf-8') as file_:
        context = {'about_me_txt' : file_.read()}
        return render(request, 'aboutme/main.html', context)
