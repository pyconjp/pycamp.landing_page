import csv
from collections.abc import Sequence

from docutils.parsers.rst.directives.tables import CSVTable


class EventHistoryCSVTable(CSVTable):
    @staticmethod
    def hyperlink_csv_data(csv_data: Sequence[str]) -> list[str]:
        """
        >>> csv_data = [
        ...   "開催地,URL,参加人数",
        ...   "京都,https://pyconjp.connpass.com/event/33014/,一般参加5人",
        ...   "愛媛,https://pyconjp.connpass.com/event/34564/,一般参加11人、学生1人",
        ... ]
        >>> expected = [
        ...   "開催地,参加人数",
        ...   "`京都 <https://pyconjp.connpass.com/event/33014/>`_,一般参加5人",
        ...   "`愛媛 <https://pyconjp.connpass.com/event/34564/>`_,一般参加11人、学生1人",
        ... ]
        >>> actual = EventHistoryCSVTable.hyperlink_csv_data(csv_data)
        >>> actual == expected
        True
        """
        # TODO: 引数にdialectを追加する余地がありそう
        reader = csv.DictReader(csv_data)
        converted_csv_data = [
            f"`{row['開催地']} <{row['URL']}>`_,{row['参加人数']}" for row in reader
        ]
        header = "開催地,参加人数"
        converted_csv_data.insert(0, header)
        return converted_csv_data

    def parse_csv_data_into_rows(
        self, csv_data: Sequence[str], dialect, source: str
    ) -> tuple[list[str], int]:
        hyperlinked = self.hyperlink_csv_data(csv_data)
        return super().parse_csv_data_into_rows(hyperlinked, dialect, source)


def setup(app):
    app.add_directive("event-history-csv-table", EventHistoryCSVTable)
