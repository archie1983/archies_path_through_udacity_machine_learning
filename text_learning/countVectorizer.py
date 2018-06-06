from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
string1 = "This is email number 1"
string2 = "Email number 2 here. Have a nice day."
string3 = "Day is indeed nice. Email number 3 by the way."

a = cv.fit_transform([string1, string2, string3])
print "index of word 'number': ",cv.vocabulary_.get("nice")
print a
