from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import numpy as np

app = Flask(__name__)

# Load the pre-trained model
vectorizer = TfidfVectorizer()
clf = LogisticRegression()
# Sample input text
input_text = [
    'It seems like the model is not recognizing the human text because the input text for prediction is different from the training data.',
    'Team PAA is in round 2'
]

# Vectorize the input text
X_train_tfidf = vectorizer.fit_transform(input_text)
X_train = X_train_tfidf.toarray()

# Define corresponding labels for each sample
y_train = [0, 1]  # Assuming two classes: 0 and 1

# Fit the classifier to the training data
clf.fit(X_train, y_train)

@app.route('/')
def home():
    return render_template('paa.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        text = request.form['text']
        # Transform the input text to a feature vector
        input_vector = vectorizer.transform([text]).toarray()
        # Make predictions
        prediction = clf.predict(input_vector)
        return render_template('result.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)
