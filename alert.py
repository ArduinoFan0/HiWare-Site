from pyscript import document, window, when
debug = False
def run(msg=None):
    try:
        import random, json, time
        window.alert(msg)

    except BaseException as e:
        raise e
