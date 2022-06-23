import re
import time

# new replacement method using re.sub()
def replace_phrases(substitutions):
    start = time.time()

    # replace any occurance of 'R123' or 'r123'
    substitutions = re.sub(r'(?i:R123)', 'the combination of resistor 1, resistor 2, and resistor 3', substitutions)

    # replace any occurance of 'VR1' 'Vr1' or 'vr1'
    substitutions = re.sub(r'(?i:VR1)', 'voltage drop across resistor 1', substitutions)

    # replace any occurance of 'VR2' 'Vr2' or 'vr2'
    substitutions = re.sub(r'(?i:VR2)', 'voltage drop across resistor 2', substitutions)

    # replace any occurance of 'VR3' 'Vr3' or 'vr3'
    substitutions = re.sub(r'(?i:VR3)', 'voltage drop across resistor 3', substitutions)

    # replace any occurance of 'IR1' 'Ir1' or 'ir1'
    substitutions = re.sub(r'(?i:IR1)', 'the current in resistor 1', substitutions)

    # replace any occurance of 'IR2' 'Ir2' or 'ir2'
    substitutions = re.sub(r'(?i:IR2)', 'the current in resistor 2', substitutions)

    # replace any occurance of 'IR3' 'Ir3' or 'ir3'
    substitutions = re.sub(r'(?i:IR3)', 'the current in resistor 3', substitutions)

    # replace any occurance of 'R2||R3' 'r2||r3' 'r2||3' or 'R2||3'
    substitutions = re.sub(r'((?i:R2\|\|R3)|(?i:R2\|\|3))', 'resistor 2 in parallel with resistor 3', substitutions)

    # replace any occurance of 'R1+R2' or 'r1+r2'
    substitutions = re.sub(r'(?i:R1\+R2)', 'resistor 1 and resistor 2', substitutions)

    # replace any occurance of 'R2+R3' or 'r2+r3'
    substitutions = re.sub(r'(?i:R2\+R3)', 'resistor 2 and resistor 3', substitutions) 

    # replace any occurance of 'R23' or 'r23'
    substitutions = re.sub(r'(?i:R23)', 'the combination of resistor 2 and resistor 3', substitutions)
   
    # replace any occurance of 'R1' or 'r1'
    substitutions = re.sub(r'(?i:R1)', 'resistor 1', substitutions)

    # replace any occurance of 'R2' or 'r2'
    substitutions = re.sub(r'(?i:R2)', 'resistor 2', substitutions)

    # replace any occurance of 'R3' or 'r3'
    substitutions = re.sub(r'(?i:R3)', 'resistor 3', substitutions)

    # replace any occurance of 'REQ' 'Req' 'rEQ' or 'req'
    substitutions = re.sub(r'(?i:REQ)', 'the equivalent resistance', substitutions)

    # replace any occurance of 'RTOT' 'rtot' 'rTOT' or 'Rtot'
    substitutions = re.sub(r'(?i:RTOT)', 'the total resistance', substitutions)

    # replace any occurance of 'REFF' 'Reff' 'rEFF' or 'reff'
    substitutions = re.sub(r'(?i:REFF)', 'the effective resistance', substitutions)

    # replace any occurance of 'v-drop' or 'V-drop'
    substitutions = re.sub(r'((?i:v-drop)|(?i:vdrop))', 'voltage drop', substitutions)

    # replace any occurance of 'v-drop' or 'V-drop'
    substitutions = re.sub(r'(?i:VS)', 'voltage source', substitutions)

    # replace any occurance of 'G2' or 'g2'
    substitutions = re.sub(r'(?i:G2)', 'the conductance of resistor 2', substitutions)

    # replace any occurance of 'G3' or 'g3'
    substitutions = re.sub(r'(?i:G3)', 'the conductance of resistor 3', substitutions)

    # replace any occurance of 'P1' or 'p1'
    substitutions = re.sub(r'(?i:P1)', 'the power associated with resistor 1', substitutions)

    # replace any occurance of 'P2' or 'P2'
    substitutions = re.sub(r'(?i:P2)', 'the power associated with resistor 2', substitutions)

    # replace any occurance of 'P3' or 'p3'
    substitutions = re.sub(r'(?i:P3)', 'the power associated with resistor 3', substitutions)

    # replace any occurance of 'KVL' or 'kvl'
    substitutions = re.sub(r'(?i:KVL)', 'Kirchhoff\'s voltage law', substitutions)

    # replace any occurance of 'KCL' or 'kcl'
    substitutions = re.sub(r'(?i:KCL)', 'Kirchhoff\'s current law', substitutions)

    # replace any occurance of 'node x'
    substitutions = re.sub(r'(?i:node x)', 'the node connecting resistor 1, resistor 2, and resistor 3', substitutions)

    # replace any occurance of 'V=IR'
    substitutions = re.sub(r'(?i:V=IR)', 'voltage equals current times resistance', substitutions)

    # replace any occurance of '(I=V/R)'
    substitutions = re.sub(r'(?i:I=V/R)', 'current equals voltage divided by resistance', substitutions)

    # replace any occurance of '(P=VI)'
    substitutions = re.sub(r'(?i:P=VI)', 'power equals voltage times current', substitutions)

    # replace any occurance of 'P=IV'
    substitutions = re.sub(r'(?i:P=IV)', 'power equals current times voltage', substitutions)

    # replace any occurance of 'P=I2R'
    substitutions = re.sub(r'(?i:P=I2R)', 'power equals current squared times resistance', substitutions)

    # replace any occurance of 'P=V2/R'
    substitutions = re.sub(r'(?i:P=V2/R)', 'power equals voltage squared divided by resistance', substitutions)

    # replace any occurance of '=' (accounts for inclusion/exclusion of whitespaces)
    substitutions = re.sub(r'\s?(=)\s?', ' equals ', substitutions)
    
    # replace any occurance of 'w/'
    substitutions = re.sub(r'(?i:w/)', 'with', substitutions)

    # replace any occurance of 'A' 'Amps' or 'amps'
    substitutions = re.sub(r'(\bA\b|(?i:Amps))', 'amperage', substitutions)

    # This next one could be problematic if someone said '5 V' for example.
    #Replace 'v' and 'V' when they occur as their own word (Catches begin and end of sentence as well)
    substitutions = re.sub(r'\b[Vv]\b', 'voltage', substitutions)

    # Replace 'r' and 'R' when they occur as their own word (Catches begin and end of sentence as well)
    substitutions = re.sub(r'\b[Rr]\b', 'resistance', substitutions)

    #Replace 'p' and 'P' when they occur as their own word (Catches begin and end of sentence as well)
    substitutions = re.sub(r'\b[Pp]\b', 'power', substitutions)

    #Replace 'w' and 'W' when they occur as their own word (Catches begin and end of sentence as well)
    substitutions = re.sub(r'\b[Ww]\b', 'watt', substitutions)

    end = time.time()
    print("New time:",end-start)

    return substitutions


if __name__ == '__main__':
    str1 = "1: Replace 'r' and 'R' when they occur as their own word (Catches begin and end of sentence as well). \n2: replace any occurance of 'R123' or 'r123'. replace any occurance of 'VR1' 'Vr1' or 'vr1'. \n3: replace any occurance of 'VR2' 'Vr2' or 'vr2'. \n4: replace any occurance of 'VR3' 'Vr3' or 'vr3'. replace any occurance of 'IR1' 'Ir1' or 'ir1'. \n5: replace any occurance of 'IR2' 'Ir2' or 'ir2'. \n6: replace any occurance of 'IR3' 'Ir3' or 'ir3'. \n7: replace any occurance of 'R2||R3' 'r2||r3' 'r2||3' or 'R2||3'. \n8: replace any occurance of 'R1+R2' or 'r1+r2'. \n9: replace any occurance of 'R2+R3' or 'r2+r3'. \n10: replace any occurance of 'R23' or 'r23'. \n11: replace any occurance of 'R1' or 'r1'. \n12: replace any occurance of 'R2' or 'r2'. \n13: replace any occurance of 'R3' or 'r3'. \n14: replace any occurance of 'REQ' 'Req' 'rEQ' or 'req'. \n15: replace any occurance of 'RTOT' 'rtot' 'rTOT' or 'Rtot'. \n16: replace any occurance of 'REFF' 'Reff' 'rEFF' or 'reff'. \n17: replace any occurance of 'v-drop' or 'V-drop'. \n18: Replace 'v' and 'V' when they occur as their own word (Catches begin and end of sentence as well). \n19: replace any occurance of 'v-drop' or 'V-drop'. \n20: replace any occurance of 'G2' or 'g2'. \n21: replace any occurance of 'G3' or 'g3'. \n22: replace any occurance of 'P1' or 'p1'. \n23: replace any occurance of 'P2' or 'P2'. \n24: replace any occurance of 'P3' or 'p3'. \n25: replace any occurance of 'KVL' or 'kvl'. \n26: replace any occurance of 'KCL' or 'kcl'. \n27: replace any occurance of 'node x'. \n28: Replace 'p' and 'P' when they occur as their own word (Catches begin and end of sentence as well). \n29: #Replace 'w' and 'W' when they occur as their own word (Catches begin and end of sentence as well). \n30: replace any occurance of '=' (accounts for inclusion/exclusion of whitespaces). \n31: replace any occurance of 'V=IR'. \n32: replace any occurance of 'I=V/R'. \n33: replace any occurance of 'w/'. \n34: replace any occurance of 'A' 'Amps' or 'amps'."

    print(replace_phrases(str1))