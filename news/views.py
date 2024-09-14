from rest_framework import generics
from .models import Article
from .serializer import ArticleSerializer
from rest_framework.views import APIView,Response
import requests

#get all datas(news) from DB
class ArticleListView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

# fetch data using ur and store it to the DB
class RetrieveNews(APIView):
    def get(self,request):
        url = 'https://newsapi.org/v2/everything?q={query}&apiKey=3b6daad44fb1444490134f5524c66cc5'
        response = requests.get(url).json()
        print(type(response))
        for item in response['articles']:
            Article.objects.create(
                title=item['title'],
                description=item['description'],
                url=item['url'],
                published_at=item['publishedAt'],
                source_name=item['source']['name']
            )
        print(response)
        return Response({'data':response})
    
# fetch data by title
class GetByTitle(APIView):
    def post(self,request):
        title= request.data.get('title')
        query = Article.objects.filter(title=title)
        serializer = ArticleSerializer(query,many=True)
        return Response({'data':serializer.data})

