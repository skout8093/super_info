from django.views.generic import TemplateView, View
from django.shortcuts import render, get_object_or_404, redirect
from super.models import Publication, Comment
from django.db.models import Q
import requests
from django.core.paginator import Paginator

# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'

    language = 'ru'

    def get_context_data(self, **kwargs):
        language = self.kwargs.get('lang', 'ru')
        publications = Publication.objects.all()
        paginator = Paginator(publications, 20)
        page_number = self.request.GET.get('page', 10)
        page_obj = paginator.get_page(page_number)

        text_data = []
        for publication in Publication.objects.all():
            if language == 'ru':
                text_data.append({
                'title': publication.title,
                'text': publication.text,
                'short_text': publication.short_text,
                'hashtag': publication.hashtag,
                'category': publication.category,
                'image': publication.image,
                'created_date': publication.created_date,
                'id': publication.id,
                })
            else:
                text_data.append({
                'title': publication.title_kg,
                'text': publication.text_kg,
                'short_text': publication.short_text_kg,
                'hashtag': publication.hashtag,
                'category': publication.category,
                'image': publication.image,
                'created_date': publication.created_date,
                'id': publication.id,
                })

        context = {
            "publications": page_obj,
            "text": text_data,
            "language": language
        }

        return context

class ContactView(TemplateView):
    template_name = 'contact.html'

class PubgView(TemplateView):
    template_name = 'publication-detail.html'

    language = 'ru'

    def get_context_data(self, **kwargs):
        language = self.kwargs.get('lang', 'ru')
        publications = Publication.objects.all()


        for publication in Publication.objects.all():
            if language == 'ru' and publication.id == kwargs['pk']:
                text_data = {
                'title': publication.title,
                'text': publication.text,
                'short_text': publication.short_text,
                'hashtag': publication.hashtag,
                'category': publication.category,
                'image': publication.image,
                'created_date': publication.created_date,
                'id': publication.id,
                'language': 'ru'
                }
            if str(language) == 'kg' and publication.id == kwargs['pk']:
                text_data = {
                'title': publication.title_kg,
                'text': publication.text_kg,
                'short_text': publication.short_text_kg,
                'hashtag': publication.hashtag,
                'category': publication.category,
                'image': publication.image,
                'created_date': publication.created_date,
                'id': publication.id,
                'language': 'kg'
                }


        context = {
            "publication": text_data,
            "publication_list": Publication.objects.exclude(id=kwargs['pk']),
            "comment_list": Publication.objects.get(id=kwargs['pk']).comments.all()
        }
        
        return context

class PubgCommnetView(View):
    def post(self, requests, *args, **kwargs):
        publication = Publication.objects.get(id=kwargs['pk'])

        Comment.objects.create(publication=publication, name=requests.POST['name'], text=requests.POST['message'])

        return redirect('pubg', pk=kwargs['pk'])

class SearchView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        search_word = self.request.GET["query"]
        context = {
            "publications": Publication.objects.filter(
                Q(short_text__icontains = search_word) | Q(title__icontains = search_word)
                )
        }

        return context

class ContactUsView(View):
    template_name = 'contact.html'
    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        data = {
            'chat_id': 6391825617,
            'text': f"{name}, {subject}\nSend you: {message}\nYou can reach them at {email}"
        }

        response = requests.post("https://api.telegram.org/bot7220782408:AAF6ZT6BKU--Rszs2sVFY1LdzU5hvHL7NF0/sendMessage", data=data)


        return redirect('contact_url')
