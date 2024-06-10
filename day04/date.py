class Date:
    def __init__(self, dd, mm, yy):
        self.d = dd
        self.m = mm
        self.y = yy
        # Attribute `tz` should be private
        self._tz = "IST"
        self.__country = "India"

    def display(self, fmt):
        breakpoint()
        print("Printing in format:", fmt)
        print(f'{self.d}-{self.m}-{self.y}')

    @classmethod
    def from_string(cls, date_str):
        parts = list(map(int, date_str.split('-')))
        return Date(parts[0], parts[1], parts[2])

# Main : client code
today = Date(6, 6, 2024)
today.display('html')
Date.display(today, 'html')

event_str = "20-6-2024"
event = Date.from_string(event_str)

#parts = list(map(int, event_str.split('-')))
#event = Date(parts[0], parts[1], parts[2])

event.display('html')
