#! /usr/bin/env python3

class Tokenizer:
    """Tokenizer for dot-parens-plus notation

    The Tokenizer accepts a string upon initialization and splits it into a
    stream of tokens which can be any of '(', ')', '+' or a sequence of non-space,
    non-special characters.

    The next topken in the strweam can be accessed with the next() function.
    The tokenizer also supports pushing back tokens, which are returned upon
    subsequent calls to next() in a last-in-first-out manner.

    Example usage:
    >>> token = Tokenizer("toehold dom1( + )")
    >>> print(next(token))
    'toehold'
    >>> print(next(token))
    'dom1'
    >>> print(next(token))
    '('
    >>> token.pushback('(')
    >>> print(next(token))
    '('
    """
    OPEN = '\('
    CLOSE = '\)'
    PLUS = '\+'
    DOMAIN = f'[^ {OPEN}{CLOSE}{PLUS}]+'
    tokens = '|'.join([OPEN, CLOSE, PLUS, DOMAIN])

    def __init__(self, string):
        import re
        self.queue = []
        self.stream = (match[0] for match in re.finditer(self.tokens, string))

    def __iter__(self):
        return self

    def __next__(self):
        if self.queue:
            return self.queue.pop()
        else:
            return next(self.stream)

    def pushback(self, token):
        self.queue.append(token)



if __name__ == '__main__':
    kernel = "a b( c ) d( e f( g h( + ) ) i j( k l( + ) m n o( p + q( + ) ) r ) )"

    tokens = Tokenizer(kernel)

    print(list(tokens))
