# codonfrequencycounter
This my first Git Repository 
<br>
Project title - Codon Frequency Counter

Overview of the project 

This Python project takes a DNA sequence from the user and finds how often each codon (a group of three DNA letters) appears.  
It checks if the sequence only has valid DNA bases (A, T, G, and C), cleans it up, and then shows how many times each codon occurs.  

Problem Definition

DNA sequences are made up of four letters: A, T, G, and C. These letters combine in groups of three, called codons, which are important in genetic studies. 
Analyzing codons by hand takes a lot of time and can lead to mistakes.  
This project makes that task faster and easier by:
- Taking a DNA sequence from the user  
- Checking if it’s valid (only A, T, G, C allowed)  
- Breaking it into codons (groups of three letters)  
- Counting how many times each codon appears  
- Showing the results neatly on the screen  

Requirement Analysis

1.Functional Requirements

DNA Input & Validation
The user types or pastes a DNA sequence.
The program removes spaces and changes all letters to uppercase.
It checks if the sequence has only A, T, G, and C.
If there are any invalid characters, it shows an error message and stops.

Codon Extraction
The program divides the DNA sequence into groups of three letters, called codons.
If the sequence length is not a multiple of three, the last few leftover letters are ignored.
All codons are stored in a list for later use.

Codon Frequency Analysis & Output
The program counts how many times each codon appears using a counter.
The results are sorted alphabetically.
It prints each codon followed by its count (for example, ATG : 5).
Input Format:The user provides a text input: a DNA sequence made of the letters A, T, G, and C.
Output Format:The program prints a table showing each codon and how many times it occurs.


2.Non-Functional Requirements

Performance: 
The program should work quickly even with very long DNA sequences (100,000+ letters).
Codon counting should finish in linear time (O(n)).

Usability:
The program should clearly explain how to enter input.
Error messages should be simple and helpful.

Reliability:
The program must always check for invalid input before processing.
It should not crash when unexpected characters appear.

Maintainability:
The code should be written in separate, reusable functions.
It should be easy to add new features in the future, such as converting codons into amino acids.

 

3.Software Requirements
- Python 3.x
- Counter from the collections module (built-in)


Main Features

- Takes DNA sequence as input from the user.  
- Removes spaces and changes all letters to uppercase.  
- Checks if the sequence only has A, T, G, and C.  
- Splits the DNA into codons (each group of 3 letters).  
- Counts how many times each codon appears.  
- Shows codons neatly in sorted order.  
- Uses simple, easy-to-read Python code.  

Top-Down Design (Modular Design)

The program is broken into simple, reusable functions:
Function --Purpose 
get_dna() -- Gets DNA sequence from the user 
check_dna(dna) -- Checks if the sequence is valid 
make_codons(dna) -- Splits the DNA into 3-letter codons 
count_codons(codon_list) -- Counts how often each codon appears 
show_result(counts) -- Displays codon counts 
main() -- Runs the whole program 

Program Flow

Main Program  
get_dna()  
check_dna()  
make_codons()  
count_codons()  
show_result()  


Algorithm

Step 1: Start  
Step 2: Ask the user for a DNA sequence  
Step 3: Remove spaces and change to uppercase  
Step 4: Check if it only has A, T, G, C  
 -  If not → show error → stop  
Step 5: Split the DNA into 3-letter codons  
Step 6: Count how many times each codon appears  
Step 7: Show the codons and their counts alphabetically  
Step 8: End  


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

 <img width="693" height="827" alt="Screenshot 2025-11-23 150735" src="https://github.com/user-attachments/assets/951182c6-1c0f-4390-8e0c-b8b3a8ca6239" />
 <img width="790" height="359" alt="Screenshot 2025-11-23 150811" src="https://github.com/user-attachments/assets/0b4840ad-7a16-41c4-aa81-140f288ead5b" />

 OUTPUTS----

 <img width="391" height="158" alt="Screenshot 2025-11-23 154524" src="https://github.com/user-attachments/assets/fddf9738-2c7e-4632-b745-af696fdffc0b" />

 <img width="439" height="183" alt="Screenshot 2025-11-23 154633" src="https://github.com/user-attachments/assets/94324fda-c2cd-44c6-8e86-3eb248f75e35" />

 <img width="556" height="51" alt="Screenshot 2025-11-23 155142" src="https://github.com/user-attachments/assets/25141d67-669f-4167-a124-bebb75efd644" />

Objectives
Main Goals
Make the computer automatically count how often each codon appears in a DNA sequence.
Check that the DNA sequence entered by the user is valid and contains only real DNA letters.
Show the codon counts in a clear and neatly formatted way.
Use a modular design (dividing the program into clear parts) to follow good programming practices.

Extra Goals
Add error handling so the program can warn users if the DNA has invalid letters.
Show how bioinformatics calculations can be done simply using Python.
Write proper documentation with explanations, diagrams, and system design for academic use.


