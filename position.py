class Position:

    def __init__(self, latitude, longitude):
        if not(-90 <= latitude <= 90):
            raise ValueError("Latitude {latitude} out of range!")

        if not(-180 <= longitude <= 180):
            raise ValueError("Latitude {longitude} out of range!")

        self._latitude = latitude
        self._longitude = longitude

    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude

    # We can customize the repr built-in function the way we want
    def __repr__(self):
        return f"{typename(self)}(latitude={self._latitude}, longitude={self._longitude})"


class EarthPosition(Position):
    pass


class MarsPosition(Position):
    pass


# Accepts the argument "obj" and returns his type which in this case is the class name
def typename(obj):
    return type(obj).__name__

