# Artikulate

<!-- Badges from https://shields.io/badges -->

[![Static Badge](https://img.shields.io/badge/Python-3.11.7-306998)](https://www.python.org/downloads/release/python-3117/) [![Static Badge](https://img.shields.io/badge/Django-4.2.10-limegreen)](https://docs.djangoproject.com/en/4.2/releases/4.2.10/) [![Static Badge](https://img.shields.io/badge/Selenium-4.16.0-62ae41)](https://www.selenium.dev/blog/2023/selenium-4-16-released/) [![Static Badge](https://img.shields.io/badge/FFmpeg-6.1.1-337521)](https://www.ffmpeg.org/download.html)

## Inspiration

The shift towards short-term content in recent years, particularly on social media platforms like TikTok, reflects a broader trend in how the modern generation consumes and engages with information. Platforms like TikTok thrive on engaging visuals and user-generated content, catering to decreasing attention spans. We aimed to create a product capable of transforming traditional text regarding realms like news, education content, and stories, into a more engaging format for the newer generations.

## What it does

Artikulate is a video-editing and content-generation tool, which creates text-to-speech caption videos. There are two main features to Artikulate: generative AI and web scraping.

When users enter Artikulate they are asked if they want to create a video for Entertainment, for educational purposes (History), or create a Custom Video. If they select Entertainment, they can choose between generative AI or web-scraping Reddit posts in real time. Regardless of their option, they can select from a list of subreddits they want their video to be from and the type of background video the generated video will have. If the user selects History, they can select from a list of articles or input their own URL to create an informative video. Lastly, if the user selects Custom, they can input their own text that will be used in the text-to-speech caption generated videos.

Read more/demo on Devpost:

[![Devpost](https://img.shields.io/badge/Devpost-003E54?style=for-the-badge&logo=devpost&logoColor=white)](https://devpost.com/software/artikulate)

## How to run:

#### Prerequisites:

- Python, Django, and Docker

### Running with docker:

- Currently Django and FFmpeg works on docker, but I need to set up docker volumes for the video files

#### Create OpenAI API key

- You will need to create a .env in frontend/ with your own OpenAI API key

```
echo "OPENAI_API_KEY=[your API key here]" > .env
```

#### Build Docker Image:

- This extracts the OPENAI_API_KEY from the .env and adds it in when building the docker image

```
docker build --build-arg OPENAI_API_KEY=$(cat .env | grep OPENAI_API_KEY | cut -d '=' -f 2) -t artikulate-docker .
```

#### Start Django server:

```
docker run -p 8002:8002 artikulate-docker
```

### Running without Docker:

- not recommended lol

#### Create Python environment:

```
python3 -m venv venv
```

#### Install FFmpeg:

- Installing on MacOS is easy, Windows requires more configuring

##### MacOS with Homebrew

```
brew install ffmpeg
```

##### Windows

Install at https://ffmpeg.org/download.html, then configure the PATH environment variable. (Good luck on that lol)

#### Install all dependencies locally:

```
install --no-cache-dir -r requirements.txt
```

#### Start Django Server:

```
python frontend/manage.py runserver
```

- This might not even work depending on your local system, had issues running ffmpeg on Windows devices, so just running it on Docker is much easier

### Assets:

- Note, the video files in frontend/assets are not on GitHub, the files are too large.

You can download the video files used in the demo project here: [Download Assets](https://www.mediafire.com/folder/c1wlsvvre7gar/assets)

## How we built it

We first did research on the technologies best to build our project. Since we were working with web scraping and we found some libraries dealing with captioning and audio in Python, that’s the language we decided to use. We used Django as our web framework because we could use HTML while working with dynamic content. We chose not to use Flask, another popular Python web framework, because it was too simplistic for our needs. To get the text content for the videos, we used Selenium and Beautiful Soup Python libraries to web scrape web pages. Selenium worked well with dynamic content and page scrolling while Beautiful Soup had a lot of functionality for parsing HTML to get the text that we needed.

To automatically generate videos with captions, we decided to use moviepy and FFmpeg to edit and overlay video and audio files. We planned the video generation to accept a string representing the script of the video and a given background video to be overlayed over. First, we get the text and call OpenAI’s text-to-speech API to generate the narration (audio file). Then we generated the captions (exported as a MOV video file) using TextClip from moviepy. The issue is that the captions generated were not transparent, so we then just made the background of the captions to be colored solid green (essentially caption video with green-screen). After this, we run an FFmpeg script to find the background video and trim the background video to be the same length as the caption video. Finally, we ran another FFmpeg script to chroma-key the green-screen caption video with the trimmed background video, which removes the green-screen background, making the captions overlayed on top of the background video with the narrated text-to-speech audio.

We created text to speech generation with Open AI. We also used Open AI to generate text similar to reddit posts in different subreddits. We created an auto captioning algorithm based off of syllables and punctuation to better match up the captions and text to speech.

## Challenges we ran into

When starting our project we quickly ran into problems on how we would generate and combine our text-to-speech audio and captions. Many possible options we found had strict limitations or were expensive.

We originally decided to use gTTS to generate the text-to-speech, but it was too simplistic and didn’t allow for much customization. Then we used pyttx3 to generate text-to-speech, but due to deprecated libraries (pyobjc), pyttx3 could not run with Django. Finally, we decided to just use OpenAI’s text-to-speech API to get the text-to-speech audio.

The caption text also needs to be synchronized with the text-to-speech audio. Our first solution was to only have one word being shown at a constant time, but this only worked with pyttx3. Then we decided to split each word parsed into a different audio file and then concatenated them. This was space and memory-inefficient, so we finally used Syllables, a Python library that finds syllables from the given text. This allowed higher precision in parsing, and we wrote an algorithm that has different delay times depending on different punctuations like commas, periods, semicolons, and question marks. This is because OpenAI’s tts would pause briefly when encountering punctuation marks.

Additionally, we had challenges combining our captions and audio video with our background video. Because of the different video formats, we had difficulties combining each of our separate components into one complete synchronized video. We made multiple utility functions that run FFmpeg scripts that convert different extensions to the desired encoding (eg MP4 to MOV, MP3 to WAV).

Another challenge we had was with our file pathing. We struggled to make our Django project access and connect to other Python files outside its directory so we had to switch how we did the text-to-speech for the videos. With the Open AI API, we had issues with the API keys and had to reset them. One of our biggest challenges was getting and installing all of the necessary libraries and packages for our project.

We struggled to make our project compatible with both Mac and Windows so our group could all work together. Half of our group was on Mac with the other half on Windows. This led to some drastically different and complicated installations for some of our libraries (FFmpeg needing to set up environment variables for Windows).

## Accomplishments that we're proud of

We’re proud that we were able to take mostly new technologies and learn them during this weekend to create a functional product. We learned and developed with innovative libraries in a short amount of time, making a mostly realized application.

We’re proud of being able to fully automate the process of creating an interactive video with captions and narration. We were able to generate or web scrape stories, summaries, and content. Then we were able to take the given text and fully automate text-to-speech and text captions from the text. And finally combine and overlay a background video to create a finished interactive video.

## What we learned

Many of the technologies used in Artikulate were new to us prior to this hackathon. We learned to use Django to create our web framework, we learned to web scrape contents, we learned to use Open AI API to generate text and text-to-speech audio, and we learned to run FFmpeg commands in the terminal and scripts in Python using FFmpeg to edit and encode videos.

## What's next for Artikulate

We have only worked on AI generative features and web scraping for Reddit and History.com. Artikulate’s web scraping and AI text generation features could be expanded to other different websites such as Wikipedia or the New York Times to make information more accessible to emerging generations.

Additionally, we’ve made a backend and have it working locally, so we want to expand the project by deploying the project to a custom domain name. Hosting some of the video files take up a lot of storage, so we also want to look into incorporating cloud services like AWS to host most of our assets.
