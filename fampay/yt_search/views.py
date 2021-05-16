from django.db.models import query
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Videos
from django.template import Context, loader
from django.http import HttpResponse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger




def index(request):
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


def pages(request):
    if request.method=='POST':
        global query,type_of_search
        query=request.POST['query']
        type_of_search=request.POST["type_of_search"]
    if type_of_search=='Description':
        post_list=Videos.objects.order_by('-publishedAt').values('title','description','publishedAt','thumbnailsUrls','video_id').filter(description__icontains=query)
    else:
        post_list=Videos.objects.order_by('-publishedAt').values('title','description','publishedAt','thumbnailsUrls','video_id').filter(title__icontains=query)
    paginator = Paginator(post_list, 10)
    page = request.GET.get('page')
    for post in post_list:
        post['video_id']=f"https://www.youtube.com/watch?v={res['video_id']}"
 
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
 
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
    return render(request, 'index.html', {'page':page,'posts':posts})


