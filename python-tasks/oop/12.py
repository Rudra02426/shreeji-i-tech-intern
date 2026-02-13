### Task 12: Multiple Inheritance
class Camera:
	def click(self):
		print("click the photo")
class MusicPlayer:
	def play(self):
		print("play the music")
class Smartphone(Camera, MusicPlayer):
	def use(self):
		print("smart phone features ")
phn= Smartphone()
phn.click()
phn.play()
phn.use()