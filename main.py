import winsound

sound_path = "ts.wav"

while True:
    key = int(input(":-"))
    if key == 1:
        break
    if key == 2:
        winsound.PlaySound(sound_path, winsound.SND_ASYNC)
        print("printed")
    if key == 3:
        winsound.PlaySound(sound_path,winsound.SND_ASYNC)



