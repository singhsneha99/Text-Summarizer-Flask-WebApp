# Text Summarizer App

This is a simple Flask web app that summarizes text passages using spaCy's NLP capabilities. 

## Features

The app allows users to:

- Enter any text passage into a form 
- Generate a summarized version of the text
- See key points extracted from the passage
- View the overall tone as detected by the summarizer 
- See top keywords pulled from the text

The summarized output contains the most important sentences from the original passage to provide a concise overview.

## Usage

To use the app:

1. Ensure Flask, spaCy and other dependencies are installed
2. Run `app.py` 
3. Navigate to `http://localhost:5000`
4. Paste or type any text into the input form
5. Click "Generate Summary" to see the results

The input text is processed by the `generate_summary()` function which handles the NLP analysis and summary generation.

## Output
<img width="1433" alt="Screenshot 2024-01-24 at 10 12 33 AM" src="https://github.com/singhsneha99/Text-Summarizer-Flask-WebApp/assets/47446483/0b0fa105-012a-4a70-bb55-aaa58b0206fb">


The number of sentences in the final summary can be adjusted by changing the slice amount in `summary_sentences` list. 

Other output like key points, tone and keywords can also be configured as needed for the use case.

Additional summarization algorithms can be added and compared alongside the current keyword extraction method.
