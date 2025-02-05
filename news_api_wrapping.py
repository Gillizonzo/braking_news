from newsapi import NewsApiClient
from utils import get_content
import os

api = NewsApiClient(api_key=os.getenv('NEWS_API_KEY'))

def get_language_news_sources(language_code):
    return [source['id'] for source in api.get_sources()['sources'] if source['language'] == language_code]

def obtain_article_text_for_prompt(article_object):
    news_source = article_object['source']['name']
    time_published = article_object['publishedAt']
    prompt = f'According to the news source {news_source} at {time_published}, \n\n'
    article_content = get_content(article_object['url'])
    return prompt + article_content

def get_prompts_from_sources(sources):
    article_objects = api.get_top_headlines(sources=sources)['articles']
    return [obtain_article_text_for_prompt(article_object) for article_object in article_objects]

