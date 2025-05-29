from pyscript import document, window, when
debug = False
def run(msg="None"):
    import random, json, time
    window.alert(msg)
def alt_print(msg="None"):
    print(msg)
__export__ = ["run", "alt_print"]