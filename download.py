import sys, os

assert len(sys.argv) == 3

os.system(f'youtube-dl --extract-audio --audio-format wav -f bestaudio {sys.argv[1]}')

files = os.listdir()
for f in files:
	if sys.argv[2] in f.lower():
		f_split = f.split('-')
		f_split.pop()	
		new_fname = 'YT_' + '-'.join(f_split) + '.wav'
		os.system(f"mv '{f}' '{new_fname}'")
