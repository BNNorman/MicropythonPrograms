
import time
import random
from NeoMatrix import neoMatrix
import sys
		
class MatrixDemo:
	def __init__(self):
		self.Matrix=neoMatrix(4,8,8)
		
	def demo(self,loopCount=1):
	
		for loop in range(0,loopCount):
			print("Set random colors")
			for x in range(0,8):
				for y in range(0,8):
					r=random.getrandbits(8)	# binary 0-255
					g=random.getrandbits(8)
					b=random.getrandbits(8)
					
					self.Matrix.setPixel(x,y,(r,g,b))
					self.Matrix.display()
					
			time.sleep(5)
		
			# fade out/in
			# if we fade out to black can we ever get the 
			# color back unless we store values as HSL?
			print("Fade out")
			for brightness in range(10,1):
				self.Matrix.setMatrixPerceivedBrightness(10.0*brightness) # 0-100%
				self.Matrix.display()
				time.sleep(0.5)
			
			print("Fade in")
			for brightness in range(1,10):
				self.Matrix.setMatrixPerceivedBrightness(10.0*brightness) # 0-100%
				self.Matrix.display()
				time.sleep(0.5)
				
		self.Matrix.clear()

MD=MatrixDemo()
print("Start with \nNeoMatrixDemo.MD.demo(5) or")
print("\nMD=NeoMatrixDemo.MatrixDemo()\nMD.demo(5)")