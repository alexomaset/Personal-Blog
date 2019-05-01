import urllib.request, json
from .models import Author





api_key = None
quotes = None


def configure_request(app):
    global api_key, quotes_url 
    api_key = app.config['QUOTES_API_KEY']
    quotes_url = app.config['QUOTES_BASE_URL']
    


def get_quote():
    '''
    Function that gets the json response to our url request
    '''

    with urllib.request.urlopen('http://quotes.stormconsultancy.co.uk/random.json') as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        quote_object= None
        if get_sources_response :
                author= get_sources_response.get('author')
                quote = get_sources_response.get('quote')
        quote_object= Author(author,quote)

    
    return quote_object