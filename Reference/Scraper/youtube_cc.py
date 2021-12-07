from youtube_transcript_api import YouTubeTranscriptApi
  
# assigning srt variable with the list
# of dictonaries obtained by the get_transcript() function
srt = YouTubeTranscriptApi.get_transcript("Mho3LleTshg")
  
phrases = ""

for i in range(len(srt)):
    phrases = phrases + ' ' + srt[i]['text']

with open('luke_dillon.txt', 'w') as f:
    f.write(phrases)