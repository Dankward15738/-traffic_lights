#
# MicroPython pcf8574 and pcf8574A I2C interface  and the LEDs red yellow and green
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
# Hardware:
# PORTs at pcf8574 : color of LED
# 4                :  red
# 5                :  yellow
# 6                :  green

from pcf8574 import PCF8574

class  Ampel(PCF8574):
    def __init__(self,address,i2c,re=4,ye=5,gr=6):
        super().__init__(address,i2c)
        self.red = re
        self.yellow = ye
        self.green = gr
    def setred(self):
        self.setbit(self.red)
        self.resetbit(self.yellow)
        self.resetbit(self.green)
    def setyellow(self):
        self.resetbit(self.red)
        self.setbit(self.yellow)
        self.resetbit(self.green)
    def setgreen(self):
        self.resetbit(self.red)
        self.resetbit(self.yellow)
        self.setbit(self.green)
    def setredyellow(self):
        self.setbit(self.red)
        self.setbit(self.yellow)
        self.resetbit(self.green)
    def setgreenyellow(self):
        self.resetbit(self.red)
        self.setbit(self.yellow)
        self.setbit(self.green)
    def setaus(self):
        self.resetbit(self.red)
        self.resetbit(self.yellow)
        self.resetbit(self.green)