from enum import Enum

import wechat_airtest
import wechat_pywinauto


class Language(Enum):
    en = 'en'
    zh = 'zh'


lang = Language.zh
i18n = {
    Language.zh: {
        'app_title': '微信',
        'app_class': 'WeChatMainWndForPC',
        'chats_button_title': '聊天',
        'contacts_button_title': '通讯录',
        'messages_button_title': '发消息',
        'message_input_title': '输入',
        'send_button_title': '发送(S)',
        'search_input_title': '搜索',
        'search_result_list_title': '搜索结果',
    },
    Language.en: {
        'app_title': 'WeChat',
        'app_class': 'WeChatMainWndForPC',
        'chats_button_title': 'Chats',
        'contacts_button_title': 'Contacts',
        'messages_button_title': 'Messages',
        'message_input_title': 'Enter',
        'send_button_title': 'Send (S)',
        'search_input_title': 'Search',
        'search_result_list_title': 'Search Results',
    },
}
wechat_version = '3.3.5.34'

if __name__ == '__main__':
    resources = i18n[lang]
    wechat_airtest.send('wechattestfriend', 'Hello, World! ——send by airtest', resources)
    wechat_pywinauto.send('wechattestfriend', 'Hello, World! ——send by pywinauto', resources)
    wechat_pywinauto.send_to_myself('Hello, World! ——send to myself by pywinauto', resources)
