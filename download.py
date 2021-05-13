import sys, os

link = input("Youtube link: ")
sim = input("Text similarity: ")
song = input("Song: ")
artist = input("Artist: ")

os.system(f'youtube-dl --extract-audio --audio-format wav -f bestaudio {link}')

files = os.listdir()
for f in files:
	if sim.lower() in f.lower():
		f_split = f.split('-')
		f_split.pop()	
		new_fname = f'YT_{artist} - {song}.wav'
		print(f"New fname: {new_fname}")
		os.system(f"mv '{f}' '{new_fname}'")
