import sys
from gtts import gTTS
from preferredsoundplayer import soundplay

def convert_hours(hour):
 if hour == 1:
    return 'ZERO ONE'
 elif hour == 2:
    return 'ZERO TWO'
 elif hour == 3:
    return 'ZERO THREE'
 elif hour == 4:
    return 'ZERO FOUR'
 elif hour == 5:
    return 'ZERO FIVE'
 elif hour == 6:
    return 'ZERO SIX'
 elif hour == 7:
    return 'ZERO SEVEN'
 elif hour == 8:
    return 'ZERO EIGHT'
 elif hour == 9:
    return 'ZERO NINE'
 elif hour == 10:
    return 'TEN'
 elif hour == 11:
    return 'ELEVEN'
 elif hour == 12:
    return 'TWELVE'
 elif hour == 13:
    return 'THIRTEEN'
 elif hour == 14:
    return 'FORTEEN'
 elif hour == 15:
    return 'FIFTEEN'
 elif hour == 16:
    return 'SIXTEEN'
 elif hour == 17:
    return 'SEVENTEEN'
 elif hour == 18:
    return 'EIGHTEENT'
 elif hour == 19:
    return 'NINETEEN'
 elif hour == 20:
    return 'TWENTY'
 elif hour == 21:
    return 'TWENTY ONE'
 elif hour == 22:
    return 'TWENTY TWO'
 elif hour == 23:
    return 'TWENTY THREE'

def convert_minutes(minutes):
 if minutes == 0:
    return " "
 elif minutes == 1:
    return "ONE"
 elif minutes == 2:
    return "TWO"
 elif minutes == 3:
    return "THREE"
 elif minutes == 4:
    return "FOUR"
 elif minutes == 5:
   return "FIVE"
 elif minutes == 6:
    return "SIX"
 elif minutes == 7:
    return "SEVEN"
 elif minutes == 8:
    return "EIGHT"
 elif minutes == 9:
    return "NINE"
 elif minutes == 10:
    return "TEN"
 elif minutes == 11:
    return "ELEVEN"
 elif minutes == 12:
    return "TWELVE"
 elif minutes == 13:
    return "THIRTEEN"
 elif minutes == 14:
    return "FORTEEN"
 elif minutes == 15:
    return "FIFTEEN"
 elif minutes == 16:
    return "SIXTEEN"
 elif minutes == 17:
    return "SEVENTEEN"
 elif minutes == 18:
    return "EIGHTEEN"
 elif minutes == 19:
    return "NINTEEN"
 elif minutes == 20:
    return "TWENTY"
 elif minutes == 1:
    return "TWENTY ONE"
 elif minutes == 22:
    return "TWENTY TWO"
 elif minutes == 23:
    return "TWENTY THREE"
 elif minutes == 24:
    return "TWENTY FOUR"
 elif minutes == 25:
    return "TWENTY FIVE"
 elif minutes == 26:
    return "TWENTY SIX"
 elif minutes == 27:
    return "TWENTY SEVEN"
 elif minutes == 28:
    return "TWENTY EIGHT"
 elif minutes == 29:
    return "TWENTY NINE"
 elif minutes == 30:
    return "THIRTY"
 elif minutes == 31:
    return "THIRTY ONE"
 elif minutes == 32:
    return "THIRTY TWO"
 elif minutes == 33:
    return "THIRTY THREE"
 elif minutes == 34:
    return "THIRTY FOUR"
 elif minutes == 35:
    return "THIRTY FIVE"
 elif minutes == 36:
    return "THIRTY SIX"
 elif minutes == 37:
    return "THIRTY SEVEN"
 elif minutes == 38:
     return "THIRTY EIGHT"
 elif minutes == 39:
    return "THIRTY NINE"
 elif minutes == 40:
    return "FORTY"
 elif minutes == 41:
    return "FORTY ONE"
 elif minutes == 42:
    return "FORTY TWO"
 elif minutes == 43:
    return "FORTY THREE"
 elif minutes == 44:
    return "FORTY FOUR"
 elif minutes == 45:
    return "FORTY FIVE"
 elif minutes == 46:
    return "FORTY SIX"
 elif minutes == 47:
    return "FORTY SEVEN"
 elif minutes == 48:
    return "FORTY EIGHT"
 elif minutes == 49:
    return "FORTY NINE"
 elif minutes == 50:
    return "FIFTY"
 elif minutes == 51:
    return "FIFTY ONE"
 elif minutes == 52:
    return "FIFTY TWO"
 elif minutes == 53:
    return "FIFTY THREE"
 elif minutes == 54:
    return "FIFTY FOUR"
 elif minutes == 55:
    return "FIFTY FIVE"
 elif minutes == 56:
    return "FIFTY SIX"
 elif minutes == 57:
    return "FIFTY SEVEN"
 elif minutes == 58:
    return "FIFTY EIGHT"
 elif minutes == 59:
    return "FIFTY NINE"

def main():
 
 if len(sys.argv) < 3 or len(sys.argv) > 3 :
        print('You need to provide command line inputs.')
        sys.exit()

 military_time = sys.argv[1]
 
 if len(sys.argv) == 3: 
  accent = sys.argv[2].lower()
 else:
    accent == 'USA'

 try:
  military_time = int(military_time)
 except ValueError:
   print("Invalid 1st command line argument. Should contain only digits.")
   sys.exit()

 hour = military_time // 100
 minutes = military_time % 100

 if hour > 23 or hour <0:
    print('Invalid 1st command line argument. Hours cannot be more than 23')
    sys.exit()
 elif minutes <0 or minutes >59:
    print('Invalid 1st command line argument. Minutes cannot be more than 59')
    sys.exit()
 else: 
   final_phrase = convert_hours(hour) + " HUNDRED " + convert_minutes(minutes) + " HOURS "
   print(final_phrase)
   
 if accent == 'aus':
  audio = gTTS(text=final_phrase, lang='en', tld = 'com.au')
  audio.save("f.mp3")
  soundplay("./f.mp3")
 elif accent == 'ind':
  audio = gTTS(text=final_phrase, lang='en', tld = 'co.in')
  audio.save("f.mp3")
  soundplay("./f.mp3")
 elif accent == 'usa':
  audio = gTTS(text=final_phrase, lang='en', tld = 'com')
  audio.save("f.mp3")
  soundplay("./f.mp3")
 else:
    print('Invalid 2nd argument. Must be one of IND, AUS, USA')

main()
