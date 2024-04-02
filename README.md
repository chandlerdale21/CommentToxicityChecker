# CommentScanner

## Description
CommentScanner is a Python application designed to classify and filter user comments by detecting levels of toxicity. This tool aids online community moderators by automating the content moderation process, identifying various degrees of inappropriate content, and promoting positive engagement across platforms.

## Features
- Multi-label classification of comments
- Machine learning integration with a logistic regression model
- Preprocessing with TF-IDF vectorization
- User-friendly graphical interface
- Visualization of comment data distribution

## Installation
To set up CommentScanner, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the project directory and run the following commands in your terminal.
3. python -m PyInstaller --onefile --windowed --add-data "toxic_comment_classifier.joblib;." --add-data "tfidf_vectorizer.joblib;." main.py
4. python -m PyInstaller main.spec

