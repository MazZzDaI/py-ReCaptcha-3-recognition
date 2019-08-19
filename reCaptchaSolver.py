#https://patrickhlauke.github.io/recaptcha/

import azure.cognitiveservices.speech as speechsdk
from pydub import AudioSegment

def recognizeSpeech(wavFilePath):
    speech_key, service_region = "123", "northeurope"
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    audio_config = speechsdk.AudioConfig(filename=wavFilePath)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    result = speech_recognizer.recognize_once()

    # Checks result.
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(result.text))
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(result.no_match_details))
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))


def mp3toWav(inMp3Filename, outWavFilename):
    sound = AudioSegment.from_mp3(inMp3Filename)
    sound.export(outWavFilename, format='wav', codec='pcm')

wavFilePath = 'work.wav'
mp3FilePath = r'.\audioSamples\andDesignSupportLine.mp3'
mp3toWav(wavFilePath, mp3FilePath)

recognizeSpeech(wavFilePath)