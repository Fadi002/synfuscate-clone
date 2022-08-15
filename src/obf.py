import os, marshal, base64, random, string, zlib
from src.codes import *
def strings(length=10):
        return "".join(random.choice(string.ascii_letters) for i in range(length))
def mar(code):
    code = compile(code,'','exec')
    code = marshal.dumps(code)
    return code
def encoder1(code,rounds=1):
    zlb = lambda in_: zlib.compress(in_)
    b64 = lambda in_: base64.b64encode(in_)
    mar = lambda in_: marshal.dumps(compile(in_,'<x>','exec'))
    for x in range(rounds):method = repr(b64(zlb(mar(code.encode('utf8'))))[::-1]);code = f"exec(__import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(%s[::-1]))))" % method
    z = []
    for i in code:z.append(ord(i))
    sata = "_ = %s\nexec(''.join(chr(SYN) for SYN in _))" % z
    return sata
def anti_decode(anti_decode):
    code = ANTI_DECODE(anti_decode).get_antidecode()
    code = encoder1(code)
    code = mar(code)
    code = base64.b64encode(code)
    code = """exec(marshal.loads(base64.b64decode({})))""".format(code)
    return code
def obf(code,anti_debug=False):
    code = f'''{ANTI_DEBUG(anti_debug).get_antidebug()}
{code}'''
    code = encoder1(code,rounds=3)
    code = mar(code)
    code = base64.b64encode(code)
    code = '''try:
 exec(marshal.loads(base64.b64decode(str(b'{}').split("b'")[1].split("'")[0])))
except:pass\n'''.format(code.decode())
    return code
def junker():
    junk = strings(length=400)
    junk = f'''{junk}'''
    junk = encoder1(junk)
    junk = mar(junk)
    junk = base64.b64encode(junk)
    junk = '''try:
 exec(marshal.loads(base64.b64decode(str(b'{}').split("b'")[1].split("'")[0])))
except:pass\n'''.format(junk.decode())
    return junk


def obff(code,antid=False,antide=False):
    code = obf(code,anti_debug=antid)
    nice = f'''import marshal,base64
{anti_decode(antide)}
{junker()}
{code}
{junker()}'''
    return nice
