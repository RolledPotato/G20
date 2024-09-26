import openai
openai.api_key='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'

file=open("ZOOM0015.wav",'rb')
result = openai.Audio.transcribe('whisper-1',file)
print(result["text"])
