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
Make a scorer from a performance metric or loss function.

This factory function wraps scoring functions for use in GridSearchCV and cross_val_score. It takes a score function, such as accuracy_score, mean_squared_error, adjusted_rand_index or average_precision and returns a callable that scores an estimator’s output.
-  greater_is_better: Whether score_func is a score function (default), meaning high is good, or a loss function, meaning low is good. In the latter case, the scorer object will sign-flip the outcome of the score_func.
-  needs_probaboolean: Whether score_func requires predict_proba to get probability estimates out of a classifier.

##### sklearn pipeline.Pipeline:
Sequentially applies a list of transforms and a final estimator. Intermediate steps must be 'transforms', so implement a fit and transform methods. The final estimator only needs to implement fit.

The purpose of the pipeline is to assemble several steps that can be cross-validated together while setting different parameters. 

##### sklearn GridSearch:
Exhaustive search over specified parameter values for an estimator.
The parameters of the estimator used to apply these methods are optimized by cross-validated grid-search over a parameter grid.

-  iid: If True, return the average score across folds, weighted by the number of samples in each test set. In this case, the data is assumed to be identically distributed across the folds, and the loss minimized is the total loss per sample, and not the mean loss across the folds.
-  refit: Refit an estimator using the best found parameters on the whole dataset
-  cv: Determines the cross-validation splitting strategy.

##### word vectors:
Word vectors are simply vectors of numbers that represent the meaning of a word.

##### %r:
old-style string formatting. Converts object to a representation with repr() function.

##### Singular Value Decomposition (SVD):
Generalises eigendecomposition (eigenfactors of a matrix) to any m*n matrix via an extension of the polar decomposition. 

Reduce a matrix to its constituent parts to make later calculations easier.

##### Embedding Matrix:
Linear mapping from original space to a real-valued space where entities can have meaningful relationships. We can learn this too.
Represent relationships in a general way to solve relationship representation problem.

Ultimately a list of words and their corresponding embeddings.

##### Spatial Dropout:
Drops entire 2D feature maps instead of individual elements. If adjacent pixels within feature maps are strongly correlatetd (usually the case in early convolution layers) then regular dropout will not regularise activations and just result in learning rate decrease. So SpatialDropout2D helps promote independence between feature maps.

##### LSTM:
LSTM: Preserves information from inputs that has alerady passed through it using the hidden state. Traditional unidirectional only preserves past information as inputs seen are from the past. 
-  Forget gate: Decides what information iss relevant to keep from prior steps.
-  Input Gate: Decides what is relevant to add from current stetp
-  Output Gate: Determines what next hidden state should be

##### Bidirectional LSSTM
Bidirectional runs inputs two ways, one from past to future and the other from future to past, thus preserving information from both past and future at any point in time. This has the effect of gathering more context around any given token.

##### GRU:
https://towardsdatascience.com/illustrated-guide-to-lstms-and-gru-s-a-step-by-step-explanation-44e9eb85bf21
During back propagation, RNNs suffer from vanishing gradient problem (shrinks as it back propagates through time) and becomes a problem as too small gradients don't contribute to learning.

Newer version of RNN. Got rid of cell statte and uses hidden state to transfer information. Only reset and update gate.
-  Update gate: Decides what information to discard and what to add
-  Reset gate: Decide how much past informaion to forget

Speedier to train than LSTM slightly as fewerr tensor operations. Depends on use case
