from pyscript import document, window, when, sync
debug = False
def run(msg="None"):
    import random, json, time
    window.alert(msg)
def alt_print(msg="None"):
    print(msg)
    output_div = document.querySelector("#output")
    output_div.innerText = msg
sync.run = run
sync.alt_print = alt_print