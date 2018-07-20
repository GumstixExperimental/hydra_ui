from hydradev.hydraport import HydraPort

class PowerOutput(object):
    def __init__(self, voltage=0, current=0, is_on=False, set_voltage=0):
        self.voltage = float(voltage)
        self.current = float(current)
        self.is_on = is_on
        self.set_voltage = set_voltage

class HydraDev(object):
    def __init__(self):
        self.__port = HydraPort()
        self.input_voltage = 0.0
        self.Vout = {1: PowerOutput(), 2: PowerOutput(), 3: PowerOutput()}
        self.updateStatus()

    def __check_vout_num(self, Vout_n):
        if Vout_n == 0 or Vout_n > 3:
            print('invalid port.  Try again')
            return False
        return True

    def updateStatus(self):
        status = self.__port.send()
        for line in status:
            if len(line) > 0:
                values = line.split()
                if values[0] == 'Vin':
                    self.input_voltage = values[1]
                if values[0].startswith('Vout'):
                    index = int(values[0][-1])
                    self.Vout[index].voltage = float(values[1])
                    self.Vout[index].current = float(values[2].split('/')[0])
                    self.Vout[index].is_on = values[3] != 'OFF'
                    if self.Vout[index].set_voltage == 0 and self.Vout[index].is_on:
                        self.Vout[index].set_voltage = float(values[1])


    def enable(self, Vout_n):
        self.updateStatus()
        if not self.__check_vout_num(Vout_n):
            return
        cmd = 'en {}'.format(Vout_n)
        self.__port.send(cmd)
        self.updateStatus()

    def set_voltage(self, Vout_n, voltage):
        self.updateStatus()
        if self.__check_vout_num(Vout_n):
            self.Vout[Vout_n].set_voltage = int(voltage)
            cmd = 'set{} {}'.format(Vout_n, self.Vout[Vout_n].set_voltage)
            reply = self.__port.send(cmd)
            self.updateStatus()
            if 'OK' in reply:
                return True
        return False

    def set_and_enable(self, Vout_n, voltage):
        self.updateStatus()
        if self.set_voltage(Vout_n, voltage):
            self.enable(Vout_n)
        self.updateStatus()

    def disable(self, Vout_n):
        self.updateStatus()
        msg = 'dis {}'.format(Vout_n)
        reply = self.__port.send(msg)
        if 'OK' in reply:
            self.updateStatus()
            return True
        return False

def main():
    hydra = HydraDev()
    print(hydra.disable(2))
    print(hydra.disable(1))
    return

if __name__ == '__main__':
    main()
