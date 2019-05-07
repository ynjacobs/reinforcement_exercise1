documentary = 'Hoop Dreams'
drama =  'Full House'
comedies = 'Friends'
dramedy = 'The Wonder Years'
answer = ""



while answer != "none":
   print("Do you enjoy 1.documentaries, 2.dramas or 3.comedies? (please select a number or answer none)") 
   answer = input()
   if answer == '1':
        print('you shloud try {}'.format(documentary))
        break

   elif answer == '2 and 3':
        print('you should try {}'.format(dramedy))
        break

   elif answer == '2':
        print('you shloud try {}'.format(drama))
        break

   elif answer == '3':
        print('you shloud try {}'.format(comedies))
        break

   else:
       print('you should try Harry Potter')
       
