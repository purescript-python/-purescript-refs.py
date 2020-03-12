def new(val):
    return lambda: {"value": val}


def read(ref):
    return lambda: ref["value"]


def modify_(f):
    def ap_ref(ref):
        def ap():
            t = f(ref["value"])
            ref["value"] = t["state"]
            return t["value"]

        return ap

    return ap_ref


globals()["modify'"] = modify_


def write(val):
    def ap_ref(ref):
        def ap():
            ref["value"] = val
            return

        return ap

    return ap_ref

