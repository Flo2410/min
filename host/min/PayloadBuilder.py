from numpy import uint, float32, float64, uint8, frombuffer
import struct

class PayloadBuilder:
    """
    The PayloadBuilder class allows for simple building of a min payload.
    """

    __payload: list[uint8]

    def __init__(self) -> None:
        self.__payload = []
        pass

    def append_uint(self, num: uint):
        self.__payload.extend(struct.pack('<H', num))

    def append_float(self, num: float32):
        self.__payload.extend(frombuffer(float32(num).tobytes(), dtype=uint8))

    def append_double(self, num: float64):
        self.__payload.extend(frombuffer(float64(num).tobytes(), dtype=uint8))

    def get_payload(self):
        return bytes(self.__payload)
        
    def size(self):
        return len(self.__payload)