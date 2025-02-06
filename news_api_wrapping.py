from newsapi import NewsApiClient
from utils import get_content, get_nanoid_from_filename
from nanoid import generate
import os

class AdvancedNewsApiClient:
    def __init__(self):
        self.api = NewsApiClient(api_key=os.getenv('NEWS_API_KEY'))

    def get_language_news_sources(self, language_code):
        return [source['id'] for source in self.api.get_sources()['sources'] if source['language'] == language_code]

    def obtain_article_text_for_prompt(self, article_object):
        news_source = article_object['source']['name']
        time_published = article_object['publishedAt']
        prompt = f'According to the news source {news_source} at {time_published}, \n\n'
        article_content = get_content(article_object['url'])
        return prompt + article_content

    def get_id_prompt_pair_from_sources(self, sources):
        article_objects = self.api.get_top_headlines(sources=sources)['articles']
        return [(generate(), self.obtain_article_text_for_prompt(article_object)) for article_object in article_objects]

    def save_prompts_to_disk(self, id_prompt_pairs):
        for nano_id, prompt in id_prompt_pairs:
            with open(f'./prompts/{nano_id}.txt', 'w') as file:
                file.write(prompt)

    def get_prompt_from_disk(self, filename):
        prompt = ""
        with open(filename, 'r') as file:
            prompt = file.read()
        return (get_nanoid_from_filename(filename), prompt)