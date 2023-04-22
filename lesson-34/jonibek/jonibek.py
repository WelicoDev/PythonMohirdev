# Open the file in read mode
with open("message.txt", "r") as f:
    # Read the contents of the file
    contents = f.read()

    # Initialize a counter variable for the number of questions
    num_questions = 0

    # Split the contents into sentences
    sentences = contents.split(". ")

    # Loop through each sentence
    for sentence in sentences:
        # Check if the sentence ends with a question mark
        if sentence.endswith("?"):
            # Increment the counter if it does
            num_questions += 1

    # Print the number of questions found
    print("Number of questions:", num_questions)