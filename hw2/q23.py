
from q22 import wrapper_p_variance
from encrypter import Vigenere

plainText = """ethicslawanduniversitypolicieswarningtodefendasystemyouneedtobeabletot
hinklikeanattackerandthatincludesunderstandingtechniquesthatcanbeusedt
ocompromisesecurityhoweverusingthosetechniquesintherealworldmayviolate
thelawortheuniversitysrulesanditmaybeunethicalundersomecircumstancesev
enprobingforweaknessesmayresultinseverepenaltiesuptoandincludingexpuls
ioncivilfinesandjailtimeourpolicyincsfortyfourfortyisthatyoumustrespec
ttheprivacyandpropertyrightsofothersatalltimesorelseyouwillfailthecour
seactinglawfullyandethicallyisyourresponsibilitycarefullyreadthecomput
erfraudandabuseactcfaaoneofseveralfederallawsthatbroadlycriminalizesco
mputerintrusioniehackingunderstandwhatthelawprohibitsifindoubtwecanref
eryoutoanattorneypleasereviewtheuniversitysacceptableusepolicyconcerni
ngproperuseofinformationtechnologyaswellasthestudentcodeasmembersofthe"""

keys = ["yz","xyz","wxyz","vwxyz","uvwxyz"]

encrypted_strings = []
for k in keys:
    encrypted_strings.append(Vigenere(plainText,k))

i = 0
for s in encrypted_strings:
    print("{:.4E}".format(wrapper_p_variance(s))) ## Prints the value for 2.3
    i += 1