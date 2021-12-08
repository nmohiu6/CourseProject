from youtube_transcript_api import YouTubeTranscriptApi
  
# assigning srt variable with the list
# of dictonaries obtained by the get_transcript() function
srt = YouTubeTranscriptApi.get_transcript("z-EtmaFJieY")

# print(type(srt[0]['text']))

phrases = ""

for i in range(len(srt)):
    encode_text = srt[i]['text'].encode(encoding='utf-8',errors='replace')
    decode_text = encode_text.decode('utf-8')
    print(srt[i]['text'])
    phrases = phrases + ' ' + decode_text
    # phrases = phrases + ' ' + srt[i]['text']

with open('luke_dillon.txt', 'w') as f:
    f.write(phrases)