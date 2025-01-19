# Social-Media-Content-Analyzer

**Overview**

The Social Media Content Analyzer is a web-based application designed to help users optimize their social media posts by analysing uploaded PDF or image files. The app extracts text from these files, analysis their sentiment, and provides actionable suggestions for improving content engagement. By making the content more engaging, readable, and discoverable, this tool aims to boost interaction on social media platforms.

**Features**

Text Extraction from PDF and Image Files
The app supports both PDF and image uploads. It uses different methods to extract text depending on the file type:
PDF Files: The app extracts text using PyPDF2, which reads and extracts text from the pages of a PDF document.
Image Files: The app uses pytesseract (OCR) to extract text from images (PNG, JPG, JPEG).

 **Sentiment Analysis**

Using TextBlob, the app analyzes the sentiment of the extracted text, categorizing it as Positive, Negative, or Neutral based on the emotional tone.

 **Engagement Suggestions**

The app generates engagement suggestions, considering factors like:
Text length (suggesting more detail if the post is too short),
Hashtags (suggesting the addition of relevant hashtags),
Readability (suggesting simplification if the readability score is low),
Keywords (suggesting relevant keywords to improve discoverability).

 **Interactive User Interface**
Built with Streamlit, the app provides a user-friendly interface for uploading files and viewing the results.

**Technologies Used**
1. Streamlit
Streamlit is used to create the interactive web interface of the application, allowing users to easily upload files and view extracted text, sentiment analysis, and engagement suggestions.

2. PyPDF2
PyPDF2 is a Python library for extracting text from PDF files, making it easy to handle multi-page documents.

3. Pytesseract (OCR)
Pytesseract is a Python wrapper for Tesseract OCR, used to extract text from image files, allowing the tool to analyze text embedded in images.

4. TextBlob
TextBlob is used for sentiment analysis, which classifies the emotional tone of the extracted text as positive, negative, or neutral.

5. Textstat
Textstat is used to assess the readability of the text, providing the Flesch Reading Ease score to determine whether the content is easy to understand.

6. Pillow (PIL)
Pillow (PIL) is used to open and manipulate image files, enabling the app to extract text from image files and modify the images if necessary.



