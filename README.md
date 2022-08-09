# Youtube Transcript API
 
### A Chrome Extension that generates summary of a YouTube video with the help of its transcript using Natural Language Processing (NLP). Tech Stack: Python, PyTorch, Flask, HuggingFace Transformer 
### Abstract : 
   With the rise of Internet reach worldwide, there has been a substantial increase in the number
of videos uploaded and shared on various networking sites. One of the most popular video
sharing sites is YouTube. On YouTube, numerous videos are uploaded every single day from
all around the world. These videos include educational content, speeches, tutorials, so on.
Compact representations of video data can enable efficient video browsing. Such
representations provide the user with information about the content of the particular video
being examined while preserving the essential message. Hence, generating the summary of a
video prior to watching it, will tell you the gist of the video, on the basis of which you can
decide if it is worth watching the entire video. This demo proposes YO-script, a Chrome
extension, which extracts the summaries from video transcripts and generates important
keywords from it. The project uses Natural Language Processing methods for extractive and
abstractive summarization.

### PROBLEM STATEMENT:
300 hours of video are uploaded to YouTube every minute! Much of this content is verbose
like tutorials, speeches, educational content. It is quite difficult to spend time watching such
videos and sometimes our efforts may become futile if we couldn't find relevant information
out of it. We have developed a Chrome extension that curbs this issue by summarizing the
captions or transcript of any given video, it is able to pull the most important information and
condense it into a small paragraph, reading this paragraph would take a tiny fraction of the
total length of the video, while still providing the most important points to the user.
OBJECTIVES:
1. To generate Summary of YouTube video in the browser through a Chrome Extension.
2. To build a robust model which can generate summaries for videos on a wide range of
topics.

### PROPOSED SYSTEM:
We have created a chrome extension, which can be activated on any YouTube video whose
transcript is available. The unique video id will then be used to fetch the video’s transcript
which will be passed to the ML model for generating summary. The summary will then be
sent through HTTP in the form of JSON and will be displayed to the user. The basic strategy
it uses is using ML summarizing techniques on the transcript of the video.\

