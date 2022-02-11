from rest_framework import serializers
from .models import Artile

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artile
        #fields = ['id', 'title', 'article']
        fields = '__all__'