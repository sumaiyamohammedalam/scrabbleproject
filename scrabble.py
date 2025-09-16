# Letters and points dictionary
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", 
           "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", 
           "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Map letters to points
letter_to_points = dict(zip(letters, points))
letter_to_points[" "] = 0  # blank tile

# Function to score a single word
def score_word(word):
    point_total = 0
    for l in word.upper():  # handle lowercase letters too
        point_total += letter_to_points.get(l, 0)
    return point_total

# Test scoring
brownie_points = score_word("BROWNIE")
print("BROWNIE points:", brownie_points)  # Expected: 15

# Players and their words
player_to_words = {
    "wordNerd": ["BLUE", "TENNIS", "EXIT"],
    "Lexi Con": ["EARTH", "EYES", "MACHINE"],
    "Prof Reader": ["ERASER", "BELLY", "HUSKY"],
    "ZAP": ["ZAP", "COMA", "PERIOD"]
}

# Calculate points for each player
player_to_points = {}

for player, words in player_to_words.items():
    player_points = 0
    for word in words:
        player_points += score_word(word)
    player_to_points[player] = player_points

# Print player scores
print("Player scores:", player_to_points)
