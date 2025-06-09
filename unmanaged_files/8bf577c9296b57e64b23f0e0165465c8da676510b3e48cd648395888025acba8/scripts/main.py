import asyncio
import copy
import os
from math import radians
from typing import overload
from pyscript import document, window, when, workers, ffi, PyWorker
from pyscript.ffi import create_proxy
debug = False
class hbmckshb():
    pass
try:
    developer_mode = False
    keys_pressed = []
    import random, json, time, hashlib, math
    from threading import Thread
    from js import setTimeout, CSS, setInterval
    import js
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
    def generate_uid():
        return hashlib.sha256(f"{time.time_ns()}{random.randint(-1234567890, 1234567890)}".encode(), usedforsecurity=False).hexdigest()
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
    def hide_elem(event):
        event.target.setAttribute('hidden', True)
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


    class Vector:
        @overload
        def __init__(self, x: float, y: float, z: float = 0) -> None: ...
        @overload
        def __init__(self, position: list[float]) -> None:
            ...

        @overload
        def __init__(self, position: str, sep=' ') -> None:
            ...

        def __init__(self, x, y:float|str=None, z:float=0) -> None:
            self.VectorError = Exception
            if isinstance(x, str):
                if y is None:
                    y = ' '
                assert isinstance(y, str), TypeError("Parameter 'sep' must be str if constructing from string")
                position = [int(x.split(y)[i]) for i in range(len(x.split(y)))]
                self.x = position[0]
                self.y = position[1]
                self.z = position[2]
            elif isinstance(x, list):
                self.x = x[0]
                self.y = x[1]
                self.z = x[2]
            elif isinstance(x, float|int):
                if y is None:
                    y = 0
                self.x = x
                self.y = y
                self.z = z
        def distance_to(self, other: "Vector") -> float:
            dx = other.x - self.x
            dy = other.y - self.y
            dz = other.z - self.z
            return math.sqrt(dx * dx + dy * dy + dz * dz)
        def direction_to(self, other: "Vector") -> float:
            '''Note: This returns degrees
            Note: This is a 2D function. For the 3D function, see "direction_to_3D"'''
            return math.degrees(math.atan2(other.y - self.y, other.x - self.x))
        def direction_to_3D(self, other: "Vector"):
            my_xz = Vector(self.z, self.x)
            their_xz = Vector(other.z, other.x)
            yaw = my_xz.direction_to(their_xz) + 180
            hdist = self.x * math.sin(math.radians(yaw)) + self.z * math.cos(math.radians(yaw))
            my_wy = Vector(hdist, self.y)
            hdist = other.x * math.sin(math.radians(yaw)) + other.z * math.cos(math.radians(yaw))
            their_zy = Vector(hdist, other.y)
            pitch = my_wy.direction_to(their_zy)
            return Vector(pitch, yaw, 0)
        def copy(self):
            return Vector(self.x, self.y, self.z)
        def to_list(self) -> list[float]:
            return [self.x, self.y, self.z]

        def __iter__(self):
            yield self.x
            yield self.y
            yield self.z
        def to_str(self, sep=' '):
            return f"{self.x}{sep}{self.y}{sep}{self.z}"
        def __repr__(self):
            return f"Vector({self.x}, {self.y}, {self.z})"

        def __sub__(self, other: "Vector"):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

        def __add__(self, other: "Vector"):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        def __mul__(self, other):
            if isinstance(other, Vector):
                return Vector(self.x * other.x, self.y * other.y, self.z * other.z)
            elif isinstance(other, float|int):
                return Vector(self.x * other, self.y * other, self.z * other)
            else:
                raise self.VectorError("Supporting value of '*' operator must be int, float, or another Vector")
        def __truediv__(self, other):
            if isinstance(other, Vector):
                return Vector(self.x / other.x, self.y / other.y, self.z / other.z)
            elif isinstance(other, float | int):
                return Vector(self.x / other, self.y / other, self.z / other)
            else:
                raise self.VectorError("Supporting value of '*' operator must be int, float, or another Vector")
        def __round__(self, n=None):
            return Vector(round(self.x, n), round(self.y, n), round(self.z, n))

        def __hex__(self):
            return '#{0:02x}{1:02x}{2:02x}'.format(
                max(0, min(255, round(self.x))),
                max(0, min(255, round(self.y))),
                max(0, min(255, round(self.z)))
            )
    class VR():
        class GameMenu():
            def __init__(self):
                self.menu_obj = document.querySelector('a-scene').querySelector('#rig').querySelector('#virtual-menu')

            def closest_button(self, cursor: Vector, get_all: bool = False):
                button_tmp = {'button-id': 'None', 'distance': 65535.0, 'model': None}
                buttons = [button_tmp.copy()]
                for button in self.menu_obj.getElementsByClassName('a-button'):
                    if button.hasAttribute('hidden'):
                        continue
                    button_tmp['button-id'] = str(button.getAttribute('id'))
                    position = js.THREE.Vector3.new()
                    button.querySelector('a-sphere').object3D.getWorldPosition(position)
                    button_tmp['model'] = button.querySelector('a-gltf-model')
                    position = list(position.to_py())
                    button_pos = Vector(position)
                    button_tmp['distance'] = button_pos.distance_to(cursor)
                    if button_tmp['distance'] < buttons[0]['distance']:
                        buttons.insert(0, button_tmp.copy())
                    else:
                        buttons.append(button_tmp.copy())
                buttons.remove({'button-id': 'None', 'distance': 65535.0, 'model': None})
                return buttons[0] if not get_all else buttons
        class Game():
            class data:
                x = 0
                y = 0
                z = 0

            def __init__(self):
                pass
            async def load_level(self, level_path:str):
                def parse_xml(xml_text: str):
                    parser = window.DOMParser.new()
                    xml_doc = parser.parseFromString(xml_text, "application/xml")
                    return xml_doc

                async def fetch_level_xml(path: str):
                    response = await window.fetch(path)
                    xml_text = await response.text()
                    return xml_text
                my_level = parse_xml(await fetch_level_xml(level_path))
                assets = document.querySelector('#assets')
                scene = document.querySelector('#scene')
                level_assets = my_level.querySelector('body').getElementsByTagName('a-assets')[0]
                level_scene = my_level.querySelector('body').getElementsByTagName('a-entity')[0]
                player_data = my_level.querySelector('head').querySelector('#player-data').getAttribute('value')
                jdata = json.loads(player_data)
                self.data.x = jdata['x']
                self.data.y = jdata['y']
                self.data.z = jdata['z']

                assets.replaceWith(level_assets)
                scene.replaceWith(level_scene)
            def get_closest_object(self, group, cursor:Vector):
                button_tmp = {'id':'None', 'distance':65535.0}
                buttons = [button_tmp.copy()]
                for button in group.children:
                    if not button.object3D.visible:
                        pass
                    if not button.hasAttribute('id'):
                        button.setAttribute('id', generate_uid())
                    button_tmp['id'] = str(button.id)
                    position = js.THREE.Vector3.new()
                    button.object3D.getWorldPosition(position)
                    position = list(position.to_py())
                    button_pos = Vector(position)
                    button_tmp['distance'] = button_pos.distance_to(cursor)
                    if button_tmp['distance'] < buttons[0]['distance']:
                        buttons.insert(0, button_tmp.copy())
                    else:
                        buttons.append(button_tmp.copy())
                buttons.remove({'id':'None', 'distance':65535.0})
                return buttons[0]
            def world_pos(self, element):
                position = js.THREE.Vector3.new()
                element.object3D.getWorldPosition(position)
                position = list(position.to_py())
                return Vector(position)

        def __init__(self):
            self.x = 0
            self.y = 10
            self.z = 0
            self.width = 1
            self.height = 1

            self.fatness = 0.7
            self.head_height = 0.4
            self.step_width = 0.5
            self.step_height = 0.4
            self.tallness = 1.5

            self.y_velocity = 0
            self.z_velocity = 0
            self.x_velocity = 0
            self.rotation = 0
            self.r_velocity = 0
            self.gravity = 9.8
            self.jump_height = 1
            self.gravity_mul = 1
            self.selected_item = document.querySelector('a-scene').querySelector("#nothing")
            self.last_selected = document.querySelector('a-scene').querySelector("#nothing")
            self.prev_selected = document.querySelector('a-scene').querySelector("#nothing")

            self.last_selected_properties = {
                'visible': bool
            }
            self.initial_selected_properties = self.last_selected_properties.copy()
            self.output_gravity = self.gravity * self.gravity_mul
            self.target_fps = 60
            self.ljx = 0
            self.ljy = 0
            self.rjx = 0
            self.rjy = 0
            self.transformation_disable_x = False
            self.transformation_disable_y = False
            self.transformation_disable_z = False
            self.level_counter = 0
            self.collision_velocity = 0.001
            self.colliding_feet = False
            self.colliding_body_x = False
            self.colliding_body_z = False
            self.colliding_body_xp = False
            self.colliding_body_zp = False
            self.colliding_body_xn = False
            self.colliding_body_zn = False
            self.selected_transformation = 'position'
            self.squishing_x = False
            self.squishing_z = False
            self.look_up_down = 0
            self.look_up_down_v = 0
            self.in_vr = window.AFRAME.utils.device.isMobileVR()
            self.is_vr = window.AFRAME.utils.device.isMobileVR()
            self.debug_mode = False
            self.clicked = False
            self.changed_selected_transformation = False
            self.holding_rt = False
            self.holding_lt = False
            self.last_cursor_position = Vector(0, 0, 0)
            self.current_cursor_pos = Vector(0, 0, 0)
            self.menu = self.GameMenu()
            self.game = self.Game()
            self.aframe = document.getElementsByTagName('a-scene')[0]
            self.playfield = self.aframe.querySelector('#scene')
            self.rig = self.aframe.querySelector("#rig")
            self.rig_rotating = self.rig.querySelector('#rig-rotate')
            self.rig_camera = self.rig.querySelector('#camera')
            self.gizmo = self.aframe.getElementsByClassName('a-debug')[0]
            self.gizmo_mode_indic = self.gizmo.querySelector('.mode-indicator')
            self.optimized_shadow_caster = self.playfield.querySelector('.optimized-shadow-caster')
            self.shadow_camera_rotation = None
            self.gizmo_no_x = self.gizmo.querySelector('.no-x')
            self.gizmo_no_y = self.gizmo.querySelector('.no-y')
            self.gizmo_no_z = self.gizmo.querySelector('.no-z')
            self.xz_velocity_smoothing = 0.75
            self.walking_speed = 1
            self.lgrip_pressed = False
            self.help_text_enabled = True
            self.colliding_objects = {
                'feet':[],
                'toes':[]
            }
            self.timers =[
                0.0,
                0.0
            ]
            self.update_external = lambda: None
            self.script_ids = []
            self.colliding_toes = False
            self.loading = False


            self.load_scripts()

        def load_scripts(self):
            scripts = document.querySelectorAll('script')
            for script in scripts:
                if not script.type == 'custom-python':
                    continue
                exec(script.innerText, globals())
                self.script_ids.append(script.id)
                globals()[self.script_ids[-1]] = Module()
        def run_scripts(self):
            for script_id in self.script_ids:
                try:
                    globals()[script_id].__main__()
                except:
                    self.script_ids.remove(script_id)
                    raise
        async def load_level(self, level_path:str):
            #js.THREE.Cache.clear()
            successful=False
            try:
                await self.game.load_level(level_path)
                self.pull_from_class_game()
                successful=True
            except:
                try:
                    self.level_counter = -1
                    await self.game.load_level('./credits.xml')
                    self.pull_from_class_game()
                except:
                    await self.game.load_level('./title-screen.xml')
                    self.pull_from_class_game()
            self.y_velocity = 0
            self.rotation = 0
            self.load_scripts()
            return successful
        def pull_from_class_game(self):
            for name in dir(self.game.data):
                if not name.startswith('_') and not callable(getattr(self.game.data, name)):
                    setattr(self, name, getattr(self.game.data, name))
        def refresh_object_cache(self):
            self.aframe = document.getElementsByTagName('a-scene')[0]
            self.playfield = self.aframe.querySelector('#scene')
            self.optimized_shadow_caster = self.playfield.querySelector('.optimized-shadow-caster')
        def update_player_collider(self):
            collider = self.rig.querySelector('#colliders')
            collider.object3D.scale.set(self.width, self.height, self.width)
        def switch_debug_mode(self, active:bool):
            my_scene = document.getElementsByTagName('a-scene')[0]
            if active:
                my_scene.querySelector('.a-debug').setAttribute('src', '#gizmo')
            else:
                my_scene.querySelector('.a-debug').setAttribute('src', '#dot-cursor')
        def scale(self):
            feet = self.rig.querySelector('#player-collider-feet')
            toes = self.rig.querySelector('#player-collider-toes')
            toes_graphic = self.rig.querySelector('#toes-graphic')

            north = self.rig.querySelector('#player-collider-body-zn')
            south = self.rig.querySelector('#player-collider-body-zp')
            east = self.rig.querySelector('#player-collider-body-xp')
            west = self.rig.querySelector('#player-collider-body-xn')
            head = self.rig.querySelector('#player-collider-head')

            step_height = self.step_height
            step_width = self.step_width
            fatness = self.fatness
            tallness = self.tallness
            head_height = self.head_height
            feet_pos = Vector(0, step_height / 2, 0)
            feet_scale = Vector(step_width, step_height, step_width)
            toes_graphic_scale = Vector(step_width, step_width, 1)
            toes_pos = Vector(0, 0, 0)
            toes_scale = Vector(step_width, 0.05, step_width)
            n_pos = Vector(0, step_height + tallness / 2, fatness / -2)
            s_pos = Vector(0, step_height + tallness / 2, fatness / 2)
            e_pos = Vector(fatness / 2, step_height + tallness / 2, 0)
            w_pos = Vector(fatness / -2, step_height + tallness / 2, 0)
            ns_scale = Vector(fatness - 0.021, tallness, 0.01)
            ew_scale = Vector(0.01, tallness, fatness - 0.021)
            head_pos = Vector(0, step_height + tallness, 0)
            head_scale = Vector(step_width, head_height, step_width)
            feet.object3D.position.set(*feet_pos)
            toes.object3D.position.set(*toes_pos)
            north.object3D.position.set(*n_pos)
            south.object3D.position.set(*s_pos)
            east.object3D.position.set(*e_pos)
            west.object3D.position.set(*w_pos)
            head.object3D.position.set(*head_pos)

            feet.object3D.scale.set(*feet_scale)
            toes.object3D.scale.set(*toes_scale)
            north.object3D.scale.set(*ns_scale)
            south.object3D.scale.set(*ns_scale)
            east.object3D.scale.set(*ew_scale)
            west.object3D.scale.set(*ew_scale)
            head.object3D.scale.set(*head_scale)

            toes_graphic.object3D.scale.set(*toes_graphic_scale)

        async def update(self):
            if self.timers[0] < time.time():
                self.timers[0] = time.time() + 2
                self.refresh_object_cache()
                self.update_player_collider()
            if self.timers[1] < time.time():
                self.scale()
                self.timers[1] = time.time() + 0.1
                self.aframe.renderer.shadowMap.needsUpdate = True
                if self.optimized_shadow_caster is not None and hasattr(self.optimized_shadow_caster, 'object3D'):
                    light_obj = self.optimized_shadow_caster.object3D.children[
                        0]  # children[0] is usually the actual THREE.DirectionalLight

                    # Update the light's position (relative to player)
                    self.optimized_shadow_caster.object3D.position.set(self.x / 2 - 20, self.y / 2 + 20, self.z / 2 + 20)

                    # Set the light's target position (where it shines towards)
                    light_obj.target.position.set(self.x / 2, self.y / 2, self.z / 2)

                    # Make sure the target is in the scene graph
                    self.aframe.object3D.add(light_obj.target)
            my_scene = self.aframe
            rig = self.rig
            gizmo = self.gizmo
            scene_level = self.playfield
            self.x += min(max(self.x_velocity, -(not self.colliding_body_xn)), not self.colliding_body_xp)
            if self.colliding_feet:
                self.y_velocity = max(self.y_velocity, 0)
            gizmo_scale = self.rjy * 0.75 + 1.25
            gizmo_scale /= 2
            transformation_multiplier = self.rjy * 0.9 + 1
            self.y += self.y_velocity / self.target_fps
            self.y += self.colliding_feet * self.collision_velocity
            self.collision_velocity += 0.001

            self.z += min(max(self.z_velocity, -(not self.colliding_body_zn)), not self.colliding_body_zp)
            self.rotation += self.r_velocity
            self.look_up_down += self.look_up_down_v
            self.y_velocity -= self.output_gravity / self.target_fps

            rig.object3D.position.set(self.x, self.y, self.z)
            self.rig_rotating.object3D.rotation.set(0, math.radians(self.rotation), 0)
            if not self.in_vr: self.rig_camera.object3D.rotation.set(math.radians(self.look_up_down), 0, 0)



            debug_text = self.gizmo.querySelector('.text')
            #debug_text = self.playfield.querySelector('#xyz-balls')
            player_position = self.game.world_pos(rig.querySelector('#camera'))
            text_position = self.game.world_pos(debug_text)
            new_rotation = text_position.direction_to_3D(player_position)
            debug_text.object3D.rotation.set(-math.radians(new_rotation.x), math.radians(new_rotation.y), math.pi)
            debug_text.object3D.scale.set(1 / gizmo_scale, 1 / gizmo_scale, 1 / gizmo_scale)
            debug_text.object3D.position.set(*((player_position - text_position) / 2.7))
            debug_text_string = ""

            if self.help_text_enabled:
                if self.is_vr:
                    help_text = [
                        'Left Stick: Move around',
                        'Right Stick: Look',
                        'RT: Action',
                        'LB: Modifier',
                        'LT: Change tool',
                        'A: Jump',
                        '--DEBUG MODE CONTROLS--',
                        'Y: New Cube',
                        'X: Disable some axes',
                        'LB+X: Delete object',
                        'Press A to hide'
                    ]
                else:
                    help_text = [
                        'WASD: Move around',
                        'Arrow keys: Look',
                        'E: Action',
                        '1: Modifier',
                        'Q: Change tool',
                        'SPACE: Jump',
                        '--DEBUG MODE CONTROLS--',
                        'N: New Cube',
                        'X: Disable some axes',
                        '1+X: Delete object',
                        'Press SPACE to hide'
                    ]
                debug_text_string += '\n'.join(help_text)
                if self.y_velocity > 1:
                    self.help_text_enabled = False



            anchor = my_scene.querySelector('#gizmo-anchor' if self.in_vr else '#gizmo-anchor-head')

            position = js.THREE.Vector3.new()
            anchor.object3D.getWorldPosition(position)
            position = list(position.to_py())
            anchor_position = Vector(position)
            if self.debug_mode:
                debug_text_string += f'Feet position: {round(Vector(self.x, self.y, self.z), 2).to_str()}\n'
                debug_text_string += f'Head position: {round(player_position, 2).to_str()}\n'
                debug_text_string += f'Cursor position: {round(anchor_position, 2).to_str()}\n'

            debug_text.setAttribute('value', debug_text_string)


            clicked = self.clicked
            self.clicked = False
            buttons = self.menu.closest_button(anchor_position, get_all=True)
            button_details = buttons.pop(0)
            touching_button = button_details['distance'] < 0.07
            self.current_cursor_pos = anchor_position
            if touching_button:
                button_details['model'].object3D.position.set(0.01, 0, 0)
                if clicked:
                    if button_details['button-id'] == 'button-debug':
                        self.debug_mode = not self.debug_mode
                    elif button_details['button-id'] == 'button-unstuck':
                        self.x = 0
                        self.z = 0
                        self.y = 5
                        self.y_velocity = 0
                    elif button_details['button-id'] == 'button-test':
                        self.rotation += 90
                self.last_selected.object3D.visible = self.last_selected_properties['visible']
                self.selected_item.object3D.visible = self.initial_selected_properties['visible']
            else:
                button_details['model'].object3D.position.set(0, 0, 0)
                if self.debug_mode:
                    my_id = self.game.get_closest_object(group=scene_level, cursor=anchor_position)['id']
                    selected = self.selected_item
                    assert selected is not None, TypeError(f'Object with id {my_id} seems to be None')
                    if not selected.hasAttribute('material'):
                        selected.setAttribute('material', '')
                    #selected.setAttribute('material', f'opacity: {math.sin(time.time() * math.tau) / 4 + 0.75}; transparent: true')
                    selected.object3D.visible = math.sin(time.time() * math.tau * 4) > -0.35
                    self.last_selected.object3D.visible = self.last_selected_properties['visible']


                    if self.holding_lt or ('q' in keys_pressed):
                        if not self.changed_selected_transformation:
                            self.changed_selected_transformation = True
                            match self.selected_transformation:
                                case 'position':
                                    self.selected_transformation = 'rotation'
                                    gizmo.children[0].setAttribute('src', '#gizmo-r')
                                case 'rotation':
                                    self.selected_transformation = 'scale'
                                    gizmo.children[0].setAttribute('src', '#gizmo-s')
                                case 'scale':
                                    self.selected_transformation = 'color'
                                    gizmo.children[0].setAttribute('src', '#gizmo-c')
                                case 'color':
                                    self.selected_transformation = 'position'
                                    gizmo.children[0].setAttribute('src', '#gizmo-p')

                    else:
                        self.changed_selected_transformation = False
                    if self.holding_rt or ('e' in keys_pressed):
                        #selected.object3D.position.set(0, 0, 0)
                        selected_transformation = self.selected_transformation
                        if not selected.hasAttribute(selected_transformation):
                            selected.setAttribute(selected_transformation, '0 0 0' if selected_transformation != 'scale' else '1 1 1')
                        else:
                            try:
                                relative_pos = list(selected.getAttribute(selected_transformation).to_py())
                                relative_pos = Vector(relative_pos[0], relative_pos[1], relative_pos[2])
                            except ValueError:
                                relative_pos = list(selected.getAttribute(selected_transformation).to_py().values())
                                relative_pos = Vector(relative_pos[0], relative_pos[1], relative_pos[2])
                            except AttributeError:
                                if selected_transformation == 'color':
                                    try:
                                        colorstring = selected.getAttribute(selected_transformation)[1:]
                                        r = int(colorstring[:2], 16)
                                        g = int(colorstring[2:4], 16)
                                        b = int(colorstring[4:6], 16)
                                        relative_pos = Vector(r, g, b)
                                    except ValueError:
                                        relative_pos = Vector(255, 255, 255)
                                else:
                                    raise
                            delta_pos = anchor_position - self.last_cursor_position
                            if selected_transformation == 'rotation':
                                delta_pos *= Vector(360, 360, 360)
                            elif selected_transformation == 'color':
                                delta_pos *= 255
                            delta_pos *= Vector(transformation_multiplier, transformation_multiplier, transformation_multiplier)
                            delta_pos *= Vector(
                                not self.transformation_disable_x,
                                not self.transformation_disable_y,
                                not self.transformation_disable_z
                            )
                            new_pos = Vector(
                                relative_pos.x +
                                delta_pos.x,
                                relative_pos.y +
                                delta_pos.y,
                                relative_pos.z +
                                delta_pos.z
                            )
                            match selected_transformation:
                                case 'position':
                                    selected.object3D.position.set(new_pos.x, new_pos.y, new_pos.z)
                                case 'rotation':
                                    selected.setAttribute(selected_transformation, new_pos.to_str())
                                case 'scale':
                                    selected.setAttribute(selected_transformation, new_pos.to_str())
                                case 'color':
                                    selected.setAttribute(selected_transformation, (new_pos).__hex__())

                        #selected.setAttribute('visible', 'false')
                        #selected.setAttribute('position', anchor_position.to_str())
                    else:
                        self.selected_item = scene_level.querySelector("#" + CSS.escape(my_id))
                else:
                    self.last_selected.object3D.visible = self.last_selected_properties['visible']
                    self.selected_item.object3D.visible = self.initial_selected_properties['visible']

            for button in buttons:
                try:
                    button['model'].object3D.position.set(0, 0, 0)
                except AttributeError:
                    pass
            mi = self.gizmo_mode_indic
            mi.object3D.visible = self.debug_mode
            self.gizmo_no_x.object3D.visible = self.transformation_disable_x and self.debug_mode
            self.gizmo_no_y.object3D.visible = self.transformation_disable_y and self.debug_mode
            self.gizmo_no_z.object3D.visible = self.transformation_disable_z and self.debug_mode

            self.switch_debug_mode(self.debug_mode) #

            gizmo.object3D.position.set(position[0], position[1], position[2])
            gizmo.object3D.scale.set(gizmo_scale, gizmo_scale, gizmo_scale)


            x = self.ljx
            y = -self.ljy
            direction = math.atan2(y, x) * 180 / math.pi
            strength = math.sqrt(x * x + y * y)
            direction += self.rotation + 180
            direction = direction * math.pi / 180
            x = math.cos(direction) * -strength
            y = math.sin(direction) * strength
            self.x_velocity = (x / 10 * self.walking_speed) * (100 - self.xz_velocity_smoothing * 100) + self.x_velocity * self.xz_velocity_smoothing * 100
            self.z_velocity = (y / 10 * self.walking_speed) * (100 - self.xz_velocity_smoothing * 100) + self.z_velocity * self.xz_velocity_smoothing * 100
            self.x_velocity /= 100
            self.z_velocity /= 100
            self.last_cursor_position = anchor_position.copy()
            if not self.selected_item == self.prev_selected:
                self.last_selected_properties = self.initial_selected_properties.copy()
                self.initial_selected_properties['visible'] = self.selected_item.object3D.visible
                self.last_selected = self.prev_selected
                self.prev_selected = self.selected_item
            closest_obj_to_feet = self.game.get_closest_object(group=scene_level, cursor=Vector(self.x, self.y, self.z))
            distance_to_goal = closest_obj_to_feet['distance'] if closest_obj_to_feet['id'] == 'level-goal' else 65535
            if distance_to_goal < 1 and not self.loading:
                self.loading = True
                print(f'Loading level {self.level_counter}...')
                successful_load = await self.load_level(f'./regular-levels/level{self.level_counter}.xml')
                if successful_load:
                    print(f'Level {self.level_counter} loaded.')
                    self.level_counter += 1
                else:
                    print(f'Level {self.level_counter} not loaded.')
                    self.level_counter = 0
                self.loading = False
            self.update_external(self)
            self.run_scripts()
    vr_player = VR()
    def extern_update(self):
        pass
    vr_player.update_external = extern_update
    await vr_player.load_level('./title-screen.xml')


    async def vr_trigger(event):
        vr_player.clicked = True
        vr_player.holding_rt = True


    async def vr_untrigger(event):
        vr_player.holding_rt = False


    async def vr_ltrigger(event):
        vr_player.holding_lt = True


    async def vr_luntrigger(event):
        vr_player.holding_lt = False

    async def vr_y_down(event):
        if vr_player.debug_mode:
            cube = document.createElement('a-box')
            cube.setAttribute('width', 1.0)
            cube.setAttribute('height', 1.0)
            cube.setAttribute('depth', 1.0)
            cube.setAttribute('position', vr_player.current_cursor_pos.to_str())
            cube.setAttribute('obb-collider', '')
            scene_level = document.querySelector('a-scene').querySelector('#scene')
            scene_level.append(cube)
    async def vr_x_down(event):
        if vr_player.debug_mode:
            if not vr_player.lgrip_pressed:
                disabled_axes = 0
                disabled_axes |= vr_player.transformation_disable_x
                disabled_axes |= vr_player.transformation_disable_y << 1
                disabled_axes |= vr_player.transformation_disable_z << 2
                disabled_axes += 1
                disabled_axes = disabled_axes % 8
                vr_player.transformation_disable_x = bool((disabled_axes & 1) >> 0)
                vr_player.transformation_disable_y = bool((disabled_axes & 2) >> 1)
                vr_player.transformation_disable_z = bool((disabled_axes & 4) >> 2)
            else:
                vr_player.selected_item.remove()
    async def vr_joystick(event):
        try:
            x = event.detail.x
            y = event.detail.y
        except AttributeError:
            w = bool('w' in keys_pressed)
            a = bool('a' in keys_pressed)
            s = bool('s' in keys_pressed)
            d = bool('d' in keys_pressed)
            if 'i' in keys_pressed:
                vr_player.debug_mode = not vr_player.debug_mode
            if vr_player.debug_mode:
                if 'o' in keys_pressed:
                    vr_player.rotation += 15
            if 'n' in keys_pressed:
                await vr_y_down(None)
            if 'x' in keys_pressed:
                await vr_x_down(None)
            if '1' in keys_pressed:
                vr_player.lgrip_pressed = True
            else:
                vr_player.lgrip_pressed = False
            x = d-a
            y = s-w
        vr_player.ljx = x
        vr_player.ljy = y
    async def vr_look(event):
        try:
            x = event.detail.x
            y = 0
        except AttributeError:
            w = bool('arrowup' in keys_pressed)
            a = bool('arrowleft' in keys_pressed)
            s = bool('arrowdown' in keys_pressed)
            d = bool('arrowright' in keys_pressed)
            x = d-a
            y = w-s
        vr_player.look_up_down_v = y * 3
        vr_player.r_velocity = x * -3
        vr_player.rjx = x
        if event is not None:
            y = event.detail.y
        vr_player.rjy = y
    @when('keydown', '*')
    def vr_rise(event):
        if not vr_player.colliding_toes:
            return
        try:
            if event.key == ' ':
                vr_player.y_velocity = math.sqrt(2 * vr_player.output_gravity * vr_player.jump_height)
        except AttributeError:
            vr_player.y_velocity = math.sqrt(2 * vr_player.output_gravity * vr_player.jump_height)


    @when('keydown', '*')
    async def key_pressed(event):
        if not event.key.lower() in keys_pressed:
            keys_pressed.append(event.key.lower())
            await vr_joystick(None)
            await vr_look(None)

    @when('keyup', '*')
    async def key_released(event):
        if event.key.lower() in keys_pressed:
            keys_pressed.remove(event.key.lower())
            await vr_joystick(None)
            await vr_look(None)
    def vr_player_collide(event):
        if event.target.id == 'player-collider-feet':
            if not event.detail.withEl.hasAttribute('id'):
                event.detail.withEl.id = generate_uid()
            if event.detail.withEl.id == 'player-collider-toes':
                return
            if not event.detail.withEl.id in vr_player.colliding_objects['feet']:

                vr_player.colliding_objects['feet'].append(event.detail.withEl.id)
                if len(vr_player.colliding_objects['feet']) != 0:
                    vr_player.colliding_feet = True
                    vr_player.collision_velocity = 0.0001
        elif event.target.id == 'player-collider-toes':
            if not event.detail.withEl.hasAttribute('id'):
                event.detail.withEl.id = generate_uid()
            if event.detail.withEl.id == 'player-collider-feet':
                return
            if not event.detail.withEl.id in vr_player.colliding_objects['toes']:

                vr_player.colliding_objects['toes'].append(event.detail.withEl.id)
                if len(vr_player.colliding_objects['toes']) != 0:
                    vr_player.colliding_toes = True
        else:
            match event.target.id:
                case 'player-collider-body-xp' | 'player-collider-body-xn':
                    if vr_player.colliding_body_x:
                        vr_player.squishing_x = True
                    vr_player.colliding_body_x = True
                case 'player-collider-body-zp' | 'player-collider-body-zn':
                    if vr_player.colliding_body_z:
                        vr_player.squishing_z = True
                    vr_player.colliding_body_z = True
            match event.target.id:
                case 'player-collider-body-xp':
                    vr_player.colliding_body_xp = True
                case 'player-collider-body-zp':
                    vr_player.colliding_body_zp = True
                case 'player-collider-body-xn':
                    vr_player.colliding_body_xn = True
                case 'player-collider-body-zn':
                    vr_player.colliding_body_zn = True
        if vr_player.squishing_z and vr_player.squishing_z:
            vr_player.y_velocity = 0

    def vr_player_uncollide(event):
        if event.target.id == 'player-collider-feet':
            if not event.detail.withEl.hasAttribute('id'):
                event.detail.withEl.id = generate_uid()
            if event.detail.withEl.id == 'player-collider-toes':
                return
            if event.detail.withEl.id in vr_player.colliding_objects['feet']:
                vr_player.colliding_objects['feet'].remove(event.detail.withEl.id)
                if len(vr_player.colliding_objects['feet']) == 0: vr_player.colliding_feet = False
        elif event.target.id == 'player-collider-toes':
            if not event.detail.withEl.hasAttribute('id'):
                event.detail.withEl.id = generate_uid()
            if event.detail.withEl.id == 'player-collider-feet':
                return
            if event.detail.withEl.id in vr_player.colliding_objects['toes']:
                vr_player.colliding_objects['toes'].remove(event.detail.withEl.id)
                if len(vr_player.colliding_objects['toes']) == 0: vr_player.colliding_toes = False

        else:
            match event.target.id:
                case 'player-collider-body-xp' | 'player-collider-body-xn':
                    if not vr_player.squishing_x:
                        vr_player.colliding_body_x = False
                    vr_player.squishing_x = False
                case 'player-collider-body-zp' | 'player-collider-body-zn':
                    if not vr_player.squishing_z:
                        vr_player.colliding_body_z = False
                    vr_player.squishing_z = False
            match event.target.id:
                case 'player-collider-body-xp':
                    vr_player.colliding_body_xp = False
                case 'player-collider-body-zp':
                    vr_player.colliding_body_zp = False
                case 'player-collider-body-xn':
                    vr_player.colliding_body_xn = False
                case 'player-collider-body-zn':
                    vr_player.colliding_body_zn = False

    async def loop():
        try:
            pass#document.querySelector('#rapid-random').innerText = random.randint(1, 100)
        except AttributeError:
            pass
        await apply_settings(None)
        try:
            if document.querySelector('a-scene') is not None:
                await vr_player.update()
        except BaseException as e:
            print(f"{e.__traceback__.tb_next.tb_lineno} {type(e).__name__} {e}")
    interval_func = ffi.create_proxy(loop)
    setInterval(interval_func, 16)
except BaseException as e:
    def on_exception(my_e):
        raise my_e
    on_exception(e)
