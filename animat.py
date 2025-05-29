from pyscript import document, window, when
debug = False
try:
    import random, json, time
    def basic_click_button(event):
        clicked_element = event.target
        def anim(elem):
            for i in range(50):
                elem.style.filter = f"brightness({i + 50}%);"
                time.sleep(0.01)

except BaseException as e:
    raise e
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
