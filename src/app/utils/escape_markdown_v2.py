import re


def escape_markdown_v2(text):
    special_chars = r'_*[]()~`>#+-=|{}.!'
    return re.sub(r'([%s])' % re.escape(special_chars), r'\\\1', text)
