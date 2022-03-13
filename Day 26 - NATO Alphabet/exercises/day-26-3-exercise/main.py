def read_files(filename):
  with open(filename, mode="r") as f:
      numbers = f.readlines()
      numbers = [w.replace('\n', '') for w in numbers]
      #print("Number list:")
      #print(numbers)
      return numbers
      
file1_list = read_files("file1.txt")
file2_list = read_files("file2.txt")
result = [int(num) for num in file1_list if num in file2_list]



# Write your code above 👆

print(result)


