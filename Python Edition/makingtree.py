case1 = ["pascal", "program", "programmer", "task", "tree",
 "treacherous", "treachery", "tread", "trace"]

case2 = ["f"]
case3 = ["f", "pi"]
case4 = ["f", "pie"]
case5 = ["fy", "piex"]
case6 = ["pascal", "programmer", "task", "tree",
 "treacherous", "treachery", "tread", "trace"]
case7 = ["academic","base","board","cola","code","cute","hack"]
case8 = ["lxxatbwhoh tooj lgwlu xiub lgwdinr rjjmufijoom",
 "vfdx toskry xhttofxo rkgqmb xiyyvyo qwbcpjcz",
 "lgquy ruyyptjv vazlfwy ruyypguoofimw qwbaarpfkukk",
 "xinhekafyi laehdkt lxxyerjt torxi lxxatijcg rkys",
 "xpktuvhcxhbg xiyyddlmf vazlfkxp xhf qwbaivq",
 "tookxlfs xiyydvil lxxatbng qwgzkvt rjlmcuwdug",
 "tdjlbbsr lxtoivq lwevhyms vfdo tfci lwevhyxmmm",
 "xpun qexfaistucs xinhgfyv qexxjfg xvljvc",
 "qwgzgina ruyqzuxbyovm ladihus rjjmufie",
 "qwgzgif xhnqem lwevhner xpuedqzd lpmedevkt",
 "vzefddtid lpmeji tfcypcvkqa tdjlbbcrm rjltci",
 "xhttofxfb xvljve xliwbcyxwg tookxf xhnqnw lgqvnh",
 "qwbqiu tdjlbbcz laehdycq lgqul qwbcpr lwevhyxi",
 "xpktuvhyc tdly rntxz xpanwsck laehdycz",
 "qwgzkva ruyypguj ruyqvsz rntg xibyr qwc xhnss",
 "xltrqddu vzcsdu qwbaijk lwevhymb xinhgfyo qwgzgf",
 "xhnqnggu toskrtau rjlmcums toskwaks xiyydvgx",
 "xiut qwbaartdb qexo rjlquefm xinl rjjifftthu",
 "rkyb lpmvbfn tfcpmbo rjlmczay rpt xltennu",
 "lgwdirzi lpmtvbija xpanwscbh tfur xhnqngrnhci",
 "xltrqbwdbl xlbwe rkghbk qwgzkk tdjw tdjry xvlfztz",
 "qwbaarpuyyse toswj xhttozvtv qwgc lxy toskrtawp",
 "rkgqx lgwdings xinhgfx lxtjtipnoy tfcpmbawxv",
 "vazlfwlo lpmvbxcct tfcpo lgqvnq lgkxgg rjlmczrm",
 "xpke rnte vajnf tfuwqdp qom xinhgcmsbmi tookxlfu",
 "xibyd xpatx lwevhnbn ladihuxw xpuep lxxaq vui",
 "lgkwbgs xvv tfuariim vazb xhva xinjovn xltrqdnqwy",
 "rjlmil xinhgcmk vzyvo lgwdplzpcon xiyydvgge ladp",
 "tdjlbudh lxxb lxxyerjynyx qwf xliwgsno lxtjetr",
 "xhttoftrvcabo xiyyddlqf xinheijxf rkghbn tfcype",
 "vfk xvayc xvlfzti laey rjltgh lgkmp rql vltqmow",
 "vzcsm qwbaivjn lpmvbxcwj qexxjfh lxtoivjrd",
 "lxxydxb xltl toskway xuyf tdlu tfuwhkp lxxatbwp",
 "lgkxgt qexfaiku xpktgyllgg vaq xlbiv lpmtvbikk",
 "lpmtvbgfo xiyphm tfcpmbau ruyd xlbil rkykcbf",
 "xpktgiusyzg lwevhnesh tdjrfy xhnsqe vzcq lgkmk",
 "lgwdirzsec vzefddtdbx lxtoii rjlmczau torak",
 "lpmtvbgoavjeq lxtjtipmhy xltrqddg vltqmytw",
 "rlxnh laehr xhtfmxvjn vltqmycl lgkwe qwbaijhx",
 "rjlmczro rkiaj xpktgia lwevuwow ruyqvsln lxtjtihl",
 "tdssjxz xiyydvie qwbaartk torax xlbwa xinheiha",
 "xvsmy vzcsds ruyqzuykr toskwakl tdjrfg vflz lxta",
 "xhnqnggj lxtoivjw tfuwhr lxtjetdp qexxjtg",
 "rnm xiue xpj vazlfwlfdg xhttozqr rkykcbo",
 "qwbcpjcmv tfuardg qwgzginklo tdssjd tfuardti lxl",
 "rlxb xhttye lwevuwl lgwiw rkykcmhltv qwgbsrgo",
 "tfuwqdgbh ruyqzxw lwemx xiypf xltrqbwm",
 "lpmedevcfkt"]
case8_1 = []

for l in case8:
    for w in l.split(' '):
        case8_1.append(w)

wordlist = case7

class node:
    def __init__(self, letter):
        self.letter = letter
        self.children = []
    
    def display(self, level = 0):
        print(' '* level + self.letter)
        for c in self.children:
            c.display(level + 1)

class nodestate:
    def __init__(self, win, depth, str):
        self.win = win
        self.depth = depth
        self.str = str
        print(f'{win},{depth},{str}')

"""node1 = node('f')
node2 = node1.children.append(node('i'))

node1.display()"""

tree = node('*')

def maketree(parent, str):
    if len(str) == 0:
        return
    result = [ item for item in parent.children if item.letter == str[0]]
    if len(result) == 0:
        newNode = node(str[0])
        parent.children.append(newNode)
        maketree(newNode,str[1:])
    else: 
        maketree(result[0],str[1:])

wordlist.sort()    
for word in wordlist:
    if wordlist.index(word) == 0:
        maketree(tree,word)
    else:
        repeatwords = 0
        for prevwords in wordlist[:wordlist.index(word)]:
            if word.startswith(prevwords):
                repeatwords += 1
                break
        if repeatwords == 0:
            maketree(tree,word)

def winstate(selectednode, IsJoe = False):
    if len(selectednode.children) == 0:
        return nodestate(not IsJoe, 0, selectednode.letter)
    else:
        if not IsJoe:
            states = [ winstate(item, not IsJoe) for item in selectednode.children]
            losingStates = [ item for item in states if item.win]
            if len(losingStates):
                losingState = sorted(losingStates, key=lambda item: item.depth, reverse=False)[0]
                return nodestate(True, losingState.depth +1, selectednode.letter + losingState.str )
            else:
                winningStates = [ item for item in states if not item.win]
                winS = sorted(winningStates, key=lambda item: item.depth, reverse=True)[0]
                return nodestate(False, winS.depth + 1, selectednode.letter + winS.str)
        else:
            states = [ winstate(item, not IsJoe) for item in selectednode.children]
            losingStates = [ item for item in states if not item.win]
            if len(losingStates):
                losingState = sorted(losingStates, key=lambda item: item.depth, reverse=False)[0]
                return nodestate(False, losingState.depth + 1, selectednode.letter + losingState.str )
            else:
                winningStates = [ item for item in states if item.win]
                winS = sorted(winningStates, key=lambda item: item.depth, reverse=True)[0]
                return nodestate(True, winS.depth + 1, selectednode.letter + winS.str)

tree.display()

print(winstate(tree).str)