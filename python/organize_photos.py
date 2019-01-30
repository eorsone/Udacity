import os
def extract_place(filename):
	return filename.split("_")[1]

def make_directory(locations):
	for each in locations:
		os.mkdir(each)

def organize_photos(photo):

	os.chdir(photo)
	originals = os.listdir()
	places = []
	for filename in originals:
		place = extract_place(filename)
		if place not in places:
			places.append(place)
		
	make_directory(places)

	for filename in originals:
		place = extract_place(filename)
		os.rename(filename, os.path.join(place, filename))


organize_photos("Photos")
