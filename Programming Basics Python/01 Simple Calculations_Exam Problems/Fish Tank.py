length_cm = int(input())
width_cm = int(input())
height_im = int(input())
ang_volume = float(input())

volume_cm = length_cm * width_cm * height_im
volume_dm = volume_cm / 1000
free_volume = volume_dm - volume_dm * (ang_volume/100)
print(free_volume)
