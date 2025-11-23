1. Problem Statement 

DNA is made of four building blocks: A, T, G, and C. 
Scientists often study how often different three-letter groups (called codons) appear in a DNA sequence to understand genes and how proteins are made.
Counting these codons by hand can be slow and confusing, especially for long DNA sequences.
This project creates a simple Codon Frequency Counter program. It checks if a given DNA sequence is valid, splits it into codons, counts how often each codon appears, and clearly shows the results automatically.

2. Scope of the Project

This program will:
Take a DNA sequence entered by the user.
Check that it only has valid letters (A, T, G, C).Break the sequence into groups of three bases (codons).
Count how many times each codon appears using an efficient method.
Show the results in a clear, sorted list.
Handle incorrect input properly by showing an error message.


3. Target UsersThis project is useful for:

Students learning about DNA and genetics.
Beginner programmers practicing Python with strings, loops, and dictionaries.
Researchers who need a quick tool to check codon usage in short DNA samples.Teachers looking for a neat, simple program for class demonstrations or assignments.

4. High-Level Features:

DNA Input & CleaningLets the user type or paste a DNA sequence.
Removes spaces and changes all letters to uppercase.
Input Validation Checks that the sequence only has the valid DNA letters (A, T, G, C).
Shows an error if any invalid characters are found.
Codon ExtractionBreaks the DNA into codons (sets of three bases).
Ignores extra bases if the sequence length is not a multiple of 3.
Codon Frequency CountingUses Python’s Counter to quickly count how often each codon appears.
Sorted Output DisplayShows codons and their counts in alphabetical order.
The output is simple, clear, and easy to read.