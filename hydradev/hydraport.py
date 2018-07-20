from serial import Serial
import serial.tools.list_ports as Ports
import io
import os
import threading
from time import sleep


class HydraNotConnectedError(Exception):
    def __init__(self, message=''):
        self.message = message


class HydraPort(object):
    def __init__(self):
        self.__port = self.get_port()

    def __del__(self):
        if self.__port.is_open:
            self.__port.close()

    def get_port(self):
        test_port = None
        current_ports = Ports.comports()
        for port in current_ports:
            if 'USB' in port.device:
                try:
                    test_port = Serial(port.device, 9600)
                except Exception as e:
                    print('opening port failed: {}'.format(e))
                    continue
                test_port.write(b'\r\n\r\n')
                test_port.flush()
                while test_port.in_waiting > 0:
                    line = test_port.readline()
                    if b'Vin: ' in line:
                        test_port.flush()
                        return test_port
                test_port.close()
        raise HydraNotConnectedError('Hydra not found.  Please connect Hydra and try again.')

    @property
    def is_open(self):
        return self.__port.is_open

    @property
    def device(self):
        return self.__port.name

    def open(self):
        if not self.is_open:
            try:
                self.__port.open()
            except Exception as e:
                print(e)
                self.__port = self.get_port()

    def close(self):
        if self.is_open:
            self.__port.close()

    def send(self, line: str=''):
        self.__port.flushInput()
        self.__port.flushOutput()
        bytestring = line.lstrip().rstrip().encode('utf-8')
        bytestring += b'\r\n'
        self.__port.write(bytestring)
        self.__port.flush()
        reply = b''
        while self.__port.in_waiting > 0:
            reply += self.__port.read(self.__port.in_waiting)
            sleep(0.1)
        retval = []
        for line in reply.splitlines():
            clean_line = line.decode('utf-8').strip()
            if len(clean_line) > 0:
                retval.append(clean_line)
        return retval




def main():
    try:
        hydra = HydraPort()
    except HydraNotConnectedError as e:
        print(e.message)
        exit()
    try:
        reply = hydra.send('set2 12')
        reply += hydra.send('dis 2')
        if 'OK' in reply:
            print('YAY')
        hydra.close()
    except KeyboardInterrupt as e:
        hydra.close()
        raise e


if __name__ == '__main__':
    main()
