import time

#ASCII art, faces of dies
die=[""" ""","""\
               
┌───────┐
│       │
│   ●   │
│       │
└───────┘  

""","""\

┌───────┐
│ ●     │
│       │
│     ● │
└───────┘ 

""","""\

┌───────┐
│ ●     │
│   ●   │
│     ● │
└───────┘ 

 ""","""\

┌───────┐
│ ●   ● │
│       │
│ ●   ● │
└───────┘

""","""\

┌───────┐
│ ●   ● │
│   ●   │
│ ●   ● │
└───────┘

 ""","""\

┌───────┐
│ ●   ● │
│ ●   ● │
│ ●   ● │
└───────┘
                    """]

 #ASCII art, p_peruke contains the protected discs                   
p_peruke=["""" ""","""\
   
     
      ,'.
    ,'   `.
  ,'       `.
,'           `.
\      ●      /
 \           /
  \         /
   \_______/
    






""","""\


      ,'.
    ,'   `.
  ,'       `.
,'   ●       `.
\             /
 \           /
  \      ●  /
   \_______/


""","""\


      ,'.
    ,'   `.
  ,'       `.
,'     ●     `.
\             /
 \           /
  \ ●     ● /
   \_______/

""","""\


      ,'.
    ,'   `.
  ,'       `.
,' ●       ● `.
\             /
 \           /
  \●       ●/
   \_______/

""","""\


      ,'.
    ,'   `.
  ,'       `.
,' ●       ● `.
\      ●      /
 \ ●       ● /
  \         /
   \_______/

   ""","""\


      ,'.
    ,'   `.
  ,'       `.
,' ●       ● `.
\  ●       ●  /
 \ ●       ● /
  \         /
   \_______/

   """]

#ASCII art, u_peruke contains unprotected discs
u_peruke=["""" ""","""\
   
     
      ,'.
    ,'___`.
  ,'_______`.
,'           `.
\      ●      /
 \           /
  \         /
   \_______/
    






""","""\


      ,'.
    ,'___`.
  ,'_______`.
,'   ●       `.
\             /
 \           /
  \      ●  /
   \_______/


""","""\


      ,'.
    ,'___`.
  ,'_______`.
,'     ●     `.
\             /
 \           /
  \ ●     ● /
   \_______/

""","""\


      ,'.
    ,'___`.
  ,'_______`.
,' ●       ● `.
\             /
 \           /
  \●       ●/
   \_______/

""","""\


      ,'.
    ,'___`.
  ,'_______`.
,' ●       ● `.
\      ●      /
 \ ●       ● /
  \         /
   \_______/

   ""","""\


      ,'.
    ,'___`.
  ,'_______`.
,' ●       ● `.
\  ●       ●  /
 \ ●       ● /
  \         /
   \_______/

   """]




