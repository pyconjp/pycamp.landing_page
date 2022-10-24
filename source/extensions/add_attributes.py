from docutils import nodes
from docutils.nodes import Element
from sphinx.writers.html import HTMLTranslator


class PatchedHTMLTranslator(HTMLTranslator):
    """aタグのリンクを別タブで開くようにパッチを当てたtranslator

    ref: https://stackoverflow.com/a/67153583
    """

    def starttag(self, node, tagname, *args, **atts):
        if (
            tagname == "a"
            and "target" not in atts
            and (
                "external" in atts.get("class", "")
                or "external" in atts.get("classes", [])
            )
        ):
            atts["target"] = "_blank"
            atts["rel"] = "noopener noreferrer"
        return super().starttag(node, tagname, *args, **atts)


def centering_header_elements_text(doctree):
    """h1とh2の要素を中央揃えにする"""
    for item1 in doctree:
        if not isinstance(item1, nodes.section):
            continue
        for item2 in item1:
            if isinstance(item2, nodes.title):
                item2.attributes["classes"].append("sd-text-center")
            if isinstance(item2, nodes.section):
                for item3 in item2:
                    if isinstance(item3, nodes.title):
                        item3.attributes["classes"].append("sd-text-center")


def doctree_resolved_hook(app, doctree, docname):
    centering_header_elements_text(doctree)


def setup(app):
    app.set_translator("html", PatchedHTMLTranslator)
    app.set_translator("singlehtml", PatchedHTMLTranslator)
    app.connect("doctree-resolved", doctree_resolved_hook)
