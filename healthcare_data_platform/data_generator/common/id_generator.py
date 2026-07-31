import random

class IdGenerator:

    generated_npis = set()

    @classmethod
    def generate_npi(cls):

        while True:

            npi = str(random.randint(1000000000,9999999999))

            if npi not in cls.generated_npis:

                cls.generated_npis.add(npi)

                return npi