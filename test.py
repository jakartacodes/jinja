from jinja.environment import Environment

e = Environment()

def test_lexer(x):
    for pos, token, data in e.lexer.tokenize(x):
        print '%-8d%-30r%-40r' % (pos, token, data)


def test_parser(x):
    from jinja.parser import Parser
    from jinja.translators.python import translate
    print translate(e, Parser(e, x).parse())