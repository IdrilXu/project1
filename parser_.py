from tokenizer import *
import re

class Parser:
    def __init__(self, tokens):
        # self.tokens = tokens
        self.tokens = Tokenizer(tokens)

    def parse_S(self, domains):
        while self.tokens:  # while True
            first = next(self.tokens)
            if re.match(Tokenizer.CLOSE, first):# d(S) loop ends with )
                break
            else:
                self.tokens.pushback(first)
            self.parse_D(domains)
        else:
            raise Exception('Invalid Syntax')


    def parse_D(self, domains: list):
        first = next(self.tokens)
        if re.match(Tokenizer.DOMAIN, first):
            following = next(self.tokens)
            if re.match(Tokenizer.OPEN, following):
                inner_sequence = []
                self.parse_S(inner_sequence)
                domains.append(inner_sequence)

            # elif re.match(Tokenizer.OPEN, following) or re.match(Tokenizer.PLUS, following):
            #     self.token.pushback(following)
            else:
                self.tokens.pushback(following)
                domains.append(f'single domain {first}')

        elif re.match(Tokenizer.PLUS, first):
            domains.append(f'strand break')

        elif re.match(Tokenizer.CLOSE, first):
            pass

        elif re.match(Tokenizer.OPEN, first) or re.match(Tokenizer.CLOSE, first):
            raise ValueError('Invalid Syntax')
        else:
            Tokenizer.pushback(first)

if __name__ == '__main__':
    tokens = 'a b( c ) d( e f( g h( + ) ) i j( k l( + ) m n o( p + q( + ) ) r ) )'
    parsers = Parser(tokens)
    parsers.parse_S()
    print(list(parsers.tokens))
    #tree?
    #input these structure representatives into SVG