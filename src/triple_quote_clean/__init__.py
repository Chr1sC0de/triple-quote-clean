import inspect
from dataclasses import dataclass


@dataclass
class TripleQuoteCleaner:
    tabs: int = 0
    skip_top_lines: int = 0
    spaces_per_tab: int = 4
    guide_character: str = "$$"
    skip_bottom_lines: int = 0

    @property
    def tab(self) -> "TripleQuoteCleaner":
        self.tabs += 1
        return self

    def __call__(self, string: str) -> str:
        tabs = " " * self.spaces_per_tab * self.tabs

        output = inspect.cleandoc(string)
        output = [
            f"{tabs}{line}"
            for line in output.splitlines()
            if not line.startswith(self.guide_character)
        ]

        output = output[self.skip_top_lines :]
        output = (
            output[: -self.skip_bottom_lines]
            if self.skip_bottom_lines > 0
            else output
        )

        output = "\n".join(output)
        tabs = 0
        return output

    def __rgt__(self, string: str) -> str:
        return self.__call__(string)

    def __gt__(self, string: str) -> str:
        return self.__call__(string)

    def __rrshift__(self, string: str) -> str:
        return self.__call__(string)

    def __rshift__(self, string: str) -> str:
        return self.__call__(string)

    def __rlshift__(self, string: str) -> str:
        return self.__call__(string)

    def __rlt__(self, string: str) -> str:
        return self.__call__(string)

    def __lt__(self, string: str) -> str:
        return self.__call__(string)

    def __lshift__(self, string: str) -> str:
        return self.__call__(string)

    def __rpow__(self, string: str) -> str:
        return self.__call__(string)

    def __pow__(self, string: str) -> str:
        return self.__call__(string)
