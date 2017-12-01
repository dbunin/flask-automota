from app.parse import Lexer, Parser, Token, State, NFA, Handler

class NFA_Parser:
    def compile(self, p):
        """Turns an input regex string into an NFA machine."""
        lexer = Lexer(p)
        parser = Parser(lexer)
        tokens = parser.parse()
        handler = Handler()
        nfa_stack = []
        for t in tokens:
            handler.handlers[t.name](t, nfa_stack)
        assert len(nfa_stack) == 1 # check there is only one final NFA on the stack
        return nfa_stack.pop() 
