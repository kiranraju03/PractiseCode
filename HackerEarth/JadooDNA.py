"""
Jadoo and DNA Transcription
Convert DNA into RNA using the input characters given

"""

r_dna = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
inp = "GGCTAACC"

if any(each_dna not in r_dna.keys() for each_dna in inp):
    print('Invalid Input')
else:
    print(''.join(r_dna[each_dna] for each_dna in inp))
