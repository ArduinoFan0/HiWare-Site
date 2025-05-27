from pyscript import document, window
try:
    import random
    output_div = document.querySelector("#output")

    enable_js_msg = document.querySelector("#enable-js-message")
    js_only_content = document.querySelector("#js-only-content")
    enable_js_msg.setAttribute("hidden", "hidden")
    js_only_content.removeAttribute('hidden')

    output_div.innerText = "The Python script is running."

    def generate(event):
        global output_div
        input_text = document.querySelector("#text_1")
        my_text = input_text.value
        output_div.innerText = f"{my_text} - {random.randint(1, 100)}"
except BaseException as e:
    window.reportError(f"Uncaught exception in line {e.__traceback__.tb_lineno} of {__name__}: {type(e).__name__}: {e}")