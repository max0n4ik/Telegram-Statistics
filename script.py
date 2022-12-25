
import re
import os

current_dir = os.getcwd()

files = os.listdir(current_dir)
numUTC = 0
numVoice = 0
numPhoto = 0
numCircle = 0
numGif = 0

for file in files:

    if file.endswith('.html'):
            with open(file, 'r', encoding='utf-8') as f:
            
               content = f.read()

            patternUTC = r'UTC'
            matchesUTC = re.findall(patternUTC, content)
            patternVoice = r'media_voice_message'
            matchesVoice = re.findall(patternVoice, content)
            patternPhoto = r'Photo'
            matchesPhoto = re.findall(patternPhoto, content)
            patternCircle = r'media_video'
            matchesCircle = re.findall(patternCircle, content)
            patternGif = r'Animation'
            matchesGif  = re.findall(patternGif, content)

            numUTC = numUTC + len(matchesUTC)
            numVoice  = numVoice  + len(matchesVoice)
            numPhoto = numPhoto + len(matchesPhoto)
            numCircle = numCircle + len(matchesCircle)
            numGif = numGif + len(matchesGif)




print(f'Сообщений всего: {numUTC}')
print(f'Текстовых сообщений: {numUTC-(numGif + numCircle + numPhoto + numVoice)}')
print(f'Голосовых: {numVoice}')
print(f'Фоток: {numPhoto}')
print(f'Кружочков: {numCircle}')
print(f'Гифок: {numGif}')
print(f'Вся медиа в сумме: {numGif + numCircle + numPhoto + numVoice}')
input("жмяк любую кнопку чтоб закрыть...")
