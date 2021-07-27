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
    def create_empty(cls, owner_code):
        return cls(owner_code, contents=[])

    @classmethod
    # This function creates a container with a list of items passed as argument
    def create_with_items(cls, owner_code, items):
        return cls(owner_code, contents=list(items))

    # The instance attribute can be accessed via the instance object reference self.
    # The class attribute can be accessed via the class object reference ShippingContainer.
    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.content = contents
        self.bic = self._make_bic_code(
            owner_code=owner_code,
            serial=ShippingContainer._generate_serial()
        )


# This is how we override a class, passing it as an argument of the subclass
class RefrigeratorShippingContainer(ShippingContainer):

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6),
            category="R"
        )
