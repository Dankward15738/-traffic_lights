#
# MicroPython pcf8574 and pcf8574A I2C interface
#
# The MIT License (MIT)
#
# 2024  Dankward Nuerenberg
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# Sample code sections for ESP pin assignments
#
# All Adressport of pcf8574 set to GND
#
#
# from machine import I2C,Pin
# from pcf8574 import PCF8574
# i2c = I2C(1,scl=Pin(22),sda=Pin(21))
# mypcf = PCF8574(0x20,i2c)
# ## all the Ports set to GND
# mypcf.setbit(6) # possible numbers (0-7)
# ## Bit 6 is HIGH
# mypcf.resetbit(6)
# ## Bit 6 is now LOW
class PCF8574():
    def __init__(self,address,i2c):
        self.address = address
        self.temp = bytearray(1)
        self.i2c = i2c
        self.status = 0b00000000
        self.aktualisiereStatus()
        
    def setbit(self,bit):
        zahl = 0b00000001 << bit
        self.status = self.status | zahl
        self.aktualisiereStatus()
     
    def resetbit(self,bit):
        zahl = 0b00000001 << bit
        zahl = ~zahl
        self.status = self.status & zahl
        self.aktualisiereStatus()
    
    def getbit(self,bit):
        datainput = self.i2c.readfrom(self.address,1)
        zahl = 0b00000001 << bit
        if zahl & datainput > 0:
            ausgabe = 1
        else:
            ausgabe = 0
    
        return ausgabe
    
    def aktualisiereStatus(self):
       
        self.temp[0] = self.status
        self.i2c.writeto(self.address,self.temp)
        
