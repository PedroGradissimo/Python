import iso6346


class ShippingContainer:

    # Class Attribute
    next_serial = 1337

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
    def create_empty(cls, owner_code, **kwargs):
        return cls(owner_code, contents=[], **kwargs)

    @classmethod
    # This function creates a container with a list of items passed as argument
    def create_with_items(cls, owner_code, items, **kwargs):
        return cls(owner_code, contents=list(items), **kwargs)

    # The instance attribute can be accessed via the instance object reference self.
    # The class attribute can be accessed via the class object reference ShippingContainer.
    def __init__(self, owner_code, contents, **kwargs):
        self.owner_code = owner_code
        self.content = contents
        self.bic = self._make_bic_code(
            owner_code=owner_code,
            serial=ShippingContainer._generate_serial()
        )


# This is how we override a class, passing it as an argument of the subclass
# allowing us to use the base class functions
class RefrigeratorShippingContainer(ShippingContainer):

    # Constant
    MAX_CELSIUS = 4.0

    def __init__(self, owner_code, contents, *, celsius, **kwargs):
        # To override the base init class in the derived class we use the built-in function "super"
        super().__init__(owner_code, contents, **kwargs)
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
        if value > RefrigeratorShippingContainer.MAX_CELSIUS:
            raise ValueError("Temperature to hot!")
        self._celsius = value

    @property
    # Getter method that retrieves the fahrenheit temperature given the celsius temperature
    def fahrenheit(self):
        return RefrigeratorShippingContainer._c_to_f(self._celsius)

    @fahrenheit.setter
    # Setter method that writes the celsius tempersture given the fahrenheit temperature
    def fahrenheit(self, value):
        self._celsius = RefrigeratorShippingContainer._f_to_c(value)


    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6),
            category="R"
        )
