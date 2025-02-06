from ChromaNewsDB import ChromaNewsDBClient
from news_api_wrapping import AdvancedNewsApiClient
from utils import format_newsapi_sources_str

if __name__ == '__main__':
    news_api = AdvancedNewsApiClient()
    chroma_client = ChromaNewsDBClient()

    news_sources = news_api.get_language_news_sources('en')
    news_api.save_prompts_to_disk(id_prompt_pairs=
                                  news_api.get_id_prompt_pair_from_sources(sources=format_newsapi_sources_str(news_sources)))
    
    #TODO: determine how many files we can actually read and push into gemini without killing api (15 requests per minute)