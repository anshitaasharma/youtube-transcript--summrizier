from flask import Flask, render_template, request
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    summary = []  
    if request.method == 'POST':
        try:
            video_url = request.form.get('video_url')
            video_id = video_url.split('=')[1]
            transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
            transcript = " ".join([d['text'] for d in transcript_list])

            summarizer = pipeline('summarization')

            num_iters = int(len(transcript) / 1000)
            for i in range(0, num_iters + 1):
                start = i * 1000
                end = (i + 1) * 1000
                out = summarizer(transcript[start:end])
                out = out[0]
                out = out['summary_text']
                summary.append(out)  

        except Exception as e:
            summary = ["An error occurred: " + str(e)]  

    return render_template('home.html', summary=summary) 

if __name__ == '__main__':
    app.run(debug=True)