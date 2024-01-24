from flask import Flask, render_template, request
import spacy

app = Flask(__name__)


def generate_summary(text):
    # Load spaCy model for English
    nlp = spacy.load("en_core_web_sm")

    # Process the text
    doc = nlp(text)

    # Extract sentences and calculate their importance scores
    sentence_scores = {}
    for sentence in doc.sents:
        for word in sentence:
            word_lower = word.text.lower()
            if word_lower in sentence_scores:
                sentence_scores[word_lower] += 1
            else:
                sentence_scores[word_lower] = 1

    # Rank sentences based on importance scores
    ranked_sentences = sorted([(sentence.text.capitalize(), sentence_scores.get(sentence.text.lower(), 0)) for sentence in doc.sents],
                              key=lambda x: x[1], reverse=True)

    # Select top N sentences for the summary
    # Adjust the number as needed
    summary_sentences = [sentence[0] for sentence in ranked_sentences[:3]]

    # Combine selected sentences to form the summary
    summary = ' '.join(summary_sentences)

    # Extract key points, tone, and keywords
    # Using top 3 sentences as key points
    key_points = [sentence[0] for sentence in ranked_sentences[:3]]
    tone = "Neutral"  # Replace with actual tone analysis
    # Adjust the number as needed
    keywords = [
        token.text for token in doc if not token.is_stop and token.is_alpha][:4]

    return summary, key_points, tone, keywords


@app.route('/', methods=['GET', 'POST'])
def index():
    summary = key_points = tone = keywords = None

    if request.method == 'POST':
        text_input = request.form['text_input']
        summary, key_points, tone, keywords = generate_summary(text_input)

    return render_template('index.html', summary=summary, key_points=key_points, tone=tone, keywords=keywords)


if __name__ == '__main__':
    app.run(debug=True)
