python -m spacy download en_core_web_md

import spacy
nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
      print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
      similarity = nlp(sentence).similarity(model_sentence)
      print(sentence + " - ",  similarity)

# The similarities between the words 'cat', 'monkey', and 'banana' were interesting to me because they illustrate how different words can have similar vector representations based on their contexts of usage.
# In this case, all three words are associated with the concept of 'tree', which is why their similarity scores are relatively high. 
# An example of my own could be the words 'car', 'bus', and 'train', which could have higher similarity scores if they appear in the context of 'transportation'.

# Note on model differences:

# When running the example file with the simpler language model 'en_core_web_sm', I noticed that the model was not as accurate in identifying the relationships between words as the 'en_core_web_md' model. 
# Specifically, the 'en_core_web_sm' model was not as good at identifying entities and part-of-speech tags, which can be important for many natural language processing tasks.
# However, the 'en_core_web_sm' model may be useful for simpler tasks where computational resources are limited.
