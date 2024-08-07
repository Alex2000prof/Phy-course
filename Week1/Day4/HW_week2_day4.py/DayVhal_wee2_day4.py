matrix = [
    "7ii",
    "Tsx",
    "h%?",
    "i #",
    "sM ",
    "$a ",
    "#t%",
    "^r!"
]
new_matrix = []
def open_matrix(matrix):
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            let = matrix[row][col]
            if let.isalpha():
                new_matrix.append(let)
            else:
                None
    word = "".join(new_matrix)
    finish_word = "".join(word.split())
    return finish_word
wordd = open_matrix(matrix)
print(wordd)