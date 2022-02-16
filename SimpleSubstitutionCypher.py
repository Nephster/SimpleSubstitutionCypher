import argparse
import string
 
 
# A list containing all characters
all_letters= string.ascii_letters
#emojis_letters=['😀','😃','😄','😁','😆','😅','😂','🤣','😊','😇','🙂','🙃','😉','😌','😍','🥰','😘','😗','😙','😚','😋','😛','😝','😜','🤪','🤨','🧐','🤓','😎','🤩','🥳','😏','😒','😞','😔','😟','😕','🙁','☹','😣','😖','😫','😩','🥺','😢','😭','😤','😠','😡','🤬','🤯','😳']
weird_letters = string.ascii_letters
def generate_dic(key):
    dict1 = {}
    key=int(key)
    for i in range(len(all_letters)):
        dict1[all_letters[i]] = weird_letters[(i+key) % len(weird_letters)]
    return dict1    

def encrypt(key,data):
    CipherTxt = []
    dict1 = generate_dic(key)
    for x in data:
        if x in all_letters:
            CipherTxt.append(dict1[x])
        else:
            print("Char {} is not in the ascii letters".format(x)) 
    return CipherTxt

def decrypt(key,enc_data):
    data = []
    dict1 = generate_dic(key)
    #print(enc_data)
    for x in enc_data:
        if x in weird_letters:
            for key, value in dict1.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
                if x == value:
                    data.append(key)
    return data

def main():
    parser = argparse.ArgumentParser(description="Simple transposition cypher")
    parser.add_argument("-k", "--key", help="key")
    parser.add_argument("-e", "--enc", help="Data to encrypt")
    parser.add_argument("-d", "--dec", help="Data to decrypt")
    args = parser.parse_args()
    key = args.key
    data = args.enc
    enc_data = args.dec
    #print(key,data,enc_data)
    
    if data != None and enc_data == None:
        print("".join(encrypt(key,data)))
    elif data == None and enc_data != None:
        print("".join(decrypt(key,enc_data)))
    else:
        print("Wrong parameters selection")
    #print(dict1)
    
if __name__ == "__main__":
    main()