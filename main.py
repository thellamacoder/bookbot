from stats import word_count
import sys

def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")  
  word_length = str
  book = sys.argv[1]
  with open(f"{book}") as f:
    file_contents = f.read()
  #print(file_contents)



  def character_counts(text):
    # characters contains all the characters to match in the 
    characters = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}#," ":0,".":0,",":0,";":0}
    words = text.lower()

    # cycle through all the keys in the characters dictionary and set the times variable to 0
    for k in characters.keys():
      # here is where you count(items[k]) in words
      times = 0
      # cycle through the words in the source text and iterate the times variable each time that key/character appears
      for word in words:
        if k in word:
          times += 1
        # set the value for the key/character being compared
        characters[k] = times
    # print(characters)
    print(f"--- Begin report of books/{book} ---")
    for k, v in characters.items():
      print(f"{k}: {v}")


  print(word_count(file_contents))
  print(character_counts(file_contents))

main()