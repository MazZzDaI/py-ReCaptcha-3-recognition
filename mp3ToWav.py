'''
#from os import path
from pydub import AudioSegment

src = r'./audioSamples/the_community_proactively.mp3'
dst = 'work.wav'

sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")
'''

from pydub import AudioSegment

src = r'./audioSamples/the_community_proactively.mp3'
dst = 'work.wav'

sound = AudioSegment.from_mp3(src)
sound.export(dst, format='wav', codec='pcm')
