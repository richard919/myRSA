# myRSA



   richards_RSA.py is an example of the RSA cryptosystem I created for
   fun in order to learn how RSA encryption works.

   WHAT DOES THIS PROGRAM DO:
   This program is my implimentation of the RSA cryptosystem.  A
   cryptosystem is a set of tools used to communicate secret messages
   over a (possibly) public network. TheRSA cryptosystem is an 
   'antisymmetric' cryptosystem, meaning that when one person, Alice,
   sends a message to another person, Bob, over a public network only
   the person decrypting the message, Bob, needs to know special 
   information, called a 'key', about the cryptosystem in order 
   decrypt Alice's message. The idea is anyone who wants to send a 
   message to Bob knows an encryption function E_bob that encrypts 
   messeges and. E_bob should be easy to compute so people who want 
   to talk to Bob can easyily encrypt their messages they send to him
   and E_bob^-1 should be hard to compute without Bob's private key 
   so other people won't be able decrypt messages meant for bob, 
   however, E_bob^-1 should be easy to compute with the knowledge of 
   Bob's private key, that way Bob can easily decrypt messages.
   
   HOW THIS PROGRAM WORKS:
   richard_RSA.py encrypts messages based off of an encryption 
   function stored in a file called ownersnames_pubic_key.txt.  
   The private key that the owner needs to decrypt messages is stored
   in a file called ownersnames_private_key.txt.  The information 
   other people need in order to encrypt files so you can decrypt 
   them is stored in a file called yournames_public_key.txt.

   HOW TO USE THIS PROGRAM:
   
       HOW TO ENCRYPT A FILE THAT BOB CAN DECRYPT:
       
           1)  Before you encrypt the file, information.txt, you want 
               to send to Bob must save information.txt in the same
               directory as richards_RSA.py and bobs_public_key.txt.

                   ***MAKE SURE THE FILE CONTAINING BOB'S PUBLIC KEY
                   IS CALLED bobs_public_key.txt OTHERWISE BOB WILL
                   NOT BE ABLE TO DECRYPT YOUR MESSAGE***

           2)  Go into terminal, type the following, hit [ENTER], and
               follow the instructions:
               
                   python richards_RSA.py

           3)  If you're running windows, just run richards_RSA.py in
               a shell

           4)  Now, you will have a new file in the same directory as
               information.txt called
               information_encrypted_bobs_key.txt. You can now send
               this file off to Bob so they can decrypt it!

       HOW TO DECRYPT:

           1)  Before you decrypt your file, make sure you have the
               file you want to decrypt,
               information_encrypted_yournames_key.txt, saved in the
               same directory as richards_RSA.py and
               yournames_public_key.txt.  Also,

                   ***MAKE SURE THE FILE CONTAINING YOUR PRIVATE KEY
                   IS CALLED yournames_private_key.txt OTHERWISE YOU
                   WILL NOT BE ABLE TO DECRYPT THE MESSAGE SENT TO
                   YOU***

           2)  Go into terminal, type the following, hit [ENTER], and
               follow the instructions:

               python richards_RSA.py

           3)  If you're running windows, just run richards_RSA.py 
               in a shell

           5)  Now, you will have a new file in the same directory as
               information_encrypted_yournames_key.txt called
               information_decrypted_yournames_key.txt which is the
               decrypted message sent to you.

   NOTES ABOUT THE CODE:

       ##  -   double pound signs are used when to comment out code
               that was used during debugging
