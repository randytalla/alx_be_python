class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        # Static method: no access to class/instance-specific data
        return a + b

    @classmethod
    def multiply(cls, a, b):
        # Class method: can access class-level attributes using the 'cls' parameter
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
