from collections.abc import Iterable

def merge(*elems):
    for elem in elems:
        if isinstance(elem, Iterable) and not isinstance(elem, (str, bytes)):
            for sub in elem:
                yield from merge(sub)
        else:
            yield elem
