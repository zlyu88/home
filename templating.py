def insert_values(content, template):
    import re

    content['message'] = "<div class='alert'><p>%s</p></div>" % content

    page = template
    for key in content.keys():
        page = page.replace("%" + key, content[key])

    # page = re.sub("%[a-z]+", "", page)

    return page


def load_page(content, path):
    f = open(path, 'r')
    return insert_values(content, f.read())
