#!/usr/bin/env python
# coding: utf-8

# #hi

# In[40]:


def remove_stopwords(input_text):
    
    stop_words = [ "a", "and" , "the" , "it" , "an", "in" , "on","at","to","of"]
    words = input_text.split()
    filtered_words = []
    for word in words:
        if word.lower() not in stop_words:
            filtered_words.append(word)

    output_text = ' '.join(filtered_words)
    return (output_text)


# In[42]:


remove_stopwords("hey it was the good movie")


# #hey

# In[ ]:




