# Subject class
class ConnectDevice:
    def connect(self):
        pass


class Connect(ConnectDevice):
    def __init__(self) -> None:
        self.target = None
        self.connected = None
        self.charged = 1
    
    def has_battery(self):
        return self.charged == 1
    
    def set_target(self, target):
        self.target = target
    
    def connect(self):
        if self.has_battery():
            print("Connecting...")
        else:
            print("Battery level too low.")
        

class Bluetooth(ConnectDevice):
    def __init__(self) -> None:
        self.method = Connect()

    def connect(self):
        target_name = 'iPhone 13'
        self.method.set_target(target_name)

        return self.method.connect()
