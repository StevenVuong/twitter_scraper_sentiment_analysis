# Overview
Collection of explainers of some of the tools and paramets that are used to help
build understanding of what we are playing with and what else is possible.

##### TF-IDF
Term Frequency- Inverse Document Frequency. Helps deterrine how important a worrd is to a document or collection, sort of a weighing factor in terms of information retrieval. So the TF-IDF increases proportionally to the number of times a word appears in the document, and also factorss in the number of documents in the corpus that contain the words. By doing so, it adjusts forr the fact that some words appear more frequently in general. This is a very popular term-weighing system.

Source: https://en.wikipedia.org/wiki/Tf%E2%80%93idf

SkLearn's TfIDF vectoriser (https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html):
-  strip_accents: Remove accents and does other character normalisation. 'ascii' only works on characters with a direct ASCII mapping, 'unicode' is slightly slower and works on any characters.
-  analyzer: Whether made of word or ngrams
-  token_pattern: Regular expression that denotes what a 'token' is
-  ngram_range: The upper and lower boundary of the range of n-values for different n-grams to be extracted
-  use_idf: Enable inverse-doc-frequency reweighting
-  smooth_idf: Smooth IDF weights by adding one to document frequency (as if an extrra doc seen containing every term in collection at least once). Prevents zero divisions.
-  sublinear_tf: Replace tf with 1+log(tf) -> sublinear tf scaling
-  stop_words: Remove stopwords from resulting tokens

##### word_tokenize
Returns tokenissed copy of text, uisng NLTK'ss recommended word tokeniser. Text split into sentences, ussing Pinkt corpus
https://kite.com/python/docs/nltk.word_tokenize

##### `.isalpha()`
Tells us if all the characters in the string are alphabets. English letters, not numbers

##### Logistic Regression(C=1)
Ref: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html


Inverse of regularization strength; must be a positive float. Like in support vector machines, smaller values specify stronger regularization.

##### Count Vectoriser:
Convert collection of document matrices to a collection of counts.

##### XGBoost Parameters
-  max_depth: Maximum depth of a tree. Increasing this value will make the model more complex and more likely to overfit. Note that XGBoost aggressively consumes memory during training
-  n_estimators: Number of trees (or estimators) in an xgboost model
-  colsample_bytree: This is a family of parameters for subsampling of columns.
-  subsample: Subsample ratio of the training instances. Setting it to 0.5 means that XGBoost would randomly sample half of the training data prior to growing trees. and this will prevent overfitting. Subsampling will occur once in every boosting iteration.
-  nthread: Number of parallel threads used to run XGBoost
-  learning_rate

##### .tocsc():
Return a copy of sparse matrix in Compressed Sparse Column format

##### sklearn make_scorer:

