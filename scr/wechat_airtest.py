from airtest.core.api import *
from pywinauto.controls.hwndwrapper import HwndWrapper
from pywinauto.findwindows import find_windows


def send(friend, message, resources):
    # Activate wechat window
    handles = find_windows(title_re=resources['app_title'])
    handle = handles[0]
    wrapper = HwndWrapper(handle).set_focus()
    wrapper.set_focus()
    wrapper.move_window(0, 0)
    # Connect wechat device
    app = connect_device("Windows:///" + str(handle))
    app.set_foreground()
    # Click the 'Chats' button
    chats = exists(Template(r"assets/chats_active.png"))
    if not chats:
        chats = exists(Template(r"assets/chats_inactive.png"))
    if not chats:
        raise Exception("'Chats' button cannot be found.")
    touch(chats)
    sleep(1)
    # Click the search input box
    search = exists(Template(r"assets/search.png"))
    if not search:
        raise Exception("Search input box cannot be found.")
    touch((search[0] + 30, search[1]))
    sleep(1)
    # Search the friend
    text(text=friend)
    sleep(1)
    keyevent("{ENTER}")
    sleep(1)
    # Send messages
    text(message)
    sleep(1)
    keyevent("{ENTER}")
    sleep(1)
