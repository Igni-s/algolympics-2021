"""
This is my solution to Algolympics mple Problem #1

link to problem:
https://www.facebook.com/157306517615186/posts/4053883574624108/
"""


from collections import Counter

class Factory:
    
    def __init__(self, input_):
        lines = [lines.split() for lines in input_.split('\n') if lines]
        
        self.shape_count = int(lines[0][0])
        self.shapes = lines[1:]
    
    @property
    def shapes(self):
        shapes_ = self._shapes
        mapping = []
        for s in shapes_:
            coords = []
            for y in range(s["y"], s["h"] + 1):
                for x in range(s["x"], s["w"]):
                    coords.append((x, y))
            mapping.append(coords)
        return mapping
    
    @shapes.setter
    def shapes(self, value):
        if not isinstance(value, list):
            raise Exception("Shapes value isn't a class: 'list'")
        
        mappings = []
        for input_ in value:
            mapping = {}
            attrs = ["x", "y", "w", "h"]
            for attr, coord in zip(attrs, input_):
                mapping[attr] = int(coord)
            mappings.append(mapping)
        self._shapes = mappings  # Rank 2 Tensor with a bunch of coordinates
        
    
class Threats:
    
    def __init__(self, shape_count, shapes):
        self.shape_count = shape_count
        self.shapes = shapes
    
    @property
    def shapes(self):
        return self._shapes
        
    @shapes.setter
    def shapes(self, value):
        self._shapes = dict(Counter(i for sub in value for i in set(sub)))
        
        
    @property
    def nukes(self):
        nukes = len([nukes for nukes in self.shapes.values() if nukes > 1])
        return nukes // self.shape_count
        
    @property
    def ion_cannons(self):
        cannon = len(self.shapes)
        return cannon - self.nukes

# This is the input as with the format as provided in the sample problem
input = """
2
0 0 3 3
1 -1 5 5 
"""
coords = Factory(input)
aliens = Threats(coords.shape_count, coords.shapes)
print(aliens.ion_cannons) # Returns 28
print(aliens.nukes) # Returns 6
