import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize

# Baixar recursos necessários
nltk.download('punkt')
nltk.download('wordnet')

def get_synonym(word):
    synonyms = wordnet.synsets(word)
    if synonyms:
        # Pega o primeiro sinônimo diferente da palavra original
        for lemma in synonyms[0].lemmas():
            if lemma.name().lower() != word.lower():
                return lemma.name().replace('_', ' ')
    return word  # Se não tiver sinônimo, retorna a palavra original

def replace_with_synonyms(text):
    words = word_tokenize(text)
    new_words = [get_synonym(word) for word in words]
    return ' '.join(new_words)

# Exemplo de uso
texto = "I love programming and learning new things"
print(replace_with_synonyms(texto))