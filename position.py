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

    @property
    def latitude_hemisphere(self):
        return "N" if self._latitude > 0 else "S"

    @property
    def longitude_hemisphere(self):
        return "E" if self._longitude >= 0 else "W"

    # We can customize the repr built-in function the way we want
    # The __repr__ method is usually used by developers
    def __repr__(self):
        return f"{typename(self)}(latitude={self._latitude}, longitude={self._longitude})"

    # The __str__ method is often used for users
    # The default implementation of __str__ invokes __repr__ that is why if we do not
    # change the method it will return the same output as __repr__
    # Another good implementation is returning the implementation of the format built-in method
    """ def __str__(self):
            return format(self)
    """
    def __str__(self):
        return (
            f"{abs(self._latitude)}º {self.latitude_hemisphere}, "
            f"{abs(self._longitude)}º {self.longitude_hemisphere}"
        )

    def __format__(self, format_spec):
        component_format_spec = ".2f"
        prefix, dot, suffix = format_spec.partition(".")
        if dot:
            num_decimal_places = int(suffix)
            component_format_spec = f".{num_decimal_places}f"
        latitude = format(abs(self._latitude), component_format_spec)
        longitude = format(abs(self._longitude), component_format_spec)
        return (
            f"{latitude}º {self.latitude_hemisphere}, "
            f"{longitude}º {self.longitude_hemisphere}"
        )


class EarthPosition(Position):
    pass


class MarsPosition(Position):
    pass


# Accepts the argument "obj" and returns his type which in this case is the class name
def typename(obj):
    return type(obj).__name__
