#! python3
# -*- coding:utf-8 -*-
#this code's owner is google.
#https://cloud.google.com/speech-to-text/docs/sync-recognize?hl=ja#speech-sync-recognize-python

from google.cloud import speech
from google.cloud.speech import RecognitionConfig
from google.cloud.speech_v1p1beta1 import RecognitionConfig as beta1Config #for MP3.
import io
import sys, os
from pathlib import Path

authJsonFile = '/root/stellar-aurora-271708-a1a7a4ae1954.json'
os.environ.setdefault('GOOGLE_APPLICATION_CREDENTIALS',authJsonFile)

def sample_recognize(local_file_path):
    
    if local_file_path == None or Path(local_file_path).exists() == False:
        print("please input target image file on first argument.")
        sys.exit(1)
    """
    Transcribe a short audio file using synchronous speech recognition

    Args:
      local_file_path Path to local audio file, e.g. /path/audio.wav
    """

    client = speech.SpeechClient()

    # local_file_path = 'resources/brooklyn_bridge.raw'

    # The language of the supplied audio
    language_code = "en-US"
    #language_code = "ja-JP"

    # Sample rate in Hertz of the audio data sent
    #sample_rate_hertz = 16000
    sample_rate_hertz = 44100
    
    #alternative num
    max_alternatives = 1

    # Encoding of audio data sent. This sample sets this explicitly.
    # This field is optional for FLAC and WAV audio formats.
    #encoding = RecognitionConfig.AudioEncoding.LINEAR16
    encoding = beta1Config.AudioEncoding.MP3
    config = {
        "language_code": language_code,
        "sample_rate_hertz": sample_rate_hertz,
        "encoding": encoding,
        "max_alternatives": max_alternatives,
        "enable_word_time_offsets":True
    }
    with io.open(local_file_path, "rb") as f:
        content = f.read()
    audio = {"content": content}

    response = client.recognize(config=config, audio=audio)
    for result in response.results:
        # First alternative is the most probable result
        alternative = result.alternatives[0]
        print(u"Transcript: {}".format(alternative.transcript))
        print(u"Confidence: {}".format(alternative.confidence))
        
        for word_info in alternative.words:
            word = word_info.word
            start_time = word_info.start_time
            end_time = word_info.end_time
            
            print(f"Word: {word}, start_time: {start_time.total_seconds()}, end_time: {end_time.total_seconds()}")
            
        print("")
        

sample_recognize(sys.argv[1])
