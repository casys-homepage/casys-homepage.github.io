import os
from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse
from .models import *

path = Path()

def index(request):
    return render(request, 'index.html')

def members(request):
    members = Members(path)
    alumni, postdoc, phd, ms = members.get_member_list()
    return render(request, 'members.html', {"postdoc": postdoc, "phd": phd, "ms": ms, "alumni": alumni})

def album(request):
    album = Album(path)
    return render(request, 'album.html', {"members_photo_li": album.get_photo_list})

def research(request):
    return render(request, 'research.html')

def publications(request):
    publications = Publications(path)
    all_pub = publications.get_all()
    international_conference = publications.get_international_conference()
    international_journal = publications.get_international_journal()
    domestic_conference = publications.get_domestic_conference()
    domestic_journal = publications.get_domestic_journal()
    return render(request, 'publications.html',
                  {"all_pub": all_pub,
                   "international_conference": international_conference,
                   "international_journal": international_journal,
                   "domestic_conference": domestic_conference,
                   "domestic_journal": domestic_journal})

def projects(request):
    projects = Projects(path)
    past_projects = projects.get_past_projects()
    ongoing_projects = projects.get_ongoing_projects()
    return render(request, 'projects.html',
                  {"ongoing_projects": ongoing_projects,
                   "past_projects": past_projects})
    
def contact(request):
    return render(request, 'contact.html')

def personal(request, *args):
    person_name = ""
    page_name = ""

    arg_num = len(args)
    if arg_num == 1:
        person_name = args[0]
    elif arg_num == 2:
        person_name = args[0]
        page_name = args[1]

    if arg_num == 1:
        template_path = "personal/%s/index.html" % (person_name)
    elif arg_num == 2:
        template_path = "personal/%s/%s" % (person_name, page_name)

    full_template_path = "%s/%s" % (path.templates(), template_path)
    if os.path.exists(full_template_path):
        return render(request, template_path)
    else:
        redirect_html ="""
        <meta http-equiv="refresh" content="0; url=http://calab.kaist.ac.kr:8080/~%s/"/>
        """ % (person_name)
        return HttpResponse(redirect_html)

def redirect_to_personal_page(request, person_name):
    redirect_html ="""
    <meta http-equiv="refresh" content="0; url=./~%s/"/>
    """ % (person_name)
    return HttpResponse(redirect_html)

def papers(request, paper_name):
    fsock = open(path.papers() + paper_name, 'r')
    response = HttpResponse(fsock, content_type='application/pdf')
    response['Content-Disposition'] = 'inline;filename=%s' % (paper_name)
    return response

def google_validation(request):
    return render(request, 'google69fb8370d742f02f.html')
