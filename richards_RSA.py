#######################################################################
#
#   richards_RSA.py is an example of the RSA cryptosystem I created for
#   fun in order to learn how RSA encryption works.
#
#   WHAT DOES THIS PROGRAM DO:
#   This program is my implimentation of the RSA cryptosystem.  A
#   cryptosystem is a set of tools used to communicate secret messages
#   over a (possibly) public network. TheRSA cryptosystem is an 
#   'antisymmetric' cryptosystem, meaning that when one person, Alice,
#   sends a message to another person, Bob, over a public network only
#   the person decrypting the message, Bob, needs to know special 
#   information, called a 'key', about the cryptosystem in order 
#   decrypt Alice's message. The idea is anyone who wants to send a 
#   message to Bob knows an encryption function E_bob that encrypts 
#   messeges and. E_bob should be easy to compute so people who want 
#   to talk to Bob can easyily encrypt their messages they send to him
#   and E_bob^-1 should be hard to compute without Bob's private key 
#   so other people won't be able decrypt messages meant for bob, 
#   however, E_bob^-1 should be easy to compute with the knowledge of 
#   Bob's private key, that way Bob can easily decrypt messages.
#   
#   HOW THIS PROGRAM WORKS
#   richard_RSA.py encrypts messages based off of an encryption 
#   function stored in a file called ownersnames_pubic_key.txt.  
#   The private key that the owner needs to decrypt messages is stored
#   in a file called ownersnames_private_key.txt.  The information 
#   other people need in order to encrypt files so you can decrypt 
#   them is stored in a file called yournames_public_key.txt.
#
#   HOW TO USE THIS PROGRAM:
#   
#       HOW TO ENCRYPT A FILE THAT BOB CAN DECRYPT:
#       
#           1)  Before you encrypt the file, information.txt, you want 
#               to send to Bob must save information.txt in the same
#               directory as richards_RSA.py and bobs_public_key.txt.
#
#                   ***MAKE SURE THE FILE CONTAINING BOB'S PUBLIC KEY
#                   IS CALLED bobs_public_key.txt OTHERWISE BOB WILL
#                   NOT BE ABLE TO DECRYPT YOUR MESSAGE***
#
#           2)  Go into terminal, type the following, hit [ENTER], and
#               follow the instructions:
#               
#                   python richards_RSA.py
#
#           3)  If you're running windows, just run richards_RSA.py in
#               a shell
#
#           4)  Now, you will have a new file in the same directory as
#               information.txt called
#               information_encrypted_bobs_key.txt. You can now send
#               this file off to Bob so they can decrypt it!
#
#       HOW TO DECRYPT:
#
#           1)  Before you decrypt your file, make sure you have the
#               file you want to decrypt,
#               information_encrypted_yournames_key.txt, saved in the
#               same directory as richards_RSA.py and
#               yournames_public_key.txt.  Also,
#
#                   ***MAKE SURE THE FILE CONTAINING YOUR PRIVATE KEY
#                   IS CALLED yournames_private_key.txt OTHERWISE YOU
#                   WILL NOT BE ABLE TO DECRYPT THE MESSAGE SENT TO
#                   YOU***
#
#           2)  Go into terminal, type the following, hit [ENTER], and
#               follow the instructions:
#
#               python richards_RSA.py
#
#           3)  If you're running windows, just run richards_RSA.py 
#               in a shell
#
#           5)  Now, you will have a new file in the same directory as
#               information_encrypted_yournames_key.txt called
#               information_decrypted_yournames_key.txt which is the
#               decrypted message sent to you.
#
#   NOTES ABOUT THE CODE:
#
#       ##  -   double pound signs are used to comment out code
#               that was used during debugging
#
#######################################################################

#Fast Power Algorithm i.e. fpow computes (g ** a) % n in O(log(a)) time

def fpow(g, a, n):

    answer = 1
    multiplier = g
    binaryexpansion = binexp(a)[::-1]
    
    for coefficient in binaryexpansion:
##        print('answer = ', str(answer))
##        print('multiplier = ', str(multiplier))
        if(int(coefficient) != 0):
##            print(coefficient, ' = 1')
            answer = (answer * multiplier) % n
##        else:
##            print(coefficient, ' = 0')
        multiplier = (multiplier * multiplier) % n

    return answer

def binexp(a):
    binary = bin(a)
    return list(binary[2:len(binary)])

# Extended euclidean algorithm returns [u, v, g]
# for the equation a*u + b*v = g

def extendedEuclideanAlgorithm(a, b):
    
    u = 1
    g = a
    x = 0
    y = b

    while(y > 0):
        q = g / y
        t = g % y
        s = u - (q * x)
        u = x
        g = y
        x = s
        y = t

    v = (g - (a * u)) / b

    return [u, v, g]

##print(exteucalg(8927, 8581))
##print(exteucalg(8581, 8927))
##print(exteucalg(123, 1234838))
##print(exteucalg(1234838, 123))
##print(exteucalg(459873982349, 1528385818238585))
##print(exteucalg(1528385818238585, 459873982349))

# Inv returns g^-1 (mod n)

def inv(g, n):

    uvg = extendedEuclideanAlgorithm(g, n)

    if(uvg[2] != 1):
        return 0

    else:
        return (uvg[0] % n)

#encrypts file called filename.txt and outputs file called filename_encrypted_ownersnames_key.txt

def encryptFile(fileName, ownersName):

    publicKeyFile = open(ownersName + 's_public_key.txt')
    n = int(publicKeyFile.readline()[:-1])
    e = int(publicKeyFile.readline())

##    print 'n = ' + str(n)
##    print 'e = ' + str(e)

    plainTextFile = open(fileName, 'r')
    plainText = plainTextFile.read()

##    print 'plainText = ' + plainText

    codeTexts = encode(plainText, n)

##    print 'codeTexts = ' + str(codeTexts)

    encryptedTexts = encryptInts(codeTexts, n, e)

    encryptedFile = open(fileName[:-4] + '_encrypted_' + ownersName + 's_key.txt', 'w')

    for line in encryptedTexts:
        encryptedFile.write(line + '\n')

    publicKeyFile.close()
    plainTextFile.close()
    encryptedFile.close()

def encryptInts(codeTexts, n, e):
    encryptedTexts = []

    for line in codeTexts:
        encryptedTexts.append(str(encryptInt(int(line), n, e)))

##    print str(encryptedTexts)

    return encryptedTexts

def encryptInt(m, n, e):
    return fpow(m, e, n)

def decryptFile(fileName, ownersName):
    
    privateKeyFile = open(ownersName + 's_private_key.txt')
    n = int(privateKeyFile.readline()[:-1])
    e = int(privateKeyFile.readline()[:-1])
    p = int(privateKeyFile.readline()[:-1])
    q = int(privateKeyFile.readline()[:-1])
    d = int(privateKeyFile.readline())

    encryptedFile = open(fileName, 'r')

    decryptedInts = []

    for line in encryptedFile:
        decryptedInts.append(str(decryptInt(int(line[:-1]),n,d)))

    decryptedText = decode(decryptedInts)

    decryptedTextFile = open(fileName[:-1 * (20 + len(ownersName))] + '_decrypted_' + ownersName + 's_key', 'w')

    decryptedTextFile.write(decryptedText)

    privateKeyFile.close()
    encryptedFile.close()
    decryptedTextFile.close()

def decryptInt(c, n, d):
    return fpow(c, d, n)

# for this part we're going to assume n is longer than about 10 digits
def encode(plainText, n):
    plainList = list(plainText)
    codeText = ''
    for word in plainList:
        codeText = codeText + str(ord(word) + 300)
    splitLength = len(str(n)) - 5
    codeTexts = []
    for i in range((len(codeText) / splitLength) + 1):
        codeTexts.append(codeText[splitLength * i : splitLength * (i + 1)])
    
    #if len(codeText) is divisible by splitLength, this will get rid of the the extra '' at the end of codeTexts because we add 1 iteration to the above loop for any leftovers
    if(codeTexts[:-1] is ''):
        return codTexts[:-1]

    else:
        return codeTexts

    return codeTexts

def decode(decryptedInts):

    decryptedText = ''

    for integer in decryptedInts:
        for character in range(len(integer) / 3):
##            print integer
##            print str(int(integer[character * 3:(character * 3) + 3]) - 300)
            decryptedText = decryptedText + chr(int(integer[character * 3:(character * 3) + 3]) - 300)

    return decryptedText


# In order to avoid the possibility the ambiguity of whether someone decrypting a message would have to type in the '_encrypted_ownersnames_key.txt' I created I function that gets rid of it if they typed it in as the file name and returns the filename if they didn't

def originalFileName(fileName, ownersName):
    if(len(fileName) < (16 + len(ownersName))):
            return fileName + '_encrypted_' + ownersName + 's_key.txt'
    else:
        if(fileName[:(-1 * (16 + len(ownersName)))] is '_encrypted_' + ownersName + 's_key'):
            return fileName + '.txt'
        else:
            return fileName + '_encrypted_' + ownersName + 's_key.txt'
    
# Main function that interacts with users.

def main():

    print '\n\nWho\'s the owner of the encryption key?\n'
    print '(please type their first name all lower case)\n'

    ownersName = ''
    ed = ''

    while(ownersName is ''):
        ownersName = raw_input('')
##    ownersName = 'RSA-704'

    print '\n\n\nWould you like to encrypt or decrypt a message?\n'
    print '(type [e/d] for encrypt or decrypt)\n'
    
    while(ed is ''):
        ed = raw_input('')
##    ed = 'd'

    if(ord(ed.lower()) == ord('e')):
        print '\n\n\nWhat is the name of the file you would like to encrypt?\n'
        fileName = raw_input('')
        print ''
        print 'fileName is ' + fileName
##        fileName = 'test1'

        if(fileName[:-4] is '.txt'):
            encryptFile(fileName, ownersName)

        else:
            encryptFile(fileName + '.txt', ownersName)

            print '\nYour file has been successfully encrypted to the file \'' + fileName + '_encrypted_' + ownersName + 's_key.txt\'\n\n'

    else:
        print '\n\n\nWhat is the name of the file you would like to decrypt?\n'

        fileName = raw_input('')
        print ''
##        fileName = 'test1'

        hasExtension = fileName[:-4] is '.txt'
        
        if(not hasExtension):
            fileName = originalFileName(fileName, ownersName)
##            print 'does not have extenseion\n'
        else:
            fileName = originalFileName(fileName[:-4], ownersName)
##            print 'does have extension\n'
##        print '\nfilename = ' + fileName + '\n'
        decryptFile(fileName, ownersName)
        print '\nYour file has been successfully decrypted to the file \'' + fileName[:-20 - len(ownersName)] + '_decrypted_' + ownersName + 's_key.txt\'' + '\n\n'

main()
