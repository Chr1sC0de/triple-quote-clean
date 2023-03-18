import inspect
from dataclasses import dataclass


@dataclass
class TripleQuoteCleaner:

    tabs             : int = 0
    skip_top_lines   : int = 0
    spaces_per_tab   : int = 4
    guide_character  : str = '$$'
    skip_bottom_lines: int = 0

    @property
    def tab(self):
        self.tabs += 1
        return self

    def __call__(self, string):

        tabs   = " "*self.spaces_per_tab*self.tabs

        output = inspect.cleandoc(string)
        output = [
            f"{tabs}{line}" for line in output.splitlines()
                if not line.startswith(self.guide_character)
        ]

        output = output[self.skip_top_lines:]
        output = (
            output[:-self.skip_bottom_lines] if self.skip_bottom_lines > 0 else output
        )

        output = "\n".join(output)
        tabs   = 0
        return output

    def __rrshift__(self, other):
        return self.__call__(other)

    def __rshift__(self, other):
        return self.__call__(other)
