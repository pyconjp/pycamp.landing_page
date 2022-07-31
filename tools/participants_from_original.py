import csv
from pathlib import Path
from urllib.request import urlopen

from bs4 import BeautifulSoup, Tag


def parse_place(td_place: Tag) -> tuple[str, str]:
    """
    >>> raw_td = '<td><a href="https://pyconjp.connpass.com/event/33014/" target="_blank">京都</a></td>'
    >>> td_place = BeautifulSoup(raw_td, "html.parser").td
    >>> parse_place(td_place)
    ('京都', 'https://pyconjp.connpass.com/event/33014/')
    """
    return td_place.text, td_place.a["href"]


def parse_count(td_count: Tag) -> str:
    """
    >>> raw_td = '<td>一般参加11人、学生1人</td>'
    >>> td_count = BeautifulSoup(raw_td, "html.parser").td
    >>> parse_count(td_count)
    '一般参加11人、学生1人'
    """
    return td_count.text


if __name__ == "__main__":
    tools_dir = Path(__file__).parent
    output_dir = tools_dir.parent / "source" / "sections"
    csv_path = output_dir / "participants_count.csv"

    with urlopen("https://peraichi.com/landing_pages/view/pycamp") as res:
        raw_html = res.read()

    soup = BeautifulSoup(raw_html, "html.parser")
    body = soup.body
    tables = body.find_all("table")
    participants_table = tables[-1]
    rows = participants_table.tbody.find_all("tr")

    outputs = [["開催地", "URL", "参加人数"]]
    for row in rows:
        # tableの中で非表示の行は処理しない（重複してしまうため）
        if "pera1-ghost" in row.attrs["class"]:
            continue
        place_tag, count_tag = row.find_all("td")
        place, event_url = parse_place(place_tag)
        count = parse_count(count_tag)
        outputs.append([place, event_url, count])

    with open(csv_path, "w", encoding="utf8") as f:
        writer = csv.writer(f)
        writer.writerows(outputs)
