try:
    from pprint import pprint
    from PyDictionary import PyDictionary
    from googletrans import Translator
except Exception as e:
    print('Modules missing {}'.format(e))

dictionary = PyDictionary()
translator = Translator()

language_code = [
    {
        'en': 'English',
        'hi': 'Hindi',
        'es': 'Spanish',
        'fr': 'French',
        'ja': 'Japanese',
        'ru': 'Russian',
        'de': 'German',
        'it': 'Italian',
        'ko': 'Korean',
        'pt-BR': 'Brazilian Portuguese',
        'zh-CN': 'Chinese (Simplified)',
        'ar': 'Arabic',
        'tr': 'Turkish'
    }
]


def meaningSynonym(word):
    # word = input('Enter a word or words separated by space to get meaning: ')
    many = word.split()
    res = ''
    for i in many:
        res += f'MEANING: {dictionary.meaning(i)}\n\n\n'
        res += f'SYNONYM: {dictionary.synonym(i)}\n\n'

    return res


def meanings(words):
    # words = input('Enter words separated by space if more than one')
    many = words.split()
    means = PyDictionary(many)
    print(means.printMeanings())


def translateAny(word, lang):
    trans = translator.translate(word, dest=lang)
    final = trans.text
    print(final)


def transFr(words, lang='fr'):
    # many = words.split()
    translation = translator.translate(words, dest=lang)
    final = f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})"
    return final


# if __name__ == '__main__':
    # translateAny('bulldog love', lang='fr')
    # translation = translator.translate("Hola Mundo")
    # print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
