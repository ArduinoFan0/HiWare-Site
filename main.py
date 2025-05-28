from pyscript import document, window, when
debug = False
try:
    import random
    def fill_from_template(template_name="button-template", placeholder_classname="button"):
        buttons = document.getElementsByClassName(placeholder_classname)
        amount = buttons.length
        template = document.getElementById(template_name)

        for i in range(amount):
            item = buttons.item(0)
            my_text = item
            template_text = template.getElementsByClassName("button-text").item(0)
            template_text.innerHTML = my_text.getHTML()
            clone = template.content.cloneNode(True)
            item.replaceWith(clone)
    fill_from_template()
    output_div = document.querySelector("#output")

    enable_js_msg = document.querySelector("#enable-js-message")
    js_only_content = document.querySelector("#js-only-content")
    enable_js_msg.setAttribute("hidden", "hidden")
    js_only_content.removeAttribute('hidden')

    output_div.innerText = "The Python script is running."
    @when('mousedown', '#button1')
    def button1_press():
        button1 = document.querySelector("#button1_img")
        button1.setAttribute("src", "./button_pressed.png")


    @when('mouseup', '#button1')
    def button1_release():
        button1 = document.querySelector("#button1_img")
        button1.setAttribute("src", "./button.png")


    def generate(event):
        global output_div
        input_text = document.querySelector("#text_1")
        my_text = input_text.value
        output_div.innerText = f"{my_text} - {random.randint(1, 100)}"
except BaseException as e:
    if debug:
        raise
    window.reportError(f"Uncaught exception in line {e.__traceback__.tb_lineno} of {__name__}: {type(e).__name__}: {e}")
