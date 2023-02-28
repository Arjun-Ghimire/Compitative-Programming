"""how many binary sequences (sequences of 0's and 1's ) of length 19 are there that begin with a 0, end with a 0,
contain no two consecutive 0's and contan no three consecutive 1's"""

# Define a function to check if a binary sequence satisfies the conditions
def is_valid(sequence):
  # Check if the sequence begins and ends with 0
  if sequence[0] != "0" or sequence[-1] != "0":
    return False
  # Check if the sequence contains two consecutive 0s or three consecutive 1s
  for i in range(len(sequence) - 1):
    if sequence[i] == "0" and sequence[i + 1] == "0":
      return False
    if i < len(sequence) - 2 and sequence[i] == "1" and sequence[i + 1] == "1" and sequence[i + 2] == "1":
      return False
  # If none of the above conditions are violated, return True
  return True

# Define a function to generate all possible binary sequences of length n
def generate_sequences(n):
  # Base case: if n is zero, return an empty list
    if n == 0:
        return []
  # Base case: if n is one, return ["0", "1"]
    if n == 1:
        return ["0", "1"]
  # Recursive case: append "0" and "1" to each sequence of length n - 1 and store them in a list
    sequences = []
    for seq in generate_sequences(n - 1):
        sequences.append(seq + "0")
        sequences.append(seq + "1")
  
   # Return the list of sequences 
    return sequences

# Define a function to count how many valid sequences of length n exist 
def count_valid_sequences(n):
   # Initialize a counter variable 
   count = 0
   
   # Loop through all possible sequences of length n 
   for seq in generate_sequences(n):
     # If the sequence is valid, increment the counter 
     if is_valid(seq):
       count += 1
   
   # Return the counter value 
   return count

# Print the answer for n =19 
print(count_valid_sequences(19))
