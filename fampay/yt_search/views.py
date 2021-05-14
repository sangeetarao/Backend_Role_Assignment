from django.shortcuts import render
from django.http import HttpResponse
from .models import Videos
from django.template import Context, loader
from django.http import HttpResponse
# from django.core.exceptions import FieldDoesNotExist



def index(request):
    from apiclient.discovery import build
    # import psycopg2
    api_key="AIzaSyAaaVZeYKQ-CLpi_vGLg6cPuhzxx1CBzQM"
    youtube = build('youtube','v3',developerKey=api_key)

    res=youtube.search().list(q="Driver's license",part='snippet',type='video',order='date',maxResults=30).execute()
    for item in res['items']:
        video_id = item['id']['videoId']
        publishedDateTime = item['snippet']['publishedAt']
        title = item['snippet']['title']
        description = item['snippet']['description']
        thumbnailsUrls = item['snippet']['thumbnails']['default']['url']
        channel_id = item['snippet']['channelId']
        channel_title = item['snippet']['channelTitle']
        video_id = item['id']['videoId']
        print(title)
        try:
            Videos.objects.get(
                        title=title,
                        description=description,
                        publishedAt=publishedDateTime,
                        thumbnailsUrls=thumbnailsUrls,
                        video_id=video_id
            )
        except:
            Videos.objects.create(
                        title=title,
                        description=description,
                        publishedAt=publishedDateTime,
                        thumbnailsUrls=thumbnailsUrls,
                        video_id=video_id
            )
    results=Videos.objects.order_by('-publishedAt').values('title','description','publishedAt','thumbnailsUrls','video_id').filter(title__icontains='Olivia')
    video_data=[]
    for result in results:
        videos_dict = {
            'title' : result['title'],
            'description': result['description'],
            'publishedAt':result['publishedAt'],
            'thumbnailsUrls':result['thumbnailsUrls'],
            'video_id':f"https://www.youtube.com/watch?v={result['video_id']}"
                    }
        
        video_data.append(videos_dict) 
    context = {
        'videos' : video_data
    }     

    return render(request,'indexpage.html',context)
