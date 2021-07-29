import iso6346


class ShippingContainer:

    # Class Attribute
    next_serial = 1337
    HEIGHT_FT = 8.5
    WIDTH_FT = 8.0

    """@staticmethod
    # Static methods allow us to bound functions with the class
    # rather then instances of the class eliminating the self instance.
    def _generate_serial():
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result"""

    @classmethod
    def _generate_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code,
                              serial=str(serial).zfill(6)
                              )

    @classmethod
    # Factory method which returns an instance of a class
    # Function creates an empty container
    # Argument **kwargs is used allows for the base class functions accept
    # arguments destined to the derived class functions
    def create_empty(cls, owner_code, length_ft, **kwargs):
        return cls(owner_code, length_ft, contents=[], **kwargs)

    @classmethod
    # This function creates a container with a list of items passed as argument
    def create_with_items(cls, owner_code, length_ft, items, **kwargs):
        return cls(owner_code, length_ft, contents=list(items), **kwargs)

    # The instance attribute can be accessed via the instance object reference self.
    # The class attribute can be accessed via the class object reference ShippingContainer.
    def __init__(self, owner_code, length_ft, contents, **kwargs):
        self.owner_code = owner_code
        self.length_ft = length_ft
        self.content = contents
        self.bic = self._make_bic_code(
            owner_code=owner_code,
            serial=ShippingContainer._generate_serial()
        )

    @property
    # Retrieves the volume of the container
    # Template method, doesnt do anything, except delegate to a regular method
    # With this method there is no need to override @property, override the regular method
    def volume_ft3(self):
        return self._calc_volume()

    def _calc_volume(self):
        return ShippingContainer.HEIGHT_FT * ShippingContainer.WIDTH_FT * self.length_ft


# This is how we override a class, passing it as an argument of the subclass
# allowing us to use the base class functions
class RefrigeratorShippingContainer(ShippingContainer):

    # Constant
    MAX_CELSIUS = 4.0
    FRIDGE_VOLUME_FT3 = 100

    def __init__(self, owner_code, length_ft, contents, *, celsius, **kwargs):
        # To override the base init class in the derived class we use the built-in function "super"
        super().__init__(owner_code, length_ft, contents, **kwargs)
        self.celsius = celsius

    @staticmethod
    # Good candidate to a static method since they don't rely on instances or class objects
    def _c_to_f(celsius):
        return celsius * 9/5 + 32

    @staticmethod
    # Good candidate to a static method since they don't rely on instances or class objects
    def _f_to_c(fahrenheit):
        return (fahrenheit - 32) * 5/9

    @property
    # getter method used to call them as attributes
    # read-only method
    def celsius(self):
        return self._celsius

    @celsius.setter
    # Setter method used as a write only method
    # to change the celsius attribute value
    def celsius(self, value):
        self._set_celsius(value)

    def _set_celsius(self, value):
        if value > RefrigeratorShippingContainer.MAX_CELSIUS:
            raise ValueError("Temperature to hot!")
        self._celsius = value

    @property
    # Getter method that retrieves the fahrenheit temperature given the celsius temperature
    def fahrenheit(self):
        return RefrigeratorShippingContainer._c_to_f(self.celsius)

    @fahrenheit.setter
    # Setter method that writes the celsius temperature given the fahrenheit temperature
    def fahrenheit(self, value):
        self.celsius = RefrigeratorShippingContainer._f_to_c(value)

    def _calc_volume(self):
        return super()._calc_volume() - RefrigeratorShippingContainer.FRIDGE_VOLUME_FT3

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6),
            category="R"
        )


class HeatedRefrigeratedShippingContainer(RefrigeratorShippingContainer):

    MIN_CELSIUS = -20

    #@RefrigeratorShippingContainer.celsius.setter
    def _set_celsius(self, value):
        if value < HeatedRefrigeratedShippingContainer.MIN_CELSIUS:
            raise ValueError("Temperature to cold!")
        super()._set_celsius(value)
