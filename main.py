import win32com.client, time
from pypresence import Presence

client = "874807932800348233"
o = win32com.client.Dispatch("iTunes.Application")

client_id = "885302124995575938" 
RPC = Presence(client_id)
RPC.connect()

while True:
    print(o.CurrentTrack.Name)
    print(o.CurrentTrack.Artist)
    print(o.PlayerState)
    if o.PlayerState == 1: # if playing
        name = "πΆ Track: " + o.CurrentTrack.Name + " πΆ"
        artist = "π§βπ€βπ§ Artist: " + o.CurrentTrack.Artist + " π§βπ€βπ§"
    if o.PlayerState == 0: # if not playing
        name = "βΈοΈ Paused βΈοΈ"
        artist = "βΈοΈ Paused βΈοΈ"
    RPC.update(state=artist, details=name, large_text="Listening to Apple Music", large_image="amusic")
    
    time.sleep(2)
RPC.close()