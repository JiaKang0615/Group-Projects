import numpy as np
import lda
import lda.datasets
import textmining
import pandas as pd
from pandas import Series, DataFrame
import os
import nltk
from nltk.corpus import stopwords

def process_text(inp_text, stop):
    lemma = nltk.wordnet.WordNetLemmatizer()
    word_list = inp_text.lower().split()
    word_list = [lemma.lemmatize((filter(str.isalpha, word)).lower()) for word in word_list]
    filtered_words = [word for word in word_list if word not in stop]
    filtered_words = [lemma.lemmatize((filter(str.isalpha, word)).lower()) for word in filtered_words]
    filtered_words.join(" ")
    return filtered_words
    



t1 = datetime.datetime.now()
print os.getcwd()
os.chdir("C:/OneDrive/UMN/MSBA 6410 Exploratory/Group Project/Final")
stop = stopwords.words('english')
stop = stop + ['thursday' , 'friday','saturday','monday','tuesday', 'wednesday','call', 'calls' ,'schedule' ,'speech' , 'sid', 'update' , 'fyi' , 'today' , 'new' ,'tomorrow' ,'latest']
stop = stop + ['autoreply' , 'thank' , 'called' ,'want' ,'asking' ,'see' ,'day' ,'plan' ,'end' , 'still' ,'also'] 

email_csv = pd.read_csv('Hillary_emails_op.csv',sep = ',',header =  0, skiprows = 0)
email_csv2 = email_csv[0:7945]

email_csv3 = pd.DataFrame()
email_csv3['id'] = email_csv2['Id']
email_csv3['content'] = (email_csv2['ExtractedSubject'] +' '+ email_csv2['ExtractedBodyText']).fillna('   ')
email_csv3['month'] = (email_csv2['MetadataDateSent'].str[5:7]).fillna(0).astype(int)
email_csv3['year'] = email_csv2['MetadataDateSent'].str[0:4].fillna(0).astype(int)



# document-term matrix
X = lda.datasets.load_reuters()
print("type(X): {}".format(type(X)))
print("shape: {}\n".format(X.shape))

# the vocab
vocab = lda.datasets.load_reuters_vocab()
print("type(vocab): {}".format(type(vocab)))
print("len(vocab): {}\n".format(len(vocab)))


# titles for each story
titles = lda.datasets.load_reuters_titles()
print("type(titles): {}".format(type(titles)))
print("len(titles): {}\n".format(len(titles)))

doc_id = 0
word_id = 3117

print("doc id: {} word id: {}".format(doc_id, word_id))
print("-- count: {}".format(X[doc_id, word_id]))
print("-- word : {}".format(vocab[word_id]))
print("-- doc  : {}".format(titles[doc_id]))


tdm = textmining.TermDocumentMatrix()

# Add the documents
for doc in email_csv3['content']:
    tdm.add_doc(doc)
    
for row in tdm.rows(cutoff=200):
    print row
    break




model = lda.LDA(n_topics=4, n_iter=500, random_state=1)
model.fit(X)
topic_word = model.topic_word_ 

n_top_words = 8

for i, topic_dist in enumerate(topic_word):
    topic_words = np.array(vocab)[np.argsort(topic_dist)][:-n_top_words:-1]
    print('Topic {}: {}'.format(i, ' '.join(topic_words)))
