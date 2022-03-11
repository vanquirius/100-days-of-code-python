sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
words = sentence.split(" ")
word_count = {word:len(word) for word in words}
print(word_count)