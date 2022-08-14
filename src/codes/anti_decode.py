import random, string
def random_string(length=10):
        return "".join(random.choice(string.ascii_letters) for i in range(length))
class ANTI_DECODE:
    def __init__(self,anti_debug=False):
        self.anti_debug = anti_debug
    def get_antidecode(self):
        code = """anti_decode = 'xd'
if anti_decode:\n
    lol1 = open(f'''{__import__('sys').argv[0]}''', 'r')
    lol2 = lol1.read()
    if 'print' in lol2:
        __import__('sys').exit()
    elif 'with open' in lol2:
        __import__('sys').exit()
    elif 'open' in lol2:
        __import__('sys').exit()""".replace("lol1",random_string(random.randint(6,10))).replace('lol2',random_string(random.randint(6,10)))
        if self.anti_debug:
            code = code.replace("'xd'",'True') 
        return code