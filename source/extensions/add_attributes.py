from docutils import nodes
from docutils.nodes import Element
from sphinx.writers.html import HTMLTranslator


class PatchedHTMLTranslator(HTMLTranslator):
    """aタグのリンクを別タブで開くようにパッチを当てたtranslator

    ref: https://stackoverflow.com/a/61669375
    """
    # Copied from Sphinx v4.5.0
    def visit_reference(self, node: Element) -> None:
        atts = {'class': 'reference'}
        if node.get('internal') or 'refuri' not in node:
            atts['class'] += ' internal'
        else:
            atts['class'] += ' external'
            # ----- patched -----
            atts["target"] = "_blank"
            atts["rel"] = "noopener noreferrer"
            # ----- patched end -----
        if 'refuri' in node:
            atts['href'] = node['refuri'] or '#'
            if self.settings.cloak_email_addresses and atts['href'].startswith('mailto:'):
                atts['href'] = self.cloak_mailto(atts['href'])
                self.in_mailto = True
        else:
            assert 'refid' in node, \
                   'References must have "refuri" or "refid" attribute.'
            atts['href'] = '#' + node['refid']
        if not isinstance(node.parent, nodes.TextElement):
            assert len(node) == 1 and isinstance(node[0], nodes.image)
            atts['class'] += ' image-reference'
        if 'reftitle' in node:
            atts['title'] = node['reftitle']
        if 'target' in node:
            atts['target'] = node['target']
        self.body.append(self.starttag(node, 'a', '', **atts))

        if node.get('secnumber'):
            self.body.append(('%s' + self.secnumber_suffix) %
                             '.'.join(map(str, node['secnumber'])))


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
    app.connect("doctree-resolved", doctree_resolved_hook)
