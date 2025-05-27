from pyscript import document
import random
output_div = document.querySelector("#output")
output_div.innerText = "The Python script is running."
def generate(event):
    global output_div
    input_text = document.querySelector("#text_1")
    my_text = input_text.value
    output_div.innerText = f"{my_text} - {random.randint(1, 100)}"
