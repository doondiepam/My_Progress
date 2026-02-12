from collections.abc import Iterable

def merge(*elems):
    for ele in elems:
        if isinstance(ele, Iterable) and not isinstance(ele, (str, bytes)):
            for sub in ele:
                yield from merge(sub)
        else:
            yield ele
