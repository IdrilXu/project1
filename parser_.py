from tokenizer import *


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.tokens = Tokenizer('a b( c ) d( e f( g h( + ) ) i j( k l( + ) m n o( p + q( + ) ) r ) )')

    def parse_S(self):
        while self.tokens:
            self.parse_D(self.tokens)
        else:
            raise Exception('Invalid Syntax')
            #empty with 'space' only？

    def parse_D(self):
        first = next(self.tokens)
        sum = first
        if first == Tokenizer.DOMAIN:
            following = next(first)
            if following == Tokenizer.OPEN:
                sum += following
                self.parse_S(next(self.tokens)) #d(S)
                sum += next(following)
                assert next(self.tokens) == Tokenizer.CLOSE
                sum += Tokenizer.CLOSE
                print(sum)
            elif following == Tokenizer.CLOSE or Tokenizer.PLUS:
                Tokenizer.pushback(following)
            else:
                print(sum)
        elif first == Tokenizer.PLUS:
            print(sum)
        elif first == Tokenizer.OPEN or Tokenizer.CLOSE:
            raise ValueError('Invalid Syntax')
        else:
            Tokenizer.pushback(first)

if __name__ == '__main__':
    parsers = Parser(Tokenizer.tokens)
    print(parsers)
    #tree?
    #input these structure representatives into SVG