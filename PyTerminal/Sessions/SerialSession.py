from tkinter import Tk
from tkinter import Frame
import serial
from PyTerminal.Sessions.Session import Session


class SerialSession(Session):
    def __init__(self, name, parent: Tk, configuration_data: dict, **kwargs):
        super().__init__(name, parent)
        self.connection = serial.Serial()
        self.connection.port = configuration_data = configuration_data["Port"]
        self.connection.baudrate = configuration_data["Baud_Rate"]
        self.connection.bytesize = convert_byte_size(configuration_data["Data_Bits"])
        self.connection.parity = convert_parity(configuration_data["Parity"])
        self.connection.stopbits = convert_stop_bits(configuration_data["Stop_Bits"])
        self.connection.timeout = configuration_data["Time_Out"]
        self.connection.xonxoff = configuration_data["Xon_Xoff"]
        self.connection.rtscts = configuration_data["Rts_Cts"]
        self.connection.dsrdtr = configuration_data["Dsr_Dtr"]
        self.connection.write_timeout = configuration_data["Write_Timeout"]
        self.connection.inter_byte_timeout = configuration_data["Inter_Byte_Timeout"]
        self.connection.exclusive = configuration_data["Exclusive"]

        self.connection_info = {"Termination_Char": configuration_data["Termination_Char"]}

    def listen_for_messages(self):
        # Threaded out to just listen for messages
        # listen for message
        message_bytes = self.connection.read_until(self.connection_info["Termination_Char"])
        super().on_message_receive_event(message_bytes.decode('utf-8'))


########################
#   Helpers to convert to pyserial enums
########################
def convert_to_pyserial_enum(config_value, conversion_dictionary: dict):
    if config_value not in conversion_dictionary:
        raise ValueError("PySerial is limited to data bit sizes of 5-8 bits")
    return conversion_dictionary[config_value]


def convert_byte_size(config_byte_size):
    pyserial_byte_enum = {5: serial.FIVEBITS, 6: serial.SIXBITS, 7: serial.SEVENBITS, 8: serial.EIGHTBITS}
    return convert_to_pyserial_enum(config_byte_size, pyserial_byte_enum)


def convert_parity(config_parity: str):
    try:
        param = config_parity.lower()
    except AttributeError:
        raise ValueError("Config loaded in a value for parity that wasn't a string. Expected None, Even, Odd, Mark,"
                         "Space, or names")
    parity_enum = {"none": serial.PARITY_NONE, "even": serial.PARITY_EVEN, "odd": serial.PARITY_ODD,
                   "mark": serial.PARITY_MARK, "space": serial.PARITY_SPACE, "names": serial.PARITY_NAMES}
    return convert_to_pyserial_enum(config_parity, parity_enum)


def convert_stop_bits(config_stop_bit: float):
    stop_bit_enum = {1: serial.STOPBITS_ONE, 1.5: serial.STOPBITS_ONE_POINT_FIVE, 2: serial.STOPBITS_TWO}
    return convert_to_pyserial_enum(config_stop_bit, stop_bit_enum)
