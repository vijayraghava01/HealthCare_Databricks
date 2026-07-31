class GeneratorOrchestrator:

    def __init__(self):
        self.generators = []

    def register(self, generator):
        self.generators.append(generator)

    def execute(self):
        for generator in self.generators:
            generator.generate()