from abc import ABC, abstractmethod


class AbstractSignal(ABC):
    __is_empty: bool = False

    def get_signal_type_name(self):
        return type(self).__name__

    def to_string(self):
        text = ""

        for attrib in self._enumerate_attributes():
            # ignore private attributes (all signal attributes are public)
            if str(attrib).startswith("_"):
                continue

            # append ", " in between attributes
            if text != "":
                text += ", "

            # append attrib=value info
            text += str(attrib) + "=" + str(getattr(self, attrib))

        return text

    def __str__(self):
        return "[Signal] " + self.get_signal_type_name() + ": " + self.to_string()

    def is_empty(self) -> bool:
        return self.__is_empty

    def set_empty(self, is_empty: bool):
        self.__is_empty = is_empty
        return self

    """Enumerates all attributes stored within the self-reference (i.e. object instance) of this class"""
    def _enumerate_attributes(self):
        return [a for a in dir(self) if not a.startswith('__') and not callable(getattr(self, a))]
