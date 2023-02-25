import shapely

class Part:
    def __init__(self, name, profile, internal_profiles, pockets, holes, grain_direction_important, grain_direction_lengthwise):
        self.name = name
        self.profile = profile
        self.internal_profiles = internal_profiles
        self.pockets = pockets
        self.holes = holes
        self.grain_direction_important = grain_direction_important
        self.grain_direction_lengthwise = grain_direction_lengthwise
    
    def __str__(self):
        return f"Part: {self.name}\nProfile: {self.profile}\nInternal Profiles: {self.internal_profiles}\nPockets: {self.pockets}\nHoles: {self.holes}\nGrain Direction Important: {self.grain_direction_important}\nGrain Direction Lengthwise: {self.grain_direction_lengthwise}"