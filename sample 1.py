"""
This is my solution to Algolympics Sample Problem #1

link to problem:
https://www.facebook.com/157306517615186/posts/4053883574624108/
"""


from collections import Counter

class Threats:
    
    def __init__(self, input_):
        lines = [lines.split() for lines in input_.split('\n') if lines]
        
        self.shape_count = int(lines[0][0])
        self.shapes = lines[1:]
        
    @property
    def shapes(self):
        return self._shapes
        
    @shapes.setter
    def shapes(self, value):
        if not isinstance(value, list):
            raise Exception("Shapes value isn't a class: 'list'")
        
        mappings = []
        for input_ in value:
            mapping = []
            input_ = map(int, input_)
            x, y, w, h  = input_
            for y_ in range(y, y + h):
                for x_ in range(x, x + w):
                    mapping.append((x_, y_))
            mappings.append(mapping)
        self._shapes = mappings  # A list of lists that contain (x, y) tuples
    
    @property
    def frequency(self):
        return dict(Counter(i for sub in self.shapes for i in set(sub)))
        
        
    @property
    def ion_cannons(self):
        cannons = len([nukes for nukes in self.frequency.values() if nukes > 1])
        return cannons # number of areas hit by ion cannons
        
    @property
    def nukes(self):
        nuke = len(self.frequency)
        return nuke # number of areas hit by nukes

# This is the input as with the format as provided in the sample problem
input = """
2
0 0 3 3
1 -1 5 5 
"""
aliens = Threats(input)
print(aliens.nukes) # Returns 28
print(aliens.ion_cannons) # Returns 6
