train_set = ("The sky is blue.", "The sun is bright.")
test_set = ("The sun in the sky is bright.", "We can see the shining sun, the bright sun.")

from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
