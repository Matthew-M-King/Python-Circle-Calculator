import math

class CircleCalculator:
    '''
        Calculate the measurements of a circle,
        based on the input of one known value for one of the following:
        
        Radius
        Circumference 
        Area
        Diameter

    '''
    def __init__(self, value, calc_by) -> None:
        
        if calc_by == "Radius":
            self.radius = value
            self.diameter = self._get_diameter()
            self.circumference = self._get_circumference()
            self.area = self._get_area()
        
        elif calc_by == "Diameter":
            self.diameter = value
            self.radius = self._get_radius_by_diameter()
            self.circumference = self._get_circumference()
            self.area = self._get_area()
        
        elif calc_by == "Area":
            self.area = value
            self.radius = self._get_radius_by_area()
            self.diameter = self._get_diameter()
            self.circumference = self._get_circumference()
        
        elif calc_by == "Circumference":
            self.circumference = value
            self.radius = self._get_radius_by_circumference()
            self.diameter = self._get_diameter()
            self.area = self._get_area()
        else:
            print('There wasn\'t an argument provided')

    def _get_diameter(self):
        return self.radius * 2
    
    def _get_area(self):
        return math.pi * math.pow(self.radius, 2)

    def _get_circumference(self):
        return math.pi * self.diameter
    
    def _get_radius_by_diameter(self):
        return self.diameter / 2

    def _get_radius_by_area(self):
        return math.sqrt(self.area / math.pi)

    def _get_radius_by_circumference(self):
        return self.circumference / (math.pi * 2)

    def __str__(self):
        output = '=' * 50
        output += '\nRadius: ' + str(self.radius)
        output += '\nDiameter: ' + str(self.diameter)
        output += '\nCircumference: ' + str(self.circumference)
        output += '\nArea: ' + str(self.area) + '\n'
        output += '=' * 50
        return output


if __name__ == "__main__":
    calc_types = {
            1: "Area",
            2: "Circumference",
            3: "Diameter",
            4: "Radius"
        }
    while True:
        
        try:
            calc_by = int(input('[1] Area\n[2] Circumference\n[3] Diameter\n[4] Radius\nWhat circle value do you have? '))
        
            if calc_by <= 0 or calc_by >= 5:
                raise ValueError

        except ValueError:
            print('Not a valid option')
            input('Press Enter to try again')
            continue
        
        try:
            value = float(input('Enter a value: '))
        except ValueError:
            print('Not a valid value')
            input('Press Enter to try again')
            continue

        calc_types[calc_by]
        circle = CircleCalculator(value, calc_types[calc_by])
        print(circle)
        input('Press Enter to continue... ')
