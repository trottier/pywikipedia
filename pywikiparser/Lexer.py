# -*- coding: utf-8  -*-
""" Mediawiki wikitext lexer """
#
# (C) 2007 Merlijn 'valhallasw' van Deen
#
# Distributed under the terms of the MIT license.
#
__version__ = '$Id$'

import re

class Token:
    def __init__(self, name, description):
        self.name = name
        self.__doc__ = description

    def __repr__(self):
        return '<T_%s>' % (self.name,)

class Tokens:
    tokens = [
               ('TEXT',        '      Text data'),
               ('SQRE_OPEN',   '[     Square bracket open'),
               ('SQRE_CLOSE',  ']     Square bracket close'),
               ('PIPE',        '|     Pipe symbol'),
               ('EQUAL_SIGN',  '=     Equal sign'),
               ('APOSTROPHE',  '\'     Apostrophe'),
               ('ASTERISK',    '*     Asterisk'),
               ('COLON',       ':     Colon'),
               ('SEMICOLON',   ';     Semicolon'),
               ('HASH',        '#     Hash symbol'),
               ('CURL_OPEN',   '{     Curly bracket open'),
               ('CURL_CLOSE',  '}     Curly bracket close'),
               ('ANGL_OPEN',   '<     Angular bracket open'),
               ('ANGL_CLOSE',  '>     Angular bracket close'),
               ('NEWPAR',      '\n\n  New paragraph'),
               ('TAB_OPEN',    '{|    Table opening symbol'),
               ('TAB_NEWLINE', '|-    Table new row symbol'),
               ('TAB_CLOSE',   '|}    Table closing symbol'),
               ('WHITESPACE',  '      Whitespace with max 1 newline'),
               ('EOF',         '      End of file')
             ]
    for token in tokens:
        exec("%s = Token(%r,%r)" % (token[0], token[0], token[1]), globals(), locals())

class Lexer:
    """ Lexer class for mediawiki wikitext. Used by the Parser module
    Lexer.lexer() returns a generator that returns (Token, text) pairs. The text represents the actual text data, the token the interpreted data.

    >>> l = Lexer('Test with [[wikilink|description]], {{template|parameter\\'s|{{nested}}=booh}}, \\n\\n new paragraphs, <html>, {| tables |- |}')
    >>> gen = l.lexer()
    >>> gen.next()
    (<T_TEXT>, 'Test')
    >>> gen.next()
    (<T_WHITESPACE>, ' ')
    >>> [token for token in gen][:10]
    [(<T_TEXT>, 'with'), (<T_WHITESPACE>, ' '), (<T_SQRE_OPEN>, '['), (<T_SQRE_OPEN>, '['), (<T_TEXT>, 'wikilink'), (<T_PIPE>, None), (<T_TEXT>, 'description'), (<T_SQRE_CLOSE>, ']'), (<T_SQRE_CLOSE>, ']'), (<T_TEXT>, ',')]
    """

    def __init__(self, string):
        self.data = (a for a in string)

    def lexer(self):
        text = ''
        try:
            c = self.getchar()
            while True:
                if (c in ('[', ']', '}', '<', '>', '=', '\'', '*', ':', ';', '#')):
                    if text:
                        yield (Tokens.TEXT, text)
                        text = ''

                    if   (c == '['): yield (Tokens.SQRE_OPEN,  c)
                    elif (c == ']'): yield (Tokens.SQRE_CLOSE, c)
                    elif (c == '}'): yield (Tokens.CURL_CLOSE, c)
                    elif (c == '<'): yield (Tokens.ANGL_OPEN,  c)
                    elif (c == '>'): yield (Tokens.ANGL_CLOSE, c)
                    elif (c == '='): yield (Tokens.EQUAL_SIGN, c)
                    elif (c == '\''): yield(Tokens.APOSTROPHE, c)
                    elif (c == '*'): yield (Tokens.ASTERISK,   c)
                    elif (c == ':'): yield (Tokens.COLON,      c)
                    elif (c == ';'): yield (Tokens.SEMICOLON,  c)
                    elif (c == '#'): yield (Tokens.HASH,       c)
                    c = self.getchar()
                elif (c == '{'):
                    if text:
                        yield (Tokens.TEXT, text)
                        text = ''
                    t = self.getchar()
                    if (t == '|'):
                        yield (Tokens.TAB_OPEN, '{|')
                        c = self.getchar()
                    else:
                        yield (Tokens.CURL_OPEN, '{')

                    c = t
                elif (c == '|'):
                    if text:
                        yield (Tokens.TEXT, text)
                        text = ''
                    t = self.getchar()

                    if (t == '-'):
                        yield (Tokens.TAB_NEWLINE, '|-')
                        c = self.getchar()
                    elif (t == '}'):
                        yield (Tokens.TAB_CLOSE, '|}')
                        c = self.getchar()
                    else:
                        yield (Tokens.PIPE, None)
                        c = t
                elif re.match('\s', c): # whitespace eater pro (TM)
                    if text:
                        yield (Tokens.TEXT, text)
                        text = ''
                    ws = ''
                    try:
                        while re.match('\s', c):
                            ws += c
                            c = self.getchar()   #eat up remaining whitespace
                    finally:
                        if (ws.count('\n') > 1):
                            yield (Tokens.NEWPAR, ws)
                        else:
                            yield (Tokens.WHITESPACE, ws)
                else:
                    text = text + c
                    c = self.getchar()
        except StopIteration: pass
        if text:
            yield (Tokens.TEXT, text)
        yield (Tokens.EOF, None)

    def getchar(self):
        return self.data.next()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
