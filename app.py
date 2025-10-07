import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Download stopwords (only needed once)
nltk.download("stopwords")
nltk.download("punkt")

# Example Text for the summarization.
text = """
Apple has announced the release of the iPhone 17, which comes with a faster A19 Bionic chip, improved battery life, and a new periscope zoom camera. The company also introduced an AI-powered “Smart Mode” that automatically adjusts settings for photography and video recording. The iPhone 17 will be available in stores from October 15, with pre-orders starting this Friday. Alongside the iPhone, Apple unveiled the Apple Watch Series 10 with enhanced health tracking and a thinner design.
"""


