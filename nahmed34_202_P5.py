# Name: Nafiz Ahmed

import random

#seed the random number generator so that 
#the randomness is the same each time you
#run the file. you can change this number 
#to get your code to match individual tests
random.seed(0)

# Defining the generate_durations function
def generate_durations(base_tempo):
    final = {}
    whole = 4 / (base_tempo/60) # One measure of the song is 
                                    # equivalent to four beats.
    half = whole/2
    quarter = whole/4   # dividing by the note types
    eighth = whole/8
    sixteenth = whole/16
    final = {'Whole': whole, 'Half': half, 'Quarter': quarter,
    'Eighth': eighth, 'Sixteenth': sixteenth}
    return final

# Defining the generate frequencies function
def generate_frequencies(base_freq):
    notes = []
    final = {}
    n = -48 # n value starting point
    for i in range(9):  #creating a list to hold all the notes
        if i == 0:
            notes.append('A' + str(i))
            notes.append('A#' + str(i))
            notes.append('B' + str(i))
        if i != 0 and i != 8:
            notes.append('C' + str(i))
            notes.append('C#'+ str(i))
            notes.append('D'+ str(i))
            notes.append('D#'+ str(i))
            notes.append('E'+ str(i))
            notes.append('F'+ str(i))
            notes.append('F#'+ str(i))
            notes.append('G'+ str(i))
            notes.append('G#'+ str(i))
            notes.append('A'+ str(i))
            notes.append('A#'+ str(i))
            notes.append('B'+ str(i))
        if i == 8:
            notes.append('C'+ str(i))
    for i in notes:
        frequency = base_freq * (2**(n/12)) # applying the keys and values
        final[i] = frequency
        n += 1
    return final

# Defining the find note function
def find_note(filename, highest_or_lowest):
    notes = []
    xs = []
    tempo = [',Whole', ',Half', ',Quarter',  ',Eighth', ',Sixteenth']
    f = open(filename, 'r')
    text = f.read()
    f.close()
    text = text.split()
    for i in range(9):  #Loop will make a list to hold all the notes
        if i == 0:
            notes.append('A' + str(i))
            notes.append('A#' + str(i))
            notes.append('B' + str(i))
        if i != 0 and i != 8:
            notes.append('C' + str(i))
            notes.append('C#'+ str(i))
            notes.append('D'+ str(i))
            notes.append('D#'+ str(i))
            notes.append('E'+ str(i))
            notes.append('F'+ str(i))
            notes.append('F#'+ str(i))
            notes.append('G'+ str(i))
            notes.append('G#'+ str(i))
            notes.append('A'+ str(i))
            notes.append('A#'+ str(i))
            notes.append('B'+ str(i))
        if i == 8:
            notes.append('C'+ str(i))
    for i in text:
        for j in tempo: # Allows me to compare keys from notes with file
            for k in notes:
                if k + j == i: # Do they match?
                    xs.append(k) # Puts all the keys from file in the list
    if highest_or_lowest == True:
        index = 0
        for i in range(len(notes)): # Will find the highest index
            for j in xs:
                if notes[i] == j: # Find a match between the keys
                    if i > index: # Set the index
                        index = i
        return notes[index]
    
    if highest_or_lowest == False:
        index = len(notes) - 1 # Start from the highest index
        for i in range(len(notes)): # Will find the lowest index
            for j in xs:
                if notes[i] == j:
                    if i < index:
                        index = i
        return notes[index]

# Defining the random song function
def random_song(filename, tempo, tuning, num_measures):
    total = 0
    values = {'Whole': 4, 'Half': 2, 'Quarter': 1,
    'Eighth': 0.5, 'Sixteenth': 0.25} # tells me how much each is worth
    notetype = ["Sixteenth", "Eighth", 'Quarter', 'Half','Whole']
    letter = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
    file = open(filename, 'w')
    file.write(str(tempo))
    file.write('\n' + str(tuning))
    
    measure = 4
    current = 0
    while total < num_measures: # Number of measures is not completed
        type = random.choice(notetype) # random note type
        compare = values[type] # get the value of the type
        current = compare
        if current <= measure: # compare if current amount is above 4
            note = random.choice(letter)
            octave = random.randint(1,7)
            file.write('\n' + note + str(octave) + ',' + type)
            measure -= current # update the current about of bpm left
            current = 0
        
        if measure == 0: # if one measure is complete
            total += 1
            measure = 4
    file.write('\n')
    file.close()

# Defining the change notes function
def change_notes(filename, changes, shift):
    tempo = [',Whole', ',Half', ',Quarter',  ',Eighth', ',Sixteenth']
    notes = []
    for i in range(9):  #Loop will make a list to hold all the notes
        if i == 0:
            notes.append('A' + str(i))
            notes.append('A#' + str(i))
            notes.append('B' + str(i))
        if i != 0 and i != 8:
            notes.append('C' + str(i))
            notes.append('C#'+ str(i))
            notes.append('D'+ str(i))
            notes.append('D#'+ str(i))
            notes.append('E'+ str(i))
            notes.append('F'+ str(i))
            notes.append('F#'+ str(i))
            notes.append('G'+ str(i))
            notes.append('G#'+ str(i))
            notes.append('A'+ str(i))
            notes.append('A#'+ str(i))
            notes.append('B'+ str(i))
        if i == 8:
            notes.append('C'+ str(i))
    f = open(filename, 'r')
    text = f.read()
    f.close()
    text = text.split()
    newfile = open(filename[:-5] + '_changed.song', 'w')
    newfile.write(text[0])
    newfile.write('\n' + text[1])
    for i in text:
        for j in tempo: # Allows me to compare keys from notes with file
            for k in range(len(notes)):
                if notes[k] + j == i: # Do they match?
                    for keys in changes.keys(): # finds if it's change value
                        if notes[k] == keys: # if letter == changes
                            newfile.write('\n' + changes[keys] + j)
                    if shift + k < 0 or shift + k > 87: # if it's invalid key
                        newfile.write('\n' + notes[k] + j)
                    else: # make the shift
                        newfile.write('\n' + notes[k+shift] + j)
    newfile.write('\n')
