# YouTubeTranscriptAPI Imports
from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound, VideoUnavailable, TooManyRequests, \
    TranscriptsDisabled, NoTranscriptAvailable
from youtube_transcript_api.formatters import TextFormatter
# Transformers Imports
from transformers import T5ForConditionalGeneration, T5Tokenizer

# Flask Imports
from flask import Flask, jsonify, request, send_from_directory, render_template, redirect

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index_page():
    return "Hello world"

def get_transcript(video_id):
    # Using Formatter to store and format received subtitles properly.
    formatter = TextFormatter()
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    formatted_text = formatter.format_transcript(transcript).replace("\n", " ")
    return formatted_text
    """
    # Catching Exceptions
    except VideoUnavailable:
        return jsonify(success=False, message="VideoUnavailable: The video is no longer available.",
                        response=None), 400
    except TooManyRequests:
        return jsonify(success=False,
                        message="TooManyRequests: YouTube is receiving too many requests from this IP."
                                " Wait until the ban on server has been lifted.",
                        response=None), 500
    except TranscriptsDisabled:
        return jsonify(success=False, message="TranscriptsDisabled: Subtitles are disabled for this video.",
                        response=None), 400
    except NoTranscriptAvailable:
        return jsonify(success=False,
                        message="NoTranscriptAvailable: No transcripts are available for this video.",
                        response=None), 400
    except NoTranscriptFound:
        return jsonify(success=False, message="NoTranscriptAvailable: No transcripts were found.",
                        response=None), 400
    except:
        # Prevent server error by returning this message to all other un-expected errors.
        return jsonify(success=False,
                        message="Some error occurred."
                                " Contact the administrator if it is happening too frequently.",
                        response=None), 500
                        """

def get_summary(transcript):
    # initialize the model architecture and weights
    model = T5ForConditionalGeneration.from_pretrained("t5-base")
    # initialize the model tokenizer
    tokenizer = T5Tokenizer.from_pretrained("t5-base")
    # encode the text into tensor of integers using the appropriate tokenizer
    inputs = tokenizer.encode("summarize: " + transcript, return_tensors="pt", max_length=512, truncation=True)
    outputs = model.generate(
    inputs, 
    max_length=150, 
    min_length=40, 
    length_penalty=2.0, 
    num_beams=4, 
    early_stopping=True)
    # just for debugging
    #print(outputs)
    return (tokenizer.decode(outputs[0]))

# Processing Function for below route.
@app.route('/summarize/', methods=['GET'])
def transcript_fetched_query():
    # Getting argument from the request
    video_id = request.args.get('id')  # video_id of the YouTube Video
    try:
        transcript = get_transcript(video_id)
    # Catching Exceptions
    except VideoUnavailable:
        return jsonify(success=False, message="VideoUnavailable: The video is no longer available.",
                        response=None), 400
    except TooManyRequests:
        return jsonify(success=False,
                        message="TooManyRequests: YouTube is receiving too many requests from this IP."
                                " Wait until the ban on server has been lifted.",
                        response=None), 500
    except TranscriptsDisabled:
        return jsonify(success=False, message="TranscriptsDisabled: Subtitles are disabled for this video.",
                        response=None), 400
    except NoTranscriptAvailable:
        return jsonify(success=False,
                        message="NoTranscriptAvailable: No transcripts are available for this video.",
                        response=None), 400
    except NoTranscriptFound:
        return jsonify(success=False, message="NoTranscriptAvailable: No transcripts were found.",
                        response=None), 400
    except:
        # Prevent server error by returning this message to all other un-expected errors.
        return jsonify(success=False,
                        message="Some error occurred. Contact the administrator if it is happening too frequently. Failed at get_transcript",
                        response=None), 500
    # return jsonify(success=True, message="Subtitles for this video was fetched and summarized successfully.",
    #                 response=transcript), 200
    try:
        summary = get_summary(transcript)
    except:
        # Prevent server error by returning this message to all other un-expected errors.
        return jsonify(success=False,
                        message="Some error occurred."
                                " Contact the administrator if it is happening too frequently. Failed at get_summary",
                        response=None), 500
    return jsonify(success=True, message="Subtitles for this video was fetched and summarized successfully.",
                    response=summary), 200

if __name__ == '__main__':
    # Running Flask Application
    app.run()