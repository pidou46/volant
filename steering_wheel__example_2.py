# MicroPython Human Interface Device library
# Copyright (C) 2021 H. Groefsema
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


# Implements a BLE HID SteeringWheel
import uasyncio as asyncio
from machine import SoftSPI, Pin, I2C
from hid_extra_services import SteeringWheel
#from as5600 import AS5600

#AS5600_id = const(0x36)  #Device ID

class Device:
    def __init__(self, name="Steering Wheel"):
        # Define state
        self.axes = (0, 0)
        self.updated = False
        self.active = True

        # Define buttons
        self.pin_forward = Pin(23, Pin.IN)
        self.pin_reverse = Pin(16, Pin.IN)
        self.pin_left = Pin(17, Pin.IN)
        self.pin_right = Pin(5, Pin.IN)
        #self.i2c = I2C(scl=Pin(18),sda=Pin(19),freq=400000)
        #self.volant = AS5600(self.i2c,AS5600_id)

        # Create our device
        self.SteeringWheel = SteeringWheel(name)
        # Set a callback function to catch changes of device state
        self.SteeringWheel.set_state_change_callback(self.SteeringWheel_state_callback)

    # Function that catches device status events
    def SteeringWheel_state_callback(self):
        if self.SteeringWheel.get_state() is SteeringWheel.DEVICE_IDLE:
            return
        elif self.SteeringWheel.get_state() is SteeringWheel.DEVICE_ADVERTISING:
            return
        elif self.SteeringWheel.get_state() is SteeringWheel.DEVICE_CONNECTED:
            return
        else:
            return

    def advertise(self):
        self.SteeringWheel.start_advertising()

    def stop_advertise(self):
        self.SteeringWheel.stop_advertising()

    async def advertise_for(self, seconds=30):
        self.advertise()

        while seconds > 0 and self.SteeringWheel.get_state() is SteeringWheel.DEVICE_ADVERTISING:
            await asyncio.sleep(1)
            seconds -= 1

        if self.SteeringWheel.get_state() is SteeringWheel.DEVICE_ADVERTISING:
            self.stop_advertise()

    # Input loop
    async def gather_input(self):
        while self.active:
            prevaxes = self.axes
            #self.axes = (int((self.volant.ANGLE-2048)/16), self.pin_forward.value() * 127 - self.pin_reverse.value() * 127)
            self.axes = (self.pin_left.value() * 127 - self.pin_right.value() * 127, self.pin_forward.value() * 127 - self.pin_reverse.value() * 127)
            self.updated = self.updated or not (prevaxes == self.axes)  # If updated is still True, we haven't notified yet
            await asyncio.sleep_ms(50)

    # Bluetooth device loop
    async def notify(self):
        while self.active:
            # If connected, set axes and notify
            # If idle, start advertising for 30s or until connected
            if self.updated:
                if self.SteeringWheel.get_state() is SteeringWheel.DEVICE_CONNECTED:
                    self.SteeringWheel.set_axes(self.axes[0], self.axes[1])
                    self.SteeringWheel.notify_hid_report()
                elif self.SteeringWheel.get_state() is SteeringWheel.DEVICE_IDLE:
                    await self.advertise_for(30)
                self.updated = False

            if self.SteeringWheel.get_state() is SteeringWheel.DEVICE_CONNECTED:
                await asyncio.sleep_ms(50)
            else:
                await asyncio.sleep(2)

    async def co_start(self):
        # Start our device
        if self.SteeringWheel.get_state() is SteeringWheel.DEVICE_STOPPED:
            self.SteeringWheel.start()
            self.active = True
            await asyncio.gather(self.advertise_for(30), self.gather_input(), self.notify())

    async def co_stop(self):
        self.active = False
        self.SteeringWheel.stop()

    def start(self):
        asyncio.run(self.co_start())

    def stop(self):
        asyncio.run(self.co_stop())

    # Test routine
    async def test(self):
        while not self.SteeringWheel.is_connected():
            await asyncio.sleep(5)

        await asyncio.sleep(5)
        self.SteeringWheel.set_battery_level(50)
        self.SteeringWheel.notify_battery_level()
        await asyncio.sleep_ms(500)

        for i in range(30):
            self.SteeringWheel.set_axes(100,100)
            self.SteeringWheel.set_buttons(1)
            self.SteeringWheel.notify_hid_report()
            await asyncio.sleep_ms(500)

            self.SteeringWheel.set_axes(100,-100)
            self.SteeringWheel.set_buttons(b3=1)
            self.SteeringWheel.notify_hid_report()
            await asyncio.sleep_ms(500)

            self.SteeringWheel.set_axes(-100,-100)
            self.SteeringWheel.set_buttons()
            self.SteeringWheel.notify_hid_report()
            await asyncio.sleep_ms(500)

            self.SteeringWheel.set_axes(-100,100)
            self.SteeringWheel.set_buttons(b2=1)
            self.SteeringWheel.notify_hid_report()
            await asyncio.sleep_ms(500)

        self.SteeringWheel.set_axes(0,0)
        self.SteeringWheel.set_buttons()
        self.SteeringWheel.notify_hid_report()
        await asyncio.sleep_ms(500)

        self.SteeringWheel.set_battery_level(100)
        self.SteeringWheel.notify_battery_level()
        
        self.SteeringWheel.stop()

    async def co_start_test(self):
        self.SteeringWheel.start()
        await asyncio.gather(self.advertise_for(30), self.test())

    # start test
    def start_test(self):
        asyncio.run(self.co_start_test())

if __name__ == "__main__":
    d = Device()
    d.start_test()
