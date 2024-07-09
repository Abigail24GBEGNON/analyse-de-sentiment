import warnings
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import streamlit as st
warnings.filterwarnings("ignore")

def main():
    st.title("Analyse du sentiment d'un texte by KidsInnov Class")
    st.image("analyse.png")
    analyseur()

# Fonction de classification
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()


def classification(text):
     sentiment = sia.polarity_scores(text)
     return sentiment

def analyseur():
     text = st.text_area("Entrez le texte à analyser")

     if st.button("Qu'exprime cet texte?"):
     
          sentiment = classification(text)
          pos = sentiment["pos"] * 100
          neu = sentiment["neu"] * 100
          neg = sentiment["neg"] * 100

          st.markdown("<h2><b>Votre texte est :</h2></b>", unsafe_allow_html=True)
          st.write("**Positif à", pos, "%**")
          st.write("**Neutre à", neu, "%**")
          st.write("**Négatif à", neg , "%**")

if __name__ == "__main__":
     main()
    
