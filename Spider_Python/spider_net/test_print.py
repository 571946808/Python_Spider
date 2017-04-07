# -*- coding: UTF-8 -*-
#!/usr/bin/env python2.7

import html_outputer
class Print(object):
    def output_html(self, key, location, rule, school):
        print key,location,rule,school


if __name__ == "__main__":
    Print().output_html('北京上海', '', '', '')