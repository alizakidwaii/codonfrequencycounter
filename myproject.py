from collections import Counter

def get_dna():
    dna = input("Enter DNA Sequence: ")
    return dna.replace(" ","").upper()

def check_dna(dna):
    valid = {"A","T","G","C"}
    for base in dna:
        if base not in valid:
            return False
    return True

def make_codons(dna):
   codon_list = []
   for i in range (0,len(dna)- len(dna)%3,3):
           codon = dna[i:i+3]
           codon_list.append(codon)
   return codon_list

def count_codons(codon_list):
    return Counter(codon_list)

def show_result(counts):
    print("\nCodon Frequency Result:")
    for codon, num in sorted(counts.items()):
        print(f"{codon} : {num}")

def main():
    dna = get_dna()

    if not check_dna(dna):
       print("Invaild DNA Sequence! Only A,T,G,C allowed")
       return

    codon_list = make_codons(dna)
    counts = count_codons(codon_list)
    show_result(counts)

if __name__ == "__main__":
    main() 