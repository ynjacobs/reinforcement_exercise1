documentary = 'Hoop Dreams'
drama =  'Full House'
comedies = 'Friends'
dramedy = 'The Wonder Years'
alt_book = 'Harry Potter'

print('on a scale from 1 to 5 how much do you enjoy 1.documentaries, 2.dramas or 3.comedies?')
documentary_rate = int(input('documentary?\n'))
drama_rate = int(input('drama?\n'))
comedy_rate = int(input('comedy?\n'))


if documentary_rate >= 4:
    print('Try {}'.format(documentary))
elif comedy_rate >= 4 and drama_rate >= 4:
    print('Try {}'.format(dramedy))
elif  drama_rate >= 4:
    print('Try {}'.format(drama))
elif  comedy_rate >= 4:
    print('Try {}'.format(comedies))
elif documentary_rate <= 3 and drama_rate <=3 and comedy_rate <=3:
    if documentary_rate > drama_rate and documentary_rate > comedy_rate:
        print('Try1 {}'.format(documentary))
    elif drama_rate > documentary_rate and drama_rate > comedy_rate:
        print('Try1 {}'.format(drama))
    elif comedy_rate > documentary_rate and comedy_rate > drama_rate:
         print('Try1 {}'.format(comedies))
else:
    print('Try {}'.format(alt_book))
