

# for the human eye
# perceived brightness= sqrt(measured brightness)
#
# pb^2=mb
#
# if pb has a range 0 to 100% then mb ranges 0 to 10000
#
# so, for 50% preceived brightness mb=50^2=2500 which means
# an LED measured brightness needs to be set at (2500/10000) = 0.25
# which is 25% on a scale 0 to 1
#
#

import neopixel
import colorsys
import machine

class neoMatrix():

	def __init__(self,pin,w,h):
		self.w=w
		self.h=h
		self.size=w*h
		self.np=neopixel.NeoPixel(machine.Pin(pin),w*h)
		self.clear()
		
	def setPixel(self,x,y,color):
		# color is a tuple (r,g,b)
		if x>self.w: return
		if y>self.h: return
		
		self.np[x+y*self.w]=color
		
	def setAll(self,color):
		for p in range(0,self.size):
			self.np[p]=color

	# as seen by the human eye
	# brightness range 0-100%
	def setMatrixPerceivedBrightness(self,brightness):
		mb=brightness*brightness/10000.0
		for p in range(0,self.size):
			(r,g,b)=self.np[p]
			# colorsys uses floating point
			(h,l,s)=colorsys.rgb_to_hls(r/255.0,g/255.0,b/255.0)
			(r,g,b)=colorsys.hls_to_rgb(h,mb,s)
			self.np[p]=(int(r*255),int(g*255),int(b*255))

	# brightness range 0-255
	def setMatrixBrightness(self,brightness):
		for p in range(0,self.size):
			(r,g,b)=self.np[p]
			# colorsys uses floating point
			(h,l,s)=colorsys.rgb_to_hls(r/255.0,g/255.0,b/255.0)
			(r,g,b)=colorsys.hls_to_rgb(h,brightness/255.0,s)
			self.np[p]=(int(r*255),int(g*255),int(b*255))

	# brightness range 0..100%
	def setMatrixBrightnessPercent(self,brightness):
		for p in range(0,self.size):
			(r,g,b)=self.np[p]
			# colorsys uses floating point
			(h,l,s)=colorsys.rgb_to_hls(r/255.0,g/255.0,b/255.0)
			(r,g,b)=colorsys.hls_to_rgb(h,brightness/100.0,s)
			self.np[p]=(int(r*255),int(g*255),int(b*255))
	
	# as seen by the human eye	
	# brightness range 0..100
	def setPixelPerceivedBrightness(self,x,y,brightness):
		mb=brightness*brightness/10000.0
		p=x+y*self.w
		(r,g,b)=self.np[p]
		(h,l,s)=colorsys.rgb_to_hls(r/255.0,g/255.0,b/255.0)
		(r,g,b)=colorsys.hls_to_rgb(h,mb,s)
		self.np[p]=(int(r*255),int(g*255),int(b*255))
	
	# brightness 0..255
	def setPixelBrightness(self,x,y,brightness):
		p=x+y*self.w
		(r,g,b)=self.np[p]
		(h,l,s)=colorsys.rgb_to_hls(r/255.0,g/255.0,b/255.0)
		(r,g,b)=colorsys.hls_to_rgb(h,brightness/255.0,s)
		self.np[p]=(int(r*255),int(g*255),int(b*255))
			
	
	# brightness 0..100%
	def setPixelBrightnessPercent(self,x,y,brightness):
		p=x+y*self.w
		(r,g,b)=self.np[p]
		(h,l,s)=colorsys.rgb_to_hls(r/255.0,g/255.0,b/255.0)
		(r,g,b)=colorsys.hls_to_rgb(h,brightness/100.0,s)
		self.np[p]=(int(r*255),int(g*255),int(b*255))
		
	def display(self):
		self.np.write()
		
	def clear(self):
		self.setAll((0,0,0))
		self.np.write()
		