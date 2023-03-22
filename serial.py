"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, starting_num=0):
        """make a new generator, beginning at starting num"""
        self.starting_num = self.next_num = starting_num

    def __repr__(self):
        """Show representation"""
        return f"<Serial Generator starting_num={self.starting_num} next={self.next_num}"

    def generate(self):
        """ method that returns next number """        
        self.next_num += 1
        return self.next_num - 1 

    def reset(self):
        """reset number to starting number""" 
        self.next_num = self.starting_num

serial = SerialGenerator(100)
print(serial.__repr__())
print(serial.generate())
print(serial.generate())
print(serial.generate())
print(serial.generate())
print(serial.reset())
print(serial.generate())




