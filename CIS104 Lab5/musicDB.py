song = [] #my list of songs
count = 0

def addsong(title,artist,album):
    song = dict(Title=title, Artist=artist, Album=album) #create a song record
    songs.append(song) #add it to the list
    
def GetSongNumber(number):
    try:
        int(number)
    except:
        return None
    if(number < 1):
        retun None
    if(number // 1) > songs.count):
         return None
    else:
        return songs[(number // 1) - 1]





        
