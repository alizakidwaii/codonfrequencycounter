# codonfrequencycounter
This my first Git Repository 
<br>
Project title - Codon Frequency Counter

Overview of the project 

This Python project takes a DNA sequence from the user and finds how often each codon (a group of three DNA letters) appears.  
It checks if the sequence only has valid DNA bases (A, T, G, and C), cleans it up, and then shows how many times each codon occurs.  


 Main Features

- Takes DNA sequence as input from the user.  
- Removes spaces and changes all letters to uppercase.  
- Checks if the sequence only has A, T, G, and C.  
- Splits the DNA into codons (each group of 3 letters).  
- Counts how many times each codon appears.  
- Shows codons neatly in sorted order.  
- Uses simple, easy-to-read Python code.  



Tools and Technologies

- Python 3  
- collections.Counter  
- Basic Python functions and loops  
- Runs in the terminal (command line)  

 How to Run the Program

1. Download the project:
   bash
   git clone https://github.com/your-alizakidwaii/codon-frequency-counter.git
   

2. Open the project folder:
   bash
   cd codon-frequency-counter
   

3. Run the program:
   bash
   python myproject.py


Try It Out

Example 1: Valid DNA

Input:  

ATGCGATTTGGA


Output:  

Codon Frequency Result:
ATG : 1
CGA : 1
TTT : 1
GGA : 1


Example 2: DNA with Spaces

Input:  

ATG CGA TTT GGA

The program will automatically remove spaces.  


Example 3: Invalid DNA

Input:  

ATGXB12


Output:  

Invalid DNA Sequence! Only A, T, G, C allowed


 Screenshots 




