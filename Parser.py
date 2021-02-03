#
#  Parser.py
#  eAUrnik
#

from lxml import html

def parse_block(block):
    if not block.xpath("table/tr/td[1]"):
        return
    title = block.xpath("table/tr/td[1]")[0].text.strip()
    class_attribute = block.get("class")
    if "ednevnik-seznam_ur_teden-td-odpadlo" in class_attribute:
        return
    # if "ednevnik-seznam_ur_teden-td-nadomescanje" in class_attribute:
    #     title += " (N)"
    if "ednevnik-seznam_ur_teden-td-zaposlitev" in class_attribute:
        title += " (Z)"
    if block.xpath("div"):
        subtitle_unformatted = block.xpath("div")[0].text.strip()
        subtitle_components = subtitle_unformatted.split(", ")
        subtitle = subtitle_components[1] + ", " + subtitle_components[0]
    else:
        subtitle = ""
    return (title, subtitle)

def lessons(page):
    tree = html.fromstring(page.content)
    if not tree.body.xpath("table"):
        return
    table = tree.body.xpath("table")[0]
    lines = table.xpath("tr")

    durations = []
    lessons = []

    for i in range(1, len(lines)):
        coloumns = lines[i].xpath("td")

        duration = coloumns[0].xpath("div[2]")[0].text
        durations.append(duration)

        rows = []
        for j in range(1, len(coloumns)):
            cell = coloumns[j]
            blocks = cell.xpath("div")
            if not blocks:
                rows.append([])
                continue
            coloumn_lessons = []
            parsed = parse_block(blocks[0])
            if parsed:
                coloumn_lessons = [parsed]
            for k in range(1, len(blocks)):
                block = blocks[k].xpath("div")[0]
                parsed = parse_block(block)
                if parsed:
                    coloumn_lessons.append(parsed)
            rows.append(coloumn_lessons)
        lessons.append(rows)

    lessons = list(map(list, zip(*lessons)))
    return (durations, lessons)
