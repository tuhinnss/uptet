"""English translation of UPTET 2018 Primary, Part IV (Q91–120): Mathematics.

The solved paper prints this section in Hindi only; this is our own translation.
EN: {n: (question, options or None to reuse the Hindi ones, explanation)}.
"""

EN = {
    93: ('If a shopkeeper makes a profit of 20% by selling an article for Rs. 390, the cost price of the article is',
         ['Rs. 321', 'Rs. 323', 'Rs. 324', 'Rs. 325'],
         'Selling price = cost price × 1.2, so cost price = 390 ÷ 1.2 = Rs. 325.'),
    94: ('If the population of a town grows from 60000 to 65000, the increase in population (in per cent) is',
         None,
         'Increase = 65000 − 60000 = 5000. Percentage increase = (5000/60000) × 100 = 25/3 = 8 1/3%.'),
    95: ('40 people eat 200 kg of rice in 30 days. In how many days will 30 people eat 500 kg of rice?',
         None,
         '40 people eat 200 kg in 30 days, so one person eats 200/1200 = 1/6 kg a day. 30 people eat 5 kg a day, so '
         '500 kg lasts 500 ÷ 5 = 100 days.'),
    96: ('The diagonals of a rhombus are 16 cm and 12 cm long. The side of the rhombus is',
         None,
         'The diagonals of a rhombus bisect each other at right angles. The half-diagonals are 8 cm and 6 cm, so the '
         'side = √(8² + 6²) = 10 cm.'),
    98: ('If the cost price of 8 pens equals the selling price of 6 pens, the profit per cent is',
         None,
         'Let one pen cost Rs. 1. Then 6 pens sell for Rs. 8 (the cost of 8 pens) but cost Rs. 6. Profit = Rs. 2 on '
         'Rs. 6, so profit % = (2/6) × 100 = 33 1/3%.'),
    99: ('Which of the following rational numbers does not lie between 3/5 and 4/5?',
         None,
         '3/5 = 0.6 and 4/5 = 0.8. 19/30 ≈ 0.63, 2/3 ≈ 0.67 and 7/10 = 0.7 lie between them, but 16/30 ≈ 0.53 does '
         'not.'),
    100: ('If 3 pens, 2 pencils and 4 erasers cost Rs. 92, and 8 pencils and 16 erasers cost Rs. 68, then 24 pens cost',
          ['Rs. 625', 'Rs. 500', 'Rs. 675', 'Rs. 600'],
          '8 pencils + 16 erasers = 68, so 2 pencils + 4 erasers = 17. Then 3 pens = 92 − 17 = 75, one pen = Rs. 25, '
          'and 24 pens = Rs. 600.'),
    101: ('We cannot construct a triangle if we are given',
          ['two angles and one side', 'only the three sides', 'only the three angles',
           'two sides and the angle between them'],
          'With only the three angles, countless similar triangles of different sizes are possible, so no particular '
          'triangle is fixed. In the other cases a triangle can be constructed.'),
    102: ('If the length and breadth of a rectangular plot are increased by 50% and 20% respectively, how many times '
          'the original area will its area become?',
          None,
          'New area = 1.5 × 1.2 = 1.8 = 1 4/5 times the original area.'),
    103: ('The body temperature of a normal human is 37° C. On the Fahrenheit scale this temperature is',
          None,
          'F = (9/5) × C + 32 = (9/5) × 37 + 32 = 66.6 + 32 = 98.6° F.'),
    104: ('If 1² + 2² + ….. + 9² = 285, then the value of (0.11)² + (0.22)² + ….. + (0.99)² is',
          None,
          '(0.11)² = (0.11)² × 1², (0.22)² = (0.11)² × 2², and so on, so the sum = 0.0121 × (1² + 2² + ... + 9²) = '
          '0.0121 × 285 = 3.4485.'),
    105: ('A sum of money doubles in 10 years at simple interest. In how many years will it triple at the same rate?',
          ['30 years', '25 years', '20 years', '15 years'],
          'In 10 years the interest equals the principal (100%), so the rate is 10% a year. To triple, the interest '
          'must be 200%, which takes 20 years.'),
    106: ('A square playground of the largest possible area is made inside a circular park of diameter 80 m. The area '
          'of the playground is',
          None,
          'The diagonal of the largest square inside a circle equals the diameter (80 m). Area of the square = '
          'diagonal²/2 = 6400/2 = 3200 m².'),
    107: ('In an examination of 240 marks, a candidate scored 52 marks. The corresponding angle in a pie chart is',
          None,
          'Angle = (52/240) × 360° = 78°.'),
    108: ('If P% of P is 36, then P equals',
          None,
          'P% of P = P × P/100 = 36, so P² = 3600 and P = 60.'),
    109: ('If 2352 = 2ˣ × 3ʸ × 7ᶻ, then the value of x + y + z is',
          None,
          '2352 = 2⁴ × 3 × 7², so x = 4, y = 1, z = 2 and x + y + z = 7.'),
    110: ('The number of even divisors of 100 is',
          None,
          '100 = 2² × 5². Its divisors are 1, 2, 4, 5, 10, 20, 25, 50 and 100; the even ones are 2, 4, 10, 20, 50 and '
          '100, which makes 6.'),
    111: ('How many cubes of side 3 cm can be cut from a cube of side 15 cm?',
          None,
          'Each edge holds 15 ÷ 3 = 5 small cubes, so there are 5 × 5 × 5 = 125 cubes in all.'),
    112: ('The remainder when 3¹⁹⁸⁹ is divided by 7 is',
          None,
          '3⁶ = 729 leaves remainder 1 when divided by 7. 1989 = 6 × 331 + 3, so the remainder is the same as for '
          '3³ = 27, which is 6.'),
    113: ('The sum of the interior angles of a polygon is 2160°. The number of sides of the polygon is–',
          None,
          'The interior angles of an n-sided polygon add up to (n − 2) × 180°. (n − 2) × 180 = 2160 gives n = 14.'),
    114: ('The smallest non-negative prime integer is–',
          None,
          '0 and 1 are not prime numbers; the smallest prime is 2.'),
    115: ('(1½ + 11½ + 111½ + 1111½) equals–',
          None,
          '1.5 + 11.5 + 111.5 + 1111.5 = 1236.'),
    116: ('If a * b = a² + b² – ab for all natural numbers a and b, then the value of 9 * 10 is',
          None,
          '9 * 10 = 9² + 10² − 9 × 10 = 81 + 100 − 90 = 91.'),
    117: ('If x and y are non-zero real numbers, then x² + xy + y²',
          ['is always negative', 'is zero for some values of x and y', 'is always positive',
           'can be both positive and negative'],
          'x² + xy + y² = (x + y/2)² + 3y²/4. For non-zero x and y this is always positive.'),
    119: ('If aᵇ = 125 for two natural numbers a and b, then bᵃ is',
          None,
          '125 = 5³, so a = 5 and b = 3. Then bᵃ = 3⁵ = 243.'),
    120: ('The smallest number divisible by all the natural numbers from 1 to 10 is',
          None,
          'The LCM of the numbers 1 to 10 = 2³ × 3² × 5 × 7 = 2520.'),
}
