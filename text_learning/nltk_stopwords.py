# if this is the first time running nltk library and nltk.download()
# has not been called before, then it will have to be done before nltk
# can be used. It takes a few minutes.
from nltk.corpus import stopwords
sw = stopwords.words("english")
print "number of stopwords in english: ",len(sw),". 10th one: ",sw[10]

# trying out a stemmer
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")
print "stem for 'responsiveness': ",stemmer.stem("responsiveness")
