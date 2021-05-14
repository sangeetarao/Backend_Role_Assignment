from django.shortcuts import render
from django.http import HttpResponse
from .models import Videos
from django.shortcuts import render

# Create your views here.
def index(request):
    from apiclient.discovery import build
    import psycopg2
    api_key="AIzaSyAaaVZeYKQ-CLpi_vGLg6cPuhzxx1CBzQM"
    youtube = build('youtube','v3',developerKey=api_key)

    request=youtube.search().list(q="drivers license",part='snippet',type='video',order='date',maxResults=3).execute()
    list_1=[]
    for i in request['items']:
        post=Videos()
        post.publishedAt=str(i['snippet']['publishedAt'][:10])
        post.title=i['snippet']['title']
        post.thumbnailsUrls=i['snippet']['thumbnails']['default']['url']
        post.description=i['snippet']['description']
        post.save()
        # list_1.append(f'{publishedAt},{title},{thumbnail},{description}')
        # list_1.append(f'{publishedAt},{title}')
    return HttpResponse("Basic Response")

