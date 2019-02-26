#!/usr/bin/env python3

#------------------------------------------------
# Title: html_render.py (homework from lesson 7)
# Changelog:
# 2019-02-25,Aaron Devey,Created
#------------------------------------------------


"""
A class-based system for rendering html.
"""

from io import StringIO

# This is the framework for the base class
class Element(object):
    contents = []
    indent = 0
    indent_width = 4
    tag_name = "html"
    tag_attrs = {}
    render_format = "{}\n{}{}\n"
    open_format = "<{}{}>"
    close_format = "</{}>"


    def __init__(self, content="", **kwargs):
        self.contents = []
        self.contents.append(content)
        self.tag_attrs = kwargs

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file, current_indent = 0):
        out_file.write(self.prerender(current_indent))

    def render_indent(self, depth):
        return " " * (depth * self.indent_width)

    def close_tag(self):
        return self.close_format.format(self.tag_name)

    def open_tag(self):
        props = ""
        for key, val in self.tag_attrs.items():
            props += " {}=\"{}\"".format(key, val)
        return self.open_format.format(self.tag_name, props)

    def prerender(self, current_indent = 0):
        self.indent = current_indent
        output = ""
        for content in self.contents:
            if type(content) == str:
                output += self.render_indent(self.indent + 1) + content + "\n"
            else:
                output += content.prerender(self.indent + 1)
        return self.render_format.format(self.render_indent(self.indent) + self.open_tag(), output, self.render_indent(self.indent) + self.close_tag())

    def __str__(self):
        return self.prerender()


class Html(Element):
    tag_name = "html"
    open_format = "<!DOCTYPE html>\n<{}{}>"

class Body(Element):
    tag_name = "body"

class P(Element):
    tag_name = "p"

class Head(Element):
    tag_name = "head"

class OneLineTag(Element):
    render_format = "{}{}{}\n"
    def prerender(self, current_indent = 0):
        self.indent = current_indent
        output = ""
        return self.render_format.format(self.render_indent(self.indent) + self.open_tag(), " ".join(self.contents), self.close_tag())

class Title(OneLineTag):
    tag_name = "title"

class SelfClosingTag(Element):
    render_format = "{}\n"
    open_format = "<{}{} />"
    def append(self, content):
        raise TypeError("Cannot add content to self closing tag type")

    def __init__(self, **kwargs):
        self.tag_attrs = kwargs

class Hr(SelfClosingTag):
    tag_name = "hr"

class A(OneLineTag):
    tag_name = "a"
    def __init__(self, link, content):
        self.tag_attrs = {'href': str(link)}
        super().__init__(content)

class Ul(Element):
    tag_name = "ul"

class Li(Element):
    tag_name = "li"

class H(OneLineTag):
    tag_name = "h"
    def __init__(self, size, content):
        self.tag_name += str(size)
        super().__init__(content)

class Meta(SelfClosingTag):
    tag_name = "meta"

