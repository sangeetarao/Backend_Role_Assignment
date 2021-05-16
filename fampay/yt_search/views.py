from django.db.models import query
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Videos
from django.template import Context, loader
from django.http import HttpResponse
import schedule
import time




def index(request):

    if request.method=='POST':
        query=request.POST['query']
        if request.POST['type_of_search']=='Title':
            results=Videos.objects.order_by('-publishedAt').values('title','description','publishedAt','thumbnailsUrls','video_id').filter(title__icontains=query)
        else:
            results=Videos.objects.order_by('-publishedAt').values('title','description','publishedAt','thumbnailsUrls','video_id').filter(description__icontains=query)
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


    from apiclient.discovery import build
    api_key="AIzaSyBjDOWFZwkxzgAPeybtNOUvKOvTN_Q8MQM"
    youtube = build('youtube','v3',developerKey=api_key)

    res=youtube.search().list(q="Learn python",
                            part='snippet',
                            type='video',
                            order='date',
                            maxResults=5).execute()
    for item in res['items']:
        video_id = item['id']['videoId']
        publishedDateTime = item['snippet']['publishedAt']
        title = item['snippet']['title']
        description = item['snippet']['description']
        thumbnailsUrls = item['snippet']['thumbnails']['default']['url']
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
    return render(request,'home.html')

