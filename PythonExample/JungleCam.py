def Primere():
		sound = str(input())
		t = "Tiger"
		s = "Snake"
		l = "Lion Lion"
		b = "Bird"
		i = 1
		while i <= 4:
			i += 1
			if sound == "Grr":
				sound = l
			elif sound == "Ssss":
				sound = s
			elif sound == "Rawr":
				sound = t
			elif sound == "Chirp":
				sound = b
		print(sound)

Primere()
