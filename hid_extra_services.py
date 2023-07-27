from hid_services import *


# Class that represents the Joystick service
class SteeringWheel(HumanInterfaceDevice):
    def __init__(self, name="Bluetooth SteeringWheel"):
        super(SteeringWheel, self).__init__(name)  # Set up the general HID services in super
        self.device_appearance = 960          # Device appearance ID, 960 = Generic Human Interface Device

        self.HIDS = (                         # Service description: describes the service and how we communicate
            UUID(0x1812),                     # Human Interface Device
            (
                (UUID(0x2A4A), F_READ),       # HID information
                (UUID(0x2A4B), F_READ),       # HID report map
                (UUID(0x2A4C), F_WRITE),      # HID control point
                (UUID(0x2A4D), F_READ_NOTIFY, ((UUID(0x2908), ATT_F_READ),)),  # HID report / reference
                (UUID(0x2A4E), F_READ_WRITE), # HID protocol mode
            ),
        )

        # fmt: off
#         self.HID_INPUT_REPORT = bytes([    # Report Description: describes what we communicate
#             0x05, 0x02,                    # USAGE_PAGE (Simulation Controls)
#             0x09, 0x04,                    # USAGE (Automobile Simulation Device)
#             0xa1, 0x01,                    # COLLECTION (Application)
#             0x85, 0x01,                    #   REPORT_ID (1)
#             0xa1, 0x00,                    #   COLLECTION (Physical)
#             0x09, 0xc8,                    #     USAGE (Steering)
#             0x09, 0xc4,                    #     USAGE (Accelerator)
#             0x15, 0x81,                    #     LOGICAL_MINIMUM (-127)
#             0x25, 0x7f,                    #     LOGICAL_MAXIMUM (127)
#             0x75, 0x08,                    #     REPORT_SIZE (8)
#             0x95, 0x02,                    #     REPORT_COUNT (2)
#             0x81, 0x02,                    #     INPUT (Data,Var,Abs)
#             0x05, 0x09,                    #     USAGE_PAGE (Button)
#             0x29, 0x08,                    #     USAGE_MAXIMUM (Button 8)
#             0x19, 0x01,                    #     USAGE_MINIMUM (Button 1)
#             0x95, 0x08,                    #     REPORT_COUNT (8)
#             0x75, 0x01,                    #     REPORT_SIZE (1)
#             0x25, 0x01,                    #     LOGICAL_MAXIMUM (1)
#             0x15, 0x00,                    #     LOGICAL_MINIMUM (0)
#             0x81, 0x02,                    #     Input (Data, Variable, Absolute)
#             0xc0,                          #   END_COLLECTION
#             0xc0                           # END_COLLECTION
#         ])
        # fmt: on
        
#         # fmt: off
#         self.HID_INPUT_REPORT = bytes([    # Report Description: describes what we communicate
#             0x05, 0x01,                    # USAGE_PAGE (Generic Desktop)
#             0x09, 0x05,                    # USAGE (Game Pad)
#             0xa1, 0x01,                    # COLLECTION (Application)
#             0xa1, 0x00,                    # 	COLLECTION (Physical)
#             0x05, 0x09,                    # 		USAGE_PAGE (Button)            
#             0x19, 0x01,                    #     	USAGE_MINIMUM (Button 1)
#             0x29, 0x08,                    #     	USAGE_MAXIMUM (Button 8)            
#             0x15, 0x00,                    #     	LOGICAL_MINIMUM (0)
#             0x25, 0x01,                    #     	LOGICAL_MAXIMUM (1)
#             0x95, 0x08,                    #     	REPORT_COUNT (8)
#             0x75, 0x01,                    #     	REPORT_SIZE (1)
#             0x81, 0x06,                    #     	INPUT (Data,Var,Rel)
#             0x05, 0x02,                    # 		USAGE_PAGE (Simulation Controls)
#             0x09, 0xc8,                    # 		USAGE (Steering)
#             0x15, 0x81,                    #     	LOGICAL_MINIMUM (-127)
#             0x25, 0x7f,                    #     	LOGICAL_MAXIMUM (127)
#             0x25, 0x7f,                    #     	PHYSICAL_MAXIMUM (127)
#             0x15, 0x81,                    #     	PHYSICAL_MINIMUM (-127)
#             0x75, 0x08,                    #     	REPORT_SIZE (8)
#             0x95, 0x01,                    #     	REPORT_COUNT (1)
#             0x81, 0x06,                    #     	INPUT (Data,Var,Rel)
#             0x09, 0xc4,                    # 		USAGE (Accelerator)
#             0x09, 0xc5,                    # 		USAGE (Brake)
#             0x09, 0xc6,                    #	USAGE (Clutch)
#             0x15, 0x00,                    #    LOGICAL_MINIMUM (0)
#             0x26, 0xff, 0x00,              #    LOGICAL_MAXIMUM (255)
#             0x75, 0x08,                    #    REPORT_SIZE (8)
#             0x95, 0x03,                    #    REPORT_COUNT (3)
#             0x35, 0x00,                    #     	PHYSICAL_MAXIMUM (0)
#             0x46, 0xff, 0x00,              #     	PHYSICAL_MINIMUM (255)
#             0x81, 0x02,                    #	INPUT (Data,Var,Abs)
#             0xc0,                          #   END_COLLECTION
#             0xc0                           # END_COLLECTION
#         ])
#         # fmt: on


        # fmt: off
        self.HID_INPUT_REPORT = bytes([    # Report Description: describes what we communicate
            0x05, 0x01,                    # USAGE_PAGE (Generic Desktop)
            0x09, 0x05,                    # USAGE (Game Pad)
            0xa1, 0x01,                    # COLLECTION (Application)
            0xa1, 0x00,                    # 	COLLECTION (Physical)
            0x05, 0x09,                    # 		USAGE_PAGE (Button)            
            0x19, 0x01,                    #     	USAGE_MINIMUM (Button 1)
            0x29, 0x08,                    #     	USAGE_MAXIMUM (Button 8)            
            0x15, 0x00,                    #     	LOGICAL_MINIMUM (0)
            0x25, 0x01,                    #     	LOGICAL_MAXIMUM (1)
            0x95, 0x08,                    #     	REPORT_COUNT (8)
            0x75, 0x01,                    #     	REPORT_SIZE (1)
            0x81, 0x06,                    #     	INPUT (Data,Var,Rel)
            0x05, 0x02,                    # 		USAGE_PAGE (Simulation Controls)
            0x09, 0xc8,                    # 		USAGE (Steering)
            0x15, 0x81,                    #     	LOGICAL_MINIMUM (-127)
            0x25, 0x7f,                    #     	LOGICAL_MAXIMUM (127)
            0x25, 0x7f,                    #     	PHYSICAL_MAXIMUM (127)
            0x15, 0x81,                    #     	PHYSICAL_MINIMUM (-127)
            0x75, 0x08,                    #     	REPORT_SIZE (8)
            0x95, 0x01,                    #     	REPORT_COUNT (1)
            0x81, 0x06,                    #     	INPUT (Data,Var,Rel)
            0x09, 0xc4,                    # 		USAGE (Accelerator)
            0x09, 0xc5,                    # 		USAGE (Brake)
            0x09, 0xc6,                    #		USAGE (Clutch)
            0x15, 0x00,                    #    	LOGICAL_MINIMUM (0)
            0x26, 0xff, 0x00,              #    	LOGICAL_MAXIMUM (255)
            0x75, 0x08,                    #    	REPORT_SIZE (8)
            0x95, 0x03,                    #    	REPORT_COUNT (3)
            0x35, 0x00,                    #     	PHYSICAL_MAXIMUM (0)
            0x46, 0xff, 0x00,              #     	PHYSICAL_MINIMUM (255)
            0x81, 0x02,                    #	INPUT (Data,Var,Abs)
            0xc0,                          #   END_COLLECTION
            0xc0                           # END_COLLECTION
        ])
        # fmt: on
        
        

        # Define the initial SteeringWheel state
        self.steering = 0
        self.accelerator = 0
        self.brake = 0

        self.button1 = 0
        self.button2 = 0
        self.button3 = 0
        self.button4 = 0
        self.button5 = 0
        self.button6 = 0
        self.button7 = 0
        self.button8 = 0

        self.services = [self.DIS, self.BAS, self.HIDS]  # List of service descriptions

    # Overwrite super to register HID specific service
    # Call super to register DIS and BAS services
    def start(self):
        super(SteeringWheel, self).start()  # Start super

        print("Registering services")
        # Register services and get read/write handles for all services
        handles = self._ble.gatts_register_services(self.services)
        # Write the values for the characteristics
        self.write_service_characteristics(handles)

        # Create an Advertiser
        # Only advertise the top level service, i.e., the HIDS
        self.adv = Advertiser(self._ble, [UUID(0x1812)], self.device_appearance, self.device_name)

        print("Server started")

    # Overwrite super to write HID specific characteristics
    # Call super to write DIS and BAS characteristics
    def write_service_characteristics(self, handles):
        super(SteeringWheel, self).write_service_characteristics(handles)

        # Get the handles from the hids, the third service after DIS and BAS
        # These correspond directly to self.HIDS
        (h_info, h_hid, _, self.h_rep, h_d1, h_proto,) = handles[2]

        # Pack the initial SteeringWheel state as described by the input report
        b = self.button1 + self.button2 * 2 + self.button3 * 4 + self.button4 * 8 + self.button5 * 16 + self.button6 * 32 + self.button7 * 64 + self.button8 * 128
        #state = struct.pack("bbB", self.accelerator, self.steering, b)
        state = struct.pack("BbBB", b, self.steering, self.accelerator, self.brake)


        print("Writing hid service characteristics")
        # Write service characteristics
        self._ble.gatts_write(h_info, b"\x01\x01\x00\x02")     # HID info: ver=1.1, country=0, flags=normal
        self._ble.gatts_write(h_hid, self.HID_INPUT_REPORT)    # HID input report map
        self._ble.gatts_write(self.h_rep, state)               # HID report
        self._ble.gatts_write(h_d1, struct.pack("<BB", 1, 1))  # HID reference: id=1, type=input
        self._ble.gatts_write(h_proto, b"\x01")                # HID protocol mode: report

    # Overwrite super to notify central of a hid report
    def notify_hid_report(self):
        if self.is_connected():
            # Pack the joystick state as described by the input report
            b = self.button1 + self.button2 * 2 + self.button3 * 4 + self.button4 * 8 + self.button5 * 16 + self.button6 * 32 + self.button7 * 64 + self.button8 * 128
            #state = struct.pack("BbB", b, self.steering, self.accelerator )
            state = struct.pack("BbBB", b, self.steering, self.accelerator, self.brake)

            print("Notify with report: ", struct.unpack("BbBB", state))
            # Notify central by writing to the report handle
            self._ble.gatts_notify(self.conn_handle, self.h_rep, state)

    def set_axes(self, steering=0, accelerator=0, brake=0):
        if steering > 127:
            steering = 127
        elif steering < -127:
            steering = -127

        if accelerator > 255:
            accelerator = 255
        elif accelerator < 0:
            accelerator = 0

        if brake > 255:
            brake = 255
        elif brake < 0:
            brake = 0

        self.steering = steering
        self.accelerator = accelerator
        self.brake = brake

    def set_buttons(self, b1=0, b2=0, b3=0, b4=0, b5=0, b6=0, b7=0, b8=0):
        self.button1 = b1
        self.button2 = b2
        self.button3 = b3
        self.button4 = b4
        self.button5 = b5
        self.button6 = b6
        self.button7 = b7
        self.button8 = b8
