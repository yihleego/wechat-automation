import time

from pywinauto.application import Application
from pywinauto.controls.hwndwrapper import HwndWrapper
from pywinauto.findwindows import find_windows


def send(friend, message, resources):
    # Activate wechat window
    handles = find_windows(title_re=resources['app_title'])
    handle = handles[0]
    wrapper = HwndWrapper(handle).set_focus()
    wrapper.set_focus()
    wrapper.move_window(0, 0)
    # Obtain wechat application
    app = Application(backend='uia')
    app.connect(handle=handle)
    wechat = app.window(class_name=resources['app_class'])
    wechat.draw_outline(colour='red')

    # Find the 'Chats'
    chats = wechat.child_window(control_type='Button', title=resources['chats_button_title'])
    chats.click_input()
    # Search the friend
    search = wechat.child_window(control_type='Edit', title=resources['search_input_title'])
    search.click_input()
    search.type_keys('^a')
    search.type_keys(friend, with_spaces=True, with_tabs=True, with_newlines=True)
    # Wait for the result
    time.sleep(2)
    # Select the friend
    search_result_list = wechat.child_window(control_type='List', title=resources['search_result_list_title'])
    search_result_item = search_result_list.child_window(control_type='ListItem', title=friend)
    if not search_result_item.exists():
        raise Exception("Friend named '{0}' cannot be found.".format(friend))
    search_result_item.click_input()

    # Send messages
    text_edit = wechat.child_window(control_type='Edit', title=resources['message_input_title'])
    text_edit.type_keys('^a')
    text_edit.type_keys(message, with_spaces=True, with_tabs=True, with_newlines=True)
    send_button = wechat.child_window(control_type='Button', title=resources['send_button_title'])
    send_button.click_input()


def send_to_myself(message, resources):
    # Activate wechat window
    handles = find_windows(title_re=resources['app_title'])
    handle = handles[0]
    wrapper = HwndWrapper(handle).set_focus()
    wrapper.set_focus()
    wrapper.move_window(0, 0)
    # Obtain wechat application
    app = Application(backend='uia')
    app.connect(handle=handle)
    wechat = app.window(class_name=resources['app_class'])
    wechat.draw_outline(colour='red')

    # Find the navigate, and click the avatar
    contacts = wechat.child_window(control_type='Button', title=resources['contacts_button_title'])
    navigate = contacts.parent()
    avatar = navigate.children()[0]
    avatar.click_input()
    # Click the 'Messages' button
    messages = wechat.child_window(control_type='Button', title=resources['messages_button_title'])
    messages.click_input()

    # Send messages
    text_edit = wechat.child_window(control_type='Edit', title=resources['message_input_title'])
    text_edit.type_keys('^a')
    text_edit.type_keys(message, with_spaces=True)
    send_button = wechat.child_window(control_type='Button', title=resources['send_button_title'])
    send_button.click_input()
