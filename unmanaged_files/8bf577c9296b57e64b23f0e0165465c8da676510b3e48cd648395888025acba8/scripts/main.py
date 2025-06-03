import asyncio
import copy
import os
from typing import overload
from pyscript import document, window, when, workers, ffi, PyWorker
from pyscript.ffi import create_proxy
debug = False
class hbmckshb():
    pass
try:
    developer_mode = False
    import random, json, time, hashlib
    from threading import Thread
    from js import setTimeout
    cookies = window.cookieStore
    import sys, traceback
    class secret_question_gen:
        people = [
            "Alice",
            "Bob",
            "Charlie",
            "David",
            "Laurel",
            "Michael",
            "Oliver",
            "Victor",
            "William",
            "Chris"
        ]
        possessives = [
            "my",
            "your",
            "their",
            "his",
            "her",
            "the"
        ]
        objects = [
            "moon",
            "sun",
            "country"
        ]
        adjectives = [
            "quick",
            "brown",
            "lazy",
            "red",
            "white",
            "black",
            "slow",
            "busy"
        ]
        nouns = people.copy()
        nouns.extend(objects)

        def generate(self):
            r = random.choice
            secret_questions = [
                f"Why did {r(self.people)} take over {r(self.possessives)} {r(self.objects)}?",
                f"The {r(self.adjectives)} {r(self.adjectives)} {r(self.nouns)} jumped over the {r(self.adjectives)} {r(self.nouns)}."
            ]
            return random.choice(secret_questions)
    s_q = secret_question_gen()

    secret_question:str = s_q.generate()
    interacted = False
    def schedule(start_delay: float, function):
        # Create the callback proxy
        async def wrapped():
            try:
                await function()
            except Exception:
                pass
            wrapped_proxy.destroy()

        wrapped_proxy = create_proxy(wrapped)
        setTimeout(wrapped_proxy, start_delay)
    def my_loop():
        #do something
        #then, run "schedule(77, my_loop)" at the very end of my_loop
        pass
        schedule(77, my_loop)
    my_loop()
    def custom_excepthook(exc_type, exc_value, exc_tb):
        # Format the traceback
        tb_str = ''.join(traceback.format_exception(exc_type, exc_value, exc_tb))
        # Log it to the browser console
        window.reportError("Custom Uncaught Exception:\n" + tb_str)
        exit(0)
        return
    sys.excepthook = custom_excepthook
    #from js import jsdocument, jswindow
    #from pyodide.ffi import jsto_js, jscreate_proxy
    async def sync_cookies():
        global secret_question
        if await cookies.get('generated-s-q') is None:
            await cookies.set('generated-s-q', secret_question)
        else:
            secret_question = (await cookies.get('generated-s-q')).value

    async def merge_page(url):
        # Step 1: Fetch the external HTML page
        response = await window.fetch(url)
        text = await response.text()

        # Step 2: Parse it as HTML using DOMParser
        parser = window.DOMParser.new()
        doc2 = parser.parseFromString(text, "text/html")

        # Step 3: Merge <head> elements
        for el in doc2.head.children:
            if el.id and document.getElementById(el.id):
                continue  # Skip elements with duplicate IDs
            document.head.appendChild(el.cloneNode(True))

        # Step 4: Merge <body> elements
        for el in doc2.body.children:
            if el.id and document.getElementById(el.id):
                continue
            document.body.appendChild(el.cloneNode(True))


    # Example usage:
    is_template = document.querySelector("data#template")
    fetch_from = document.querySelector("data#draw-from")
    try:

        if is_template.value == "True":
            await merge_page(fetch_from.value)
    except AttributeError:
        pass
    my_workers = {}
    async def start_worker(worker_path: str, worker_name: str):
        worker = PyWorker(worker_path, type='pyodide')
        await worker.ready
        my_workers[worker_name] = worker
    async def stop_worker(worker_name: str):
        my_workers[worker_name].terminate()
        del my_workers[worker_name]
    enable_js_msg = document.querySelector("#enable-js-message")
    loading_text = enable_js_msg.querySelector("#loading-text-1")  #
    loading_text.innerText = "Starting workers..."
    await start_worker("/HiWare-Site/unmanaged_files/8bf577c9296b57e64b23f0e0165465c8da676510b3e48cd648395888025acba8/scripts/alert.py", "alert.py")
    #await start_worker("./unmanaged_files/8bf577c9296b57e64b23f0e0165465c8da676510b3e48cd648395888025acba8/scripts/loop.py", "loop")
    def animate(el, keyframes:list, options:dict, restore_style:bool=True):
        my_keyframes = keyframes.copy()
        my_keyframes.append({})
        old_style = el.getAttribute("style")
        duration = options['duration']
        iterations = options['iterations']
        num_frames = len(my_keyframes)
        interval = round(duration/num_frames)
        i = -1
        for keyframe in my_keyframes:
            i += 1
            on_start = bool(i == 0)
            on_end = bool(i == num_frames-1)
            on_endpoint = bool(on_start or on_end)
            def frame(_keyframe=keyframe, _endpoint=on_endpoint):
                try:
                    list(_keyframe.keys())[0]
                    el.style.transition = f"{' '.join([list(_keyframe.keys())[k] for k in range(len(_keyframe.keys()))])} {interval if not _endpoint else 0}ms linear"
                    for k in range(len(_keyframe.keys())):
                        setattr(el.style, f"{list(_keyframe.keys())[k]}", f"{list(_keyframe.values())[k]}")
                except IndexError:
                    if restore_style:
                        el.style = old_style
            proxy_handle = hashlib.md5(str(time.time_ns()).encode(), usedforsecurity=False).hexdigest()
            setattr(hbmckshb, proxy_handle, ffi.create_proxy(frame))
            setTimeout(getattr(hbmckshb, proxy_handle), interval * i)
    def brighten_element(el):
        # Set the initial brightness
        el.style.transition = "filter 0.06s ease-in-out"
        el.style.filter = "brightness(150%)"
    def normal_element(el):
        # Set the initial brightness
        el.style.transition = "filter 0.2s ease-in-out"
        el.style.filter = "brightness(100%)"
    def flash_element(el):
        # Set the initial brightness
        el.style.transition = "filter 0.06s ease-in-out"
        el.style.filter = "brightness(150%)"
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
            item_style = str(item.getAttribute("style"))
            if not item_style.endswith(";"):
                item_style = item_style + ";"
                if not item_style.endswith(" "):
                    item_style = item_style + " "
            button_container.setAttribute("style", f"{item_style}width: {width}; height: {height}; font-size: {font_size}; {item_style}")
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
                button_actual.setAttribute("custom-on-click", my_jdict["on-click"])
            except KeyError:
                pass
            try:
                button_actual.setAttribute("custom-data", json.dumps(str(my_jdict['custom-data']).replace("'", '"') ).strip('"').replace('\\', ''))
            except KeyError:
                pass
            template_text.innerText = my_text
            item.replaceWith(clone)
    def fill_from_template():
        #Replace <from-template> elements with content from their <template> with the ID corresponding to the <from-template>'s class attribute
        #Then, <data value=VAR_A>'s contents from <from-template> replace <template>'s <data value=VAR_A> element, then with VAR_B, and so on
        #
        templates = document.getElementsByTagName("template")
        placeholders = document.getElementsByTagName("place-holder")
        for template in range(len(templates)):
            template = templates[template]
            for placeholder in range(len(placeholders)):
                clone = template.content.cloneNode(True)
                clone_contents = clone.children.item(0)
                placeholder = placeholders[0]
                if placeholder.className == template.getAttribute("id"):
                    pdatas = placeholder.getElementsByTagName("data")
                    tdatas = clone_contents.getElementsByTagName("data")
                    for tdata in range(len(tdatas)):
                        for pdata in range(len(pdatas)):
                            if pdatas[pdata].value == tdatas[tdata].value:
                                tdatas[tdata].replaceWith(pdatas[pdata])
                    clone_contents.setAttribute('class', placeholder.getAttribute("id"))
                    if placeholder.hasAttribute('hidden'):
                        clone_contents.setAttribute('hidden', True)
                    placeholder.replaceWith(clone)
        pass
    fill_from_template_button()
    for _ in range(20):
        fill_from_template()
    fill_from_template()
    output_div = document.querySelector("#output")
    js_only_content = document.querySelector("#js-only-content")
    enable_js_msg.setAttribute("hidden", "hidden")
    js_only_content.removeAttribute('hidden')
    try:
        output_div.innerText = "The Python script is running."
    except AttributeError:
        pass
    def navigate_from_element(src_element, dests=[]):
        try:
            current = src_element
            my_dests = dests.copy()
            head = my_dests.pop(0)
            while current and not current.classList.contains(head):
                current = current.parentElement
            for dest in my_dests:
                current = current.getElementsByClassName(dest)[0]
            return current
        except:
            window.reportError(f"could not navigate from {src_element} to {dests}")
            return None
    def animate_button(element, mode="flash"):
        current = element
        while current and not current.classList.contains("button-container"):
            current = current.parentElement
        current = current.getElementsByClassName("button-actual")[0]
        current = current.getElementsByClassName("button-contents")[0]
        current = current.getElementsByClassName("button-img")[0]
        nav = navigate_from_element(element, ["button-container", "button-actual", "button-contents", "button-img"])
        if nav:
            match mode:
                case "flash":
                    flash_element(nav)
                case "brighten":
                    brighten_element(nav)
                case "normal":
                    normal_element(nav)
        else:
            window.reportError("Couldn't apply animation to requested element.")
    @when("mouseenter", ".button-img")
    async def hovered(event):
        if event.target.className == "button-img":
            animate_button(event.target, "brighten")
    @when("mouseleave", ".button-img")
    async def hover_gone(event):
        if event.target.className == "button-img":
            animate_button(event.target, "normal")
    error_counter = 0
    @overload
    async def on_error(msg_or_event, url, line, column, error) -> None: ...
    @overload
    async def on_error(msg_or_event) -> None: ...
    async def on_error(msg_or_event):
        global error_counter, output_div #
        error_counter += 1
        suffix = "th"
        match error_counter % 10:
            case 1:
                suffix = "st"
            case 2:
                suffix = "nd"
            case 3:
                suffix = "rd"
        output_div.innerText = f"This is the {error_counter}{suffix} error."
    window.addEventListener("unhandledrejection", ffi.create_proxy(on_error))
    window.onError = on_error
    @when("click", ".button-container.button-actual.button-contents.button-img.button-text")
    async def clicked_button(event):
        current = event.target
        current = navigate_from_element(current, ["button-container", "button-actual", "button-contents", "button-img"])
        animate(current, [
            {"filter": "hue-rotate(90deg)"},
            {"filter": "hue-rotate(80deg)"},
            {"filter": "hue-rotate(70deg)"},
            {"filter": "hue-rotate(60deg)"},
            {"filter": "hue-rotate(50deg)"},
            {"filter": "hue-rotate(40deg)"},
            {"filter": "hue-rotate(30deg)"},
            {"filter": "hue-rotate(20deg)"},
            {"filter": "hue-rotate(10deg)"},
            {"filter": "hue-rotate(0deg)"}
        ],{
            "duration": 500,
            "iterations": 1
        }, restore_style=False)
        button_actual = navigate_from_element(current, ["button-container", "button-actual"])
        function_name = button_actual.getAttribute("custom-on-click")
        function = None
        for i in range(300):
            try:
                function = globals()[function_name]
                time.sleep(0.01)
                break
            except KeyError:
                pass
        if function is not None:
            try:
                await function(event)
            except TypeError:
                pass
    async def run_script(event):
        button_actual = navigate_from_element(event.target, ["button-container", "button-actual"])
        if not button_actual:
            return
        data = button_actual.getAttribute("custom-data")
        jdata = json.loads(data)
        worker_name = jdata["name"]
        try:
            worker = my_workers[worker_name]
            try:
                function_name = jdata["func"]
                my_worker = worker
                function = getattr(my_worker.sync, function_name)
                await function(*jdata['args'])
            except (KeyError, TypeError, AttributeError) as e:
                my_worker = worker
                await my_worker.sync.run(*jdata['args'])
        except (KeyError, TypeError, AttributeError) as e:
            window.reportError(f"exception occurred: {type(e).__name__}: {e}")

    async def generate(event):
        global output_div
        input_text = document.querySelector("#text_1")
        my_text = input_text.value
        output_div.innerText = f"{my_text} - {random.randint(1, 100)}"
    async def music(event):
        for music_obj in document.getElementsByClassName("background-music"):
            #audio_obj = document.querySelector("#background-music")
            audio_obj = music_obj
            audio_obj.muted = not audio_obj.muted
    old_music = ""
    async def apply_settings(event):
        def apply_music():
            global old_music
            for music_obj in document.getElementsByClassName("background-music"):
                # audio_obj = document.querySelector("#background-music")
                audio_obj = music_obj
                setting = document.querySelector("#music-slider")
                music_type = document.querySelector("#music-type")

                if audio_obj.getAttribute("name") == music_type.value:
                    if old_music != music_type.value:
                        old_music = music_type.value
                        audio_obj.currentTime = 0
                    audio_obj.volume = float(setting.value) / 100
                else:
                    audio_obj.volume = 0.0
                if interacted:
                    audio_obj.play()
        #await config_music()
        apply_music()
    async def config_music():
        for music_obj in document.getElementsByClassName("background-music"):
            # audio_obj = document.querySelector("#background-music")
            audio_obj = music_obj
            audio_obj.volume = 0.0
    await config_music()
    popup_classes = [
        "this-is-not-an-existing-class",
        "welcome-screen",
        "settings"
    ]

    async def music_on(event):
        setting = document.getElementById("music-slider")
        setting.setAttribute('value', "50")
        await apply_settings(event)
    async def music_off(event):
        setting = document.getElementById("music-slider")
        setting.setAttribute('value', "0")
        await apply_settings(event)

    def hide(event):
        for n in popup_classes:
            try:
                element = event.target
                element = navigate_from_element(element, [n])
                element.setAttribute("hidden", "true")
                break
            except AttributeError:
                continue

    @when("click", "*")
    async def click(event):
        global interacted
        #return
        time.sleep(0.001)
        interacted = True
        await apply_settings(None)
    def open_settings(event):
        try:

            settings_page = document.querySelector(".settings")

            settings_page.removeAttribute("hidden")
        except AttributeError:
            pass

    await sync_cookies()
    secret_answer = hashlib.sha256(secret_question.encode()).hexdigest()

    print("To resolve the developer access key:")

    print(secret_question)
    async def try_devkey(event, quiet=False, force_cookie=False):
        key_input = document.querySelector("#devkey-input")
        global developer_mode
        key:str = ""
        if not force_cookie:
            key = key_input.value
        if force_cookie:
            pass#key = "None"
        if await cookies.get('user-generated-key') is None:
            await cookies.set('user-generated-key', key)
        else:
            if not force_cookie:
                cookies.set('user-generated-key', key)
            data = (await cookies.get('user-generated-key')).value
            if key != data:
                key_input.value = data
                key = data

        if key == secret_answer:
            if not quiet: window.alert("Access granted")
            developer_mode = True
            for element in document.getElementsByClassName("developer-mode-element"):
                element.removeAttribute("hidden")
            for element in document.getElementsByClassName("user-mode-element"):
                element.setAttribute("hidden", "true")
        else:
            if not quiet: window.alert("Access denied")
            for element in document.getElementsByClassName("developer-mode-element"):
                element.setAttribute("hidden", True)
            for element in document.getElementsByClassName("user-mode-element"):
                element.removeAttribute("hidden")
            developer_mode = False
    await try_devkey(None, quiet=True, force_cookie=True)
    class VR():
        def __init__(self):
            self.x = 0
            self.y = 10
            self.z = 0
        def update(self):
            rig = document.getElementById("rig")
            rig.setAttribute("position", f"{self.x},{self.y} {self.z}")
    vr_player = VR()
    async def joystick(event):
        x = event.detail.x
        y = event.detail.y
    async def loop():
        try:
            document.querySelector('#rapid-random').innerText = random.randint(1, 100)
        except AttributeError:
            pass
        await apply_settings(None)
        schedule(77, loop)
        #vr_player.update()
    await loop()
except BaseException as e:
    def on_exception(my_e):
        raise my_e
    on_exception(e)
