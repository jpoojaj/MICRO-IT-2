import streamlit as st
from textblob import TextBlob

# Set page config
st.set_page_config(page_title="Sentiment Analyzer", page_icon="😊", layout="centered")

st.title("😊 Sentiment Analysis Web App")
st.markdown("### Predict the emotion behind your text!")

# Input text
text_input = st.text_area("📝 Enter your text below:")

# Analyze function
def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "Positive 😀", polarity
    elif polarity < 0:
        return "Negative 😞", polarity
    else:
        return "Neutral 😐", polarity

# Button to analyze
if st.button("🔍 Analyze Sentiment"):
    if text_input.strip() != "":
        sentiment, polarity = analyze_sentiment(text_input)
        st.success(f"**Sentiment:** {sentiment}")
        st.info(f"**Polarity Score:** {polarity:.2f}")
    else:
        st.warning("⚠️ Please enter some text!")

# Footer
st.markdown("---")
st.caption("Built with ❤️ by Pooja J | Micro IT Internship Project")
