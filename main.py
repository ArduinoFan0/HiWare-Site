import copy
from pyscript import document, window, when, workers, ffi
debug = False
try:
    import random, json, time
    from threading import Thread
    from js import setTimeout
    my_workers = {}
    #for key, worker in dict(workers).items():
        #my_workers[key] = await workers[key]
    def flash_element(el):
        # Set the initial brightness
        el.style.transition = "filter 0.06s ease-in-out"
        el.style.filter = "brightness(150%)"
        #


        # Schedule brightness reset using JS setTimeout (non-blocking)
        def after_init():
            el.style.transition = "filter 0.2s ease-in-out"
            el.style.filter = "brightness(100%)"
            after_init_proxy.destroy()
        after_init_proxy = ffi.create_proxy(after_init)
        setTimeout(after_init_proxy, 60)  # Delay in milliseconds

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
            try:
                button_actual.setAttribute("py-click", my_jdict["on-click"])
            except KeyError:
                pass
            try:
                button_actual.setAttribute("custom-data", json.dumps(str(my_jdict['custom-data']).replace("'", '"') ).strip('"').replace('\\', ''))
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
    def navigate_from_element(src_element, dests=[]):
        try:
            current = src_element
            my_dests = dests.copy()
            head = my_dests.pop(0)
            while current and not current.classList.contains(head):
                current = current.parentElement
            #print(current.className if current is not None else "Error descending")
            for dest in my_dests:
                current = current.getElementsByClassName(dest)[0]
            return current
        except:
            window.reportError(f"could not navigate from {src_element} to {dests}")
            return None
    @when("click", ".button-container.button-actual.button-contents.button-img.button-text")
    def animate_button(element):
        current = element
        while current and not current.classList.contains("button-container"):
            current = current.parentElement
        print(current.className if current is not None else "Error descending")
        current = current.getElementsByClassName("button-actual")[0]
        print(current.className if current is not None else "Error descending")
        current = current.getElementsByClassName("button-contents")[0]
        print(current.className if current is not None else "Error descending")
        current = current.getElementsByClassName("button-img")[0]
        print(current.className if current is not None else "Error descending")

        nav = navigate_from_element(current, ["button-container", "button-actual", "button-contents", "button-img"])
        if nav:
            flash_element(nav)
        else:
            window.reportError("Couldn't apply animation to requested element.")

    def run_script(event):
        button_actual = navigate_from_element(event.target, ["button-container", "button-actual"])
        if button_actual:
            data = button_actual.getAttribute("custom-data")
            jdata = json.loads(data)
            try:
                function_name = jdata["func"]
                my_worker = await workers[jdata['name']]
                function = getattr(my_worker, function_name)
                function(*jdata['args'])
            except (KeyError, TypeError, AttributeError):
                my_worker = await workers[jdata['name']]
                my_worker.run(*jdata['args'])

    def generate(event):
        # Traverse up to button-container
        current = event.target
        #animate_button(current)
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
