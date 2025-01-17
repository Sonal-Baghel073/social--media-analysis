import streamlit as st
from PyPDF2 import PdfReader
from pytesseract import image_to_string
from PIL import Image
from textblob import TextBlob
import textstat


st.title("Social Media Content Analyzer")
st.subheader("Upload PDF or Image Files")
uploaded_file = st.file_uploader("Choose a file", type=["pdf", "png", "jpg", "jpeg"])

# Text extraction functions
def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def extract_text_from_image(file):
    image = Image.open(file)
    text = image_to_string(image)
    return text

# Sentiment analysis function
def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        return "Positive"
    elif sentiment < 0:
        return "Negative"
    else:
        return "Neutral"

# Engagement suggestion function
def suggest_improvements(text):
    suggestions = []
    
    # Check for text length
    if len(text.split()) < 50:
        suggestions.append("Consider adding more details to your content.")
    
    # Check for hashtags
    if not any(word.startswith("#") for word in text.split()):
        suggestions.append("Add relevant hashtags for better engagement.")
    
    # Readability analysis
    readability_score = textstat.flesch_reading_ease(text)
    if readability_score < 60:
        suggestions.append("Consider simplifying the language for better readability. Readability score: {:.2f}".format(readability_score))
    
    # Keyword suggestions (simple approach)
    keywords = ['fitness', 'health', 'wellness', 'motivation', 'lifestyle']  # Example list, could be dynamic
    if not any(keyword in text.lower() for keyword in keywords):
        suggestions.append("Consider adding relevant keywords like 'fitness', 'health', or 'motivation' to improve visibility.")
    
    return suggestions

if uploaded_file:
    if uploaded_file.name.endswith(".pdf"):
        extracted_text = extract_text_from_pdf(uploaded_file)
    else:
        extracted_text = extract_text_from_image(uploaded_file)

    st.write("Extracted Text:")
    st.text_area("", extracted_text, height=200)

    # If text has been extracted, proceed with sentiment analysis and suggestions
    if extracted_text.strip():
        sentiment = analyze_sentiment(extracted_text)
        st.write("Sentiment Analysis:", sentiment)

        suggestions = suggest_improvements(extracted_text)
        st.write("Engagement Suggestions:")
        for suggestion in suggestions:
            st.write("- ", suggestion)
