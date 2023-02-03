from q1 import frequency_analysis
from population_variance import p_variance

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

def divide_frequency(frequency, divisor):
    for s in frequency:
        frequency[s] = frequency[s]*1.0 / divisor
    
    
def wrapper_p_variance(plain):    
    plain = plain.replace('\n', '') ## Removes unnecessary new lines
    length = len(plain)
    freq = frequency_analysis(plain,1)
    divide_frequency(freq,length)
    chars = freq.keys()
    return p_variance(freq,chars)

# print(wrapper_p_variance(plainText)) ## Prints value of 2.2