import requests

APP_ID = 'ce9bfac4'
APP_KEY = '93524c8a5a1ddc2344b2ba36295f37bb'

# e.g. -
# https://od-api.oxforddictionaries.com:443/api/v1/entries/en/ace/regions=us
#
# Note that regions=us will make the query fail if language is not english.
URL_FORMAT = ("https://od-api.oxforddictionaries.com:443/api/v1/entries/"
              "{0}/{1}{2}")

class WordDefinition:
    def __init__(self, domains, definitions, examples, lexicalCategory):
        self.domains = domains
        self.definitions = definitions
        self.examples = examples
        self.lexicalCategory = lexicalCategory

class WordDetails:
    def __init__(self, word, language, definitions):
        self.word = word
        self.language = language
        self.definitions = definitions

def get_word_definitions(sense, lexicalCategory):
    domains = []
    if 'domains' in sense:
        for domain in sense['domains']:
            domains.append(domain)

    definitions = []
    if 'definitions' in sense:
        for definition in sense['definitions']:
            definitions.append(definition)

    examples = []
    if 'examples' in sense:
        for example in sense['examples']:
            examples.append(example['text'])

    return WordDefinition(domains, definitions, examples, lexicalCategory)

def get_word_details(word, language):
    """
    Get the details of this word from the RESTful Dictionary service.
    :param word: The word for details are requested
    :param language: 'en' for english, 'es' for spanish
    :return: an object of WordDetails if we find the details, None otherwise
    """

    region = '/regions=us' if language is 'en' else ''
    rest_url = URL_FORMAT.format(language, word.lower(), region)
    print (rest_url)
    response = requests.get(rest_url,
                            headers={'app_id': APP_ID, 'app_key': APP_KEY})

    if response.status_code != 200:
        return None

    dict_json = response.json()
    print (dict_json)

    definitions = []

    for result in dict_json['results']:
        for lexicalEntry in result['lexicalEntries']:
            lexicalCategory = lexicalEntry['lexicalCategory']
            for entry in lexicalEntry['entries']:
                for sense in entry['senses']:
                    definitions.append(
                        get_word_definitions(sense, lexicalCategory))
                    if 'subsenses' in sense:
                        for subsense in sense['subsenses']:
                            definitions.append(
                                get_word_definitions(subsense, lexicalCategory))

    return WordDetails(word, language, definitions)

def main():
    word_details = get_word_details("pedagogical", "en")

    for definition in word_details.definitions:
        print ("\n** Entry\n")
        print ("Type: {0},\n Domains: {1},\n Definitions: {2},\n Examples: {3}".format(
            definition.lexicalCategory, definition.domains, definition.definitions,
            definition.examples
        ))

if __name__ == '__main__':
    main()