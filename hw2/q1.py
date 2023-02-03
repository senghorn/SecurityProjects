cipher = """ELFMASBQDXISZMNMHIBFEFQIMEUVNGLMLRETHAZAQPPDOTEGDEDONLYVZJNWHCKBLPPQWD
QZZGFFUKDWCIXWPZKKSIDYBGBATBUMOWFMYGFBPKYVELFHRHBMDMESJLQMZVHSXMCPDIOW
KJKLOVFGOWCBSIOOPAYVDEZWJYKORVFGOAYVHMMZJGDAEEORWYKQYWUYQOKQEXISZMNMCI
UINFCBZLJGWHKZEQFBPORMCIVDKFOVEISWJYKVOGMCOAXOELFRKGBPPMTDNGWXEPZUNSLJ
PHCMPOYUPRXVKXYZNIIWIAXBZXISXSDPCSPAWFNASSWSDACPPEEWJLRMESJZALDPPCESIS
XLXSOSUGGMOXPXWUUQPXSSAZYZYWBMEFQBSEUHDWNCOITKEXOJFROMYDKQXIEVAOKARSPR
BGBQEFFTKJOWYIPTPZOBSYHGQJSVLXFGKFDPPHVRAKBCRWBMEFQMGISHDMCBZHFOZTOIEW
MSXGGAVMCSSAVLPVFRPZOLFHFQKFFQYGFGPZOUELBHPZOGSEWSPZOECSOULWBAZRBGDWSA
YXNONJSMOEORYSXBASTGETVGASTGAKCBSIBAKMXBZJNCJWIBSIZOOCPWCPPCGAXOLVPIJV
DPPJJFOLDPFKSSWDSHPWUVAQRIGINOZWKUTWUOGWKVOQVGPZKDPXISSJYVRPFPKOCSTVFU
WJNTPWTHDWIJCIBYKFOWQLJGXSDPCSPAPAVMDFFTKJOTPEWWJYDPPHVRAUKTWWBTPWBBSI
NGWQSVREUZASCBTENVKMCMMVPYAFDPPHVRAEOMEWVDSADPSMTPKOVQYKUSWEKBELFZKUKT
LPMSUSXLEEMYOLYBSINOXGEBSMTJEGVMYXFBYGEVEISKWDDMCWPPYZKSCIBQPKGQELBBCW
BIYHWSJYOIYGFCJZSAXMORKXDMYWQSWCSVRSGVEKDQXITSNNOLTRWWALXIXXPFADKBPXPH
DWSADYFGHGGETXUSZLRMZHPFAVYVLPERKFXGVISOXSDAZWPTPWXMYXFFEFQKZRWSNKKBTS
OGDSVNHEZHDJYCRLQWLWCQYFVHEKZZZQQHHQDWWHZCQSBMZYUCBQYCCIMSIWXBMCXOHLOZ
"""


def frequency_analysis(text,space):
    analysis = {}
    characters = [char for char in text];
    for i in range(0,len(text),space):
        c = characters[i]
        if c in analysis:
            analysis[c] = analysis[c] + 1
        else:
            analysis[c] = 1
    return analysis
    
def get_string( text, start,space):
    analysis = ""
    characters = [char for char in text];
    for i in range(start,len(text),space):
        c = characters[i]
        analysis+=c
    return analysis

for i in range(8):
    substring = get_string( cipher.replace('\n',''),i,8)


