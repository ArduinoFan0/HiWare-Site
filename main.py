from pyscript import document, window, when, workers
debug = False
try:
    import random, json, time
    from threading import Thread
    def fill_from_template_button():
        template_name = "button-template"
        placeholder_classname = "button"
        buttons = document.getElementsByClassName(placeholder_classname)
        amount = buttons.length
        template = document.getElementById(template_name)

        for i in range(amount):
            item = buttons.item(0)
            my_json = item.innerText
            my_jdict = json.loads(my_json)
            my_text = my_jdict["text"]
            width = my_jdict["wh"][0]
            height = my_jdict["wh"][1]
            font_size = "0%"
            if height.endswith("px"):
                font_size = f"{int(height[:-2]) - 10}px"
            try:
                my_style = my_jdict["style"]
                if not my_style.endswith(";"):
                    my_style = my_style + ";"
                    if not my_style.endswith(" "):
                        my_style = my_style + " "
            except KeyError:
                my_style = ""
            try:
                my_tstyle = my_jdict["text-style"]
                if not my_tstyle.endswith(";"):
                    my_tstyle = my_tstyle + ";"
                    if not my_tstyle.endswith(" "):
                        my_tstyle = my_tstyle + " "
            except KeyError:
                my_tstyle = ""

            clone = template.content.cloneNode(True)
            button_container = clone.children.item(0)
            button_container.setAttribute("style", f"width: {width}; height: {height}; font-size: {font_size};")
            button_actual = button_container.getElementsByClassName('button-actual').item(0)
            button_contents = button_actual.getElementsByClassName('button-contents').item(0)
            template_text = button_contents.getElementsByClassName("button-text").item(0)
            template_text.setAttribute("style", f"{my_tstyle}{template_text.getAttribute("style")}{my_tstyle}")
            button_image = button_contents.getElementsByClassName("button-img").item(0)
            try:
                button_image.setAttribute("src", my_jdict["img"])
            except KeyError:
                pass

            template_text.innerText = my_text

            item.replaceWith(clone)
    fill_from_template_button()
    output_div = document.querySelector("#output")

    enable_js_msg = document.querySelector("#enable-js-message")
    js_only_content = document.querySelector("#js-only-content")
    enable_js_msg.setAttribute("hidden", "hidden")
    js_only_content.removeAttribute('hidden')

    output_div.innerText = "The Python script is running."


    def generate(event):
        # Traverse up to button-container
        current = event.target
        print(current.className)
        current = current.getElementsByClassName("button-contents")[0]
        current = current.getElementsByClassName("button-img")[0]
        if current:
            current.animate([
                {"filter": "brightness(50%)"},
                {"filter": "brightness(100%)"}
            ], {
                "duration": 500,
                "iterations": 1
            })
        else:
            window.reportError("Couldn't apply animation to requested element.")
        global output_div
        input_text = document.querySelector("#text_1")
        my_text = input_text.value
        output_div.innerText = f"{my_text} - {random.randint(1, 100)}"
    def generate_dep(event):
        clicked_element = event.target
        clicked_element.animate([
            {"filter":"brightness(50%)"},
            {"filter":"brightness(100%)"}
        ],
            {
                "duration": 500,
                "iterations": 1
            })
        global output_div
        input_text = document.querySelector("#text_1")
        my_text = input_text.value
        output_div.innerText = f"{my_text} - {random.randint(1, 100)}"
except BaseException as e:
    def on_exception(my_e):
        import sys, traceback
        def custom_excepthook(exc_type, exc_value, exc_tb):
            # Format the traceback
            tb_str = ''.join(traceback.format_exception(exc_type, exc_value, exc_tb))
            # Log it to the browser console
            window.reportError("Custom Uncaught Exception:\n" + tb_str)

        # Set the custom handler
        sys.excepthook = custom_excepthook
        raise my_e
    on_exception(e)
