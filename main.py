import streamlit as st
import string
import joblib
import re
import emoji
from PIL import Image

model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")



st.header("Twitter sentiment Analysis")
image = Image.open('head_image.png')
st.image(image, caption='Is the tweet Positive or Negative?',use_column_width=True)
st.text(" By Sanjay Suthraye ")



def url(i):
    j=" ".join(filter(lambda x:x[0]!='@', i.split()))
    j1=re.sub(r"http\S+", "", j)
    j2=" ".join(filter(lambda x:x[0]!='&', j1.split()))
    return j2

def smiley(a):
    x1=a.replace(":‑)","happy")
    x2=x1.replace(";)","happy")
    x3=x2.replace(":-}","happy")
    x4=x3.replace(":)","happy")
    x5=x4.replace(":}","happy")
    x6=x5.replace("=]","happy")
    x7=x6.replace("=)","happy")
    x8=x7.replace(":D","happy")
    x9=x8.replace("xD","happy")
    x10=x9.replace("XD","happy")
    x11=x10.replace(":‑(","sad")
    x12=x11.replace(":‑[","sad")
    x13=x12.replace(":(","sad")
    x14=x13.replace("=(","sad")
    x15=x14.replace("=/","sad")
    x16=x15.replace(":[","sad")
    x17=x16.replace(":{","sad")
  
    x18=x17.replace(":P","playful")
    x19=x18.replace("XP","playful")
    x20=x19.replace("xp","playful")
  
    
    x21=x20.replace("<3","love")
    x22=x21.replace(":o","shock")
    x23=x22.replace(":-/","sad")
    x24=x23.replace(":/","sad")
    x25=x24.replace(":|","sad")
    
    return x25

def lower(x):
    z=x.lower()
    return z


    
def decontracted(phrase):
    # specific
    phrase = re.sub(r"won\'t", "will not", phrase)
    phrase = re.sub(r"can\'t", "can not", phrase)

    # general
    phrase = re.sub(r"n\'t", " not", phrase)
    phrase = re.sub(r"\'re", " are", phrase)
    phrase = re.sub(r"\'s", " is", phrase)
    phrase = re.sub(r"\'d", " would", phrase)
    phrase = re.sub(r"\'ll", " will", phrase)
    phrase = re.sub(r"\'t", " not", phrase)
    phrase = re.sub(r"\'ve", " have", phrase)
    phrase = re.sub(r"\'m", " am", phrase)
    return phrase

def digit(x):
    z=re.sub('\w*\d\w*','', x)
    return z

def punct(x):
    z=re.sub('[%s]' % re.escape(string.punctuation), '', x)
    return z

def odd(a):
    words = ['wi','ame','quot','ti','im']
    querywords = a.split()

    resultwords  = [word for word in querywords if word.lower() not in words]
    result = ' '.join(resultwords)
    return result



def stop(a):
    stop=["i", "me", "my", "myself", "we", "our","will", "go","got","ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such",  "nor", "only", "own", "same", "so", "than", "too", "very", "s", "t", "just", "don", "should", "now"]

    querywords = a.split()

    resultwords  = [word for word in querywords if word.lower() not in stop]
    result = ' '.join(resultwords)
    return result

def space(a):
    x=re.sub(' +', ' ', a)
    return x

def prediction():
    input1=st.text_input("Enter Tweet below & Click Predict"," ")
    



    if st.button("Predict"):
        process1=url(input1)
        process2=smiley(process1)
        process3=lower(process2)
        process4=decontracted(process3)
        process5=digit(process4)
        process6=punct(process5)
        process7=odd(process6)
        process8=space(process7)
        process9=stop(process8)
        process10=space(process9)
        process11=[process10]    
        vect_pro=vectorizer.transform(process11)
        result1 =vect_pro.reshape(1, -1)
        result=model.predict(result1)
        
        if result==1:
            st.text(emoji.emojize(":grinning_face_with_big_eyes:"))
            st.success('The tweet is Positive')
        if result==0:
            st.text(emoji.emojize(":zipper-mouth_face:"))
            st.error('The tweet is Negative')
            
            
        



if __name__=='__main__':
    prediction()