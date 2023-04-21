from numpy import float32, float64, uint8, frombuffer, int8, uint16, uint32
import struct
from collections import deque

c_types = {
    "uint8_t": {"bytes": 1, "dtype": uint8},
    "uint16_t": {"bytes": 2, "dtype": uint16},
    "uint32_t": {"bytes": 4, "dtype": uint32},
    "int8_t": {"bytes": 1, "dtype": int8},
    "float": {"bytes": 4, "dtype": float32},
    "double": {"bytes": 8, "dtype": float64}
}

class PayloadBuilder:
    """
    The PayloadBuilder class allows for simple building of a min payload.
    """

    __payload: deque[uint8] = deque(maxlen=255)

    def __init__(self, payload: list[uint8] = None) -> None:
        if payload != None:
            self.__payload.extend(payload)
        pass

    def append_uint8(self, num: uint8):
        self.__payload.append(num)

    def append_uint16(self, num: uint16):
        self.__payload.extend(struct.pack('<H', num))

    def append_float(self, num: float32):
        self.__payload.extend(frombuffer(float32(num).tobytes(), dtype=uint8))

    def append_double(self, num: float64):
        self.__payload.extend(frombuffer(float64(num).tobytes(), dtype=uint8))

    def read_c_type(self, type_str: str):
        t = c_types[type_str]
        buf: list[uint8] = []
        for _ in range(t.get("bytes")):
            buf.append(self.__payload.popleft())
        
        return frombuffer(bytes(buf), dtype=t.get("dtype"))[0]
  
    def get_payload(self):
        b =  bytes(self.__payload)
        self.__payload.clear()
        return b
        
    def size(self):
        return len(self.__payload)