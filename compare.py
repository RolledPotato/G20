with open("Beast.txt") as f1, open("Beast0.txt") as f2:
    file1_words = f1.read().split()
    file2_words = f2.read().split()

    different_words = set(file1_words) ^ set(file2_words)

    if different_words:
        print("Words that are different between the two files:")
        for word in different_words:
            print(word)
    else:
        print("The two files have the same words!")
