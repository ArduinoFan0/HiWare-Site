from pyscript import document
import random
output_div = document.querySelector("#output")

enable_js_msg = document.querySelector("#enable-js-message")
js_only_content = document.querySelector("#js-only-content")
del enable_js_msg
del js_only_content.attributes.hidden

output_div.innerText = "The Python script is running."
js_content = document.body.children
    if element.className == 'js-only-content':
        element.attributes.hidden = False
    elif element.className == 'enable-js-message':
def generate(event):
    global output_div
    input_text = document.querySelector("#text_1")
    my_text = input_text.value
    output_div.innerText = f"{my_text} - {random.randint(1, 100)}"
