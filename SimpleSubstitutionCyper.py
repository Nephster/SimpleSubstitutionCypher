import argparse
import string
 
 
# A list containing all characters
all_letters= string.ascii_letters
emojis_letters=['😀','😃','😄','😁','😆','😅','😂','🤣','😊','😇','🙂','🙃','😉','😌','😍','🥰','😘','😗','😙','😚','😋','😛','😝','😜','🤪','🤨','🧐','🤓','😎','🤩','🥳','😏','😒','😞','😔','😟','😕','🙁','☹','😣','😖','😫','😩','🥺','😢','😭','😤','😠','😡','🤬','🤯','😳']
dict1= {}

def encrypt(key,data):
    CipherTxt = []
    for i in range(len(all_letters)):
        dict1[all_letters[i]] = emojis_letters[(i+key)%len(emojis_letters)]

    for x in data:
        if x in all_letters:
            CipherTxt.append(dict1[x])
        else:
            print("Char {} is not in the ascii letters".format(x)) 
    return CipherTxt
def main():
    parser = argparse.ArgumentParser(description="Simple transposition cypher")
    parser.add_argument("-k", "--key", help="key")
    parser.add_argument("-d", "--data", help="Data to encrypt/decrypt")
    args = parser.parse_args()
    print("".join(encrypt(7,"fhrgsdfgsdgfsdfgsdfgsfgsdfgsfgsdfg")))
    #print(dict1)

if __name__ == "__main__":
    main()