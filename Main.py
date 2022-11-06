# import mysql.connector
import time
import random
import sys
from getpass import getpass
from datetime import date
from datetime import datetime
from methods import *
from array import *
from archive import *

#Connecting to the database 
# mydb=mysql.connector.connect(
# 	host="localhost",
# 	username="root",
# 	passwd="Warwick2022",
# 	database="UserInfo"
	
# )

#Database Commands:

#Initializing cursor of the database
# mycursor=mydb.cursor()   
# mycursor.execute("CREATE DATABASE UserInfo")
# mycursor.execute("CREATE TABLE gamers (name VARCHAR(255),ID INTEGER(10), password VARCHAR(255), nick VARCHAR(255))")
# mycursor.execute("CREATE TABLE ghistory (ID INTEGER(10), history VARCHAR(255), Day VARCHAR(255))")
# sqlCommand1="INSERT INTO gamers(name,ID,password,nick) VALUES(%s,%s,%s,%s)"
# sqlCommand2="INSERT INTO ghistory(ID,history,Day) VALUES (%s,%s,%s)"
# rmv = "DELETE FROM gamers WHERE Name='Tesla'"
# mydb.commit()


#Players, will be initialized as a Gamer objects
Player1=None 
Player2=None


#Interim variables
I_name=None 
I_id=None 
I_nick=None 
I_pwd=None 

#Variable that keeps info if user logged or played as a guest
log=0

#Interim lists, that contains elements of u_peruke and p_peruke for printing them in one line
I_arr1=[7,[],[]]
I_arr2=[7,[],[]]
I_die=[]


#Variable that keeps record of winner of every round
#For exm:if player 2 wins both rounds it will increase to 2, if looses that will be -2, in the case of draw it will stay 0
result=0
#Die array, consists of 4 elements with trivial first elemtent, and the rest represent 3 dies in the game
dies=[7,1,2,3]

#Two dimensional arrays that represent each players protected and unproteced disks
#First terms are 7 and empty lists are added to lists as it makes indexing more convenient
#The elements of these lists are -1,0,1 which represents captured,unproteced and protected discs correspondingly
arr1=[[],[7,0,0,0,0,0,0],[7,0,0,0,0,0,0]]
arr2=[[],[7,0,0,0,0,0,0],[7,0,0,0,0,0,0]]


#Player class
class Gamer:
 	def __init__(self,name):
 		self.name=name
 		# Num=random.randint(100,1000)
 		# if check(Num)==0:
 		# 	self.id=Num
 		# else:
 		# 	while check(Num)!=0:
 		# 		Num=random.randint(100,1000)
 		# 	self.id=Num
 		 
 		# self.nick=self.name+str(self.id)




#Menu of the game
def start():
	
 	print("Welcome to the Peruke game:)")
 	print("Do you want to play as a guest or to sign in?")
 	print("Guest--press 1 or signing in--press 2")
 	print("Please play as a guest if you are not in owner's computer")
 	global Player1,Player2,log
 	try:
 		ans=int(input())
 	except ValueError:
 		print("Please enter 1 or 2")
 		ans=int(input())
 	while(ans!=1 and ans!=2):
 		print("Please enter valid answer")
 		print("Guest--press 1 or signing in--press 2")
 		ans=int(input())
 	if(ans==1):
 		
 		
 		print("You will play as a guest")
 		Player1=Gamer("Player 1")
 		Player2=Gamer("Player 2")
 		main()
 	elif(ans==2):
 		log=1
 		inquiry("Player1")
 		
 		Player1=Gamer(I_name)
 		Player1.nick=I_nick
 		Player1.id=I_id
 		Player1.pwd=I_pwd
 		inquiry("Player2")
 		Player2=Gamer(I_name)
 		Player2.nick=I_nick
 		Player2.id=I_id
 		Player2.pwd=I_pwd
 		main()
 		
		


#Function asks for signing of players
def inquiry(Player):

 		print("Does {} have an account:Enter yes or no".format(Player))
 		ans = input().lower()
 		while(ans!="yes" and ans!="no"):
 			print("Please enter valid response")
 			print("Do you have an account:Enter yes or no")
 			ans = input().lower()
 		if(ans=="yes"):
 			print("{}, please login to your account".format(Player))
 			login()
 		elif(ans=="no"):
 			print("{}, please signup".format(Player))
 			new_user()

#login

def login():
	fetch_nick="SELECT nick FROM gamers WHERE nick= %s"
	print("Enter your nickname:")
	global I_nick

	I_nick=str(input())	   #Getting nickname from player  
	mycursor.execute(fetch_nick,(I_nick,))
	user_nick=mycursor.fetchall()		#Getting user_nick from database



	if(len(user_nick)==0):					# Checking if user exists or not
  		print("Username does not exist!")
  		print("Please create new account!")
  		print("Do you want to create new account?(Yes or No)")
  		reply=input().lower()
  		if reply=="yes":
  			new_user()
  		else:
  			sys.exit()

	else:
		global I_pwd
		global I_name
		global I_id
		#Using interim variables for saving name,password and id that are got from database and than assigning to 2 players of the game 
		I_pwd=getpass("Enter your  password:")
		fetch_pwd="SELECT password FROM gamers WHERE nick= %s"
		mycursor.execute(fetch_pwd,(I_nick,))
		user_pwd=mycursor.fetchone()
		for i in range(3):
			if(I_pwd==user_pwd[0]):
				fetch_name="SELECT name FROM gamers WHERE nick= %s"
				mycursor.execute(fetch_name,(I_nick,))
				user_name=mycursor.fetchone()
				fetch_id="SELECT ID FROM gamers WHERE nick= %s"
				mycursor.execute(fetch_id,(I_nick,))
				user_id=mycursor.fetchone()
				I_name=user_name[0]
				I_id=user_id[0]
			
				print("Welcome to main game:)")
				
				break
			else:
				print("Wrong password!")
				I_pwd=getpass("Enter your password again!:")
				if(i==2 and I_pwd!=user_pwd[0]):
					print("Please contact us about your password!")
					sys.exit()





#Function for checking primary row of arr1 and arr2
def empty_arr(arr):
	for i in range(1,7):
		if(arr[i]>-1):
			return False
			break
	else:
		return True

#Function for simulating, die throw
def die_throw():
	global dies
	for i in range(1,4):
		dies[i]=random.randint(1,6)
	while((dies[1]==dies[2] and dies[2]==dies[3]) or (dies[1]==dies[2] or dies[1]==dies[3] or dies[2]==dies[3])):
		for i in range(1,4):
			dies[i]=random.randint(1,6)
		

#Creating new user
def new_user():	
	print("Please enter your name to create your account:")
	Player=Gamer(input())
	Player.password=getpass("Please set a password:")
	print("Gamer is successfully created!")
	#Peruker is a tuple that gets new players info and dispatchs it to database with sql command
	Peruker=(Player.name,Player.id,Player.password,Player.nick)
	mycursor.execute(sqlCommand1,Peruker)
	mydb.commit() 
	print("These are your details:")
	print(" Name:{} \n Id:{} \n Nickname:{}".format(Player.name,Player.id,Player.nick))
	login()


#Main function of game
def main():
	global Player1
	global Player2
	print("These are the disks and dies, we are ready to start!")
	print_Peruke()
	time.sleep(5)
	play()
	print("Now round 2 is starting...")

	play()
	if(log==1):
		today=date.today()
		d2=today.strftime("%B %d, %Y")
		if(result==2):
			
			print("{} won the game".format(Player2.name))
			Winner=(Player2.id,"won",d2)
			Loser=(Player1.id,"lose",d2)
			mycursor.execute(sqlCommand2,Winner)
			mycursor.execute(sqlCommand2,Loser)
			mydb.commit()
		elif(result==-2):
			print("{} won the game".format(Player1.name))
			Winner=(Player1.id,"won",d2)
			Loser=(Player2.id,"lose",d2)
			mycursor.execute(sqlCommand2,Winner)
			mycursor.execute(sqlCommand2,Loser)
			mydb.commit()
		elif(result==0):
			print("Game ended in a draw")
			Draw1=(Player1.id,"draw",d2)
			Draw2=(Player2.id,"draw",d2)
			mycursor.execute(sqlCommand2,Draw1)
			mycursor.execute(sqlCommand2,Draw2)
			mydb.commit()

	elif(log==0):
		if(result==2):
			print("Player 2 won the game")
			

		elif(result==-2):
			print("Player 1 won the game")

		elif(result==0):
			print("Game ended in a draw")
		

	if(log==1):
		res=(Player1.id,)
		sql="SELECT * FROM ghistory WHERE ID=%s"
		print("{},Do you want to look your game history".format(Player1.name))
		ans=input().lower()
		if(ans=="yes"):
			mycursor.execute(sql,res)
			myhistory=mycursor.fetchall()
			for his in myhistory:
				print(his[1]+" "+his[2])
		elif(ans=="no"):
			pass

		res=(Player2.id,)
		sql="SELECT * FROM ghistory WHERE ID=%s"
		print("{},Do you want to look your game history".format(Player2.name))
		ans=input().lower()
		if(ans=="yes"):
			mycursor.execute(sql,res)
			myhistory=mycursor.fetchall()
			for his in myhistory:
				print(his[1]+" "+his[2])
		elif(ans=="no"):
			pass
		print("Game ended")
		sys.exit()
	elif(log==0):
		print("Game ended")
		sys.exit()





#Function of gameplay,attacking and protecting discs
def play():
	global Player1,Player2
	global I_arr1,I_arr2,p_peruke,u_peruke,arr1,arr2,I_die,result
	arr1=[[],[7,0,0,0,0,0,0],[7,0,0,0,0,0,0]]
	arr2=[[],[7,0,0,0,0,0,0],[7,0,0,0,0,0,0]]

	
	print("{} is throwing the die!".format(Player1.name))
	#Randomly, throwing 3 dies
	die_throw()
	time.sleep(3)
		
	print_Peruke()
	print("{},Choose three discs to protect:".format(Player1.name))
	for i in range(3):
		ans=input().lower()     #variable that asks for first or secondary row
		try:
			num=int(input())		#variable that ask the numbers of discs to protect
		except ValueError:
			print("Oops!  That was no valid number.  Try again...")
		while((num!=dies[1] and num!=dies[2] and num!=dies[3]) or (ans=='f' and arr1[1][num]==1) or (ans=='s' and arr1[2][num]==1) or (ans!='f' and ans!='s')):
			print("Please select right discs that match dies, or not already are protected!")
			ans=input().lower()     
			num=int(input())
		if(ans=='f'):
			arr1[1][num]=1
		elif(ans=='s'):
			arr1[2][num]=1
	print_Peruke()

	print("{} is throwing the die!".format(Player2.name))

	die_throw()
	time.sleep(3)	


	print_Peruke()
	print("{},Choose three discs to protect:".format(Player2.name))
	for i in range(3):
		ans=input().lower()     #variable that asks for first or secondary row(accepts(f-first row, s-secondry row))
		num=int(input())		#variable that ask the numbers of discs to protect
		while((num!=dies[1] and num!=dies[2] and num!=dies[3]) or (ans=='f' and arr2[2][num]==1) or (ans=='s' and arr2[1][num]==1) or (ans!='f' and ans!='s')):
			print("Please select right discs that match dies, or not already are protected!")
			ans=input().lower()   
			try:  
				num=int(input())
			except ValueError:
				print("Oops!  That was no valid number.  Try again...")
		if(ans=='f'):
			arr2[2][num]=1
		elif(ans=='s'):
			arr2[1][num]=1
	print_Peruke()

	#while primary row of player1's or player2's is not empty, continue to play
	while(empty_arr(arr1[1])==False and empty_arr(arr2[2])==False):
		print("{} is throwing the die!".format(Player1.name))
		die_throw()
		time.sleep(3)
		print_Peruke()
		for i in range(3):
			print("{} do you want to attack or protect?".format(Player1.name))
			rep=input().lower()    #variable that asks for attack or protect, accepts(a-attack, p-protect)
			ans=input().lower()
			try:
				num=int(input())
				
			except ValueError:
				print("Oops!  That was no valid number.  Try again...")

			while((num!=dies[1] and num!=dies[2] and num!=dies[3]) or (ans!='f' and ans!='s') or (rep!='a' and rep!='p') or (str(num).isdigit()==False or num>6 or num<1) or (rep=='p' and ans=='f' and arr1[1][num]!=0) or (rep=='p' and ans=='s' and arr1[2][num]!=0) or (rep=='a' and ans=='f' and arr2[2][num]<0) or (rep=='a' and ans=='s' and arr2[1][num]<0)):
				print("Please select right discs that match dies,attack or protect, or enter valid response!")
				rep=input().lower()
				ans=input().lower()
				num=int(input())
				if((rep=='p' and ans=='f' and arr1[1][num]!=0) or (rep=='p' and ans=='s' and arr1[2][num]!=0) or (rep=='a' and ans=='f' and arr2[2][num]<0) or (rep=='a' and ans=='s' and arr2[1][num]<0)):
					print("You cannot play this number,try other one")
					break

			if(rep=='a' and ans=='f' and arr2[2][num]>=0):
				arr2[2][num]-=1
					
			elif(rep=='a' and ans=='s' and arr2[1][num]>=0):
				arr2[1][num]-=1
					
			elif(rep=='p' and ans=='f' and arr1[1][num]==0):
				arr1[1][num]+=1
					
			elif(rep=='p' and ans=='s' and arr1[2][num]==0):
				arr1[2][num]+=1
					
		#checking primary rows at the end of each turn
		if(empty_arr(arr1[1])==True):
			print("{}, won the round".format(Player2.name))
			result+=1
			break
		elif(empty_arr(arr2[2])==True):
			print("{}, won the round".format(Player1.name))
			result-=1
			break


		print("{} is throwing the die!".format(Player2.name))
		die_throw()
		time.sleep(3)
		print_Peruke()
		for i in range(3):
			print("{} do you want to attack or protect?".format(Player2.name))
			rep=input().lower()
			ans=input().lower()
			try:
				num=int(input())
			except ValueError:
				print("Oops!  That was no valid number.  Try again...")

			while((num!=dies[1] and num!=dies[2] and num!=dies[3]) or (ans!='f' and ans!='s') or (rep!='a' and rep!='p') or (str(num).isdigit()==False or num>6 or num<1) or (rep=='p' and ans=='f' and arr2[2][num]!=0) or (rep=='p' and ans=='s' and arr2[1][num]!=0) or (rep=='a' and ans=='f' and arr1[1][num]<0) or (rep=='a' and ans=='s' and arr1[2][num]<0)):
				print("Please select right discs that match dies,attack or protect, or enter valid response!")
				rep=input().lower()
				ans=input().lower()
				num=int(input())
				if((rep=='p' and ans=='f' and arr2[2][num]!=0) or (rep=='p' and ans=='s' and arr2[1][num]!=0) or (rep=='a' and ans=='f' and arr1[1][num]<0) or (rep=='a' and ans=='s' and arr1[2][num]<0)):
					print("You cannot play this number,try other one")
					break
			if(rep=='a' and ans=='f' and arr1[1][num]>=0):
				arr1[1][num]-=1

			elif(rep=='a' and ans=='s' and arr1[2][num]>=0):
				arr1[2][num]-=1

			elif(rep=='p' and ans=='f' and arr2[2][num]==0):
				arr2[2][num]+=1

			elif(rep=='p' and ans=='s' and arr2[1][num]==0):
				arr2[1][num]+=1

		
		
		if(empty_arr(arr1[1])==True):
			print("{}, won the round".format(Player2.name))
			result+=1
			break
		elif(empty_arr(arr2[2])==True):
			print("{}, won the round".format(Player1.name))
			result-=1
			break




	

#This is UI function, that prints the discs and dies
def print_Peruke():
	global Player1,Player2
	global I_arr1,I_arr2,p_peruke,u_peruke,arr1,arr2,I_die
	I_arr1=[7,[],[]]
	I_arr2=[7,[],[]]
	I_die=[]
	for i in range(1,3):
		for j in range(1,7):
			if(arr1[i][j]==1):
				I_arr1[i].append(p_peruke[j])
			elif(arr1[i][j]==0):
				I_arr1[i].append(u_peruke[j])

	for i in range(1,3):
		for j in range(1,7):
			if(arr2[i][j]==1):
				I_arr2[i].append(p_peruke[j])
			elif(arr2[i][j]==0):
				I_arr2[i].append(u_peruke[j])


	for i in range(1,4):
		I_die.append(die[dies[i]])


	print('-'*150)
	print('-'*150)
	print("{}'s disks:".format(Player1.name))

	for lines in zip(*map(str.splitlines,I_arr1[1])):
		print(*(line.ljust(15) for line in lines))

	for lines in zip(*map(str.splitlines,I_arr1[2])):
		print(*(line.ljust(15) for line in lines))



	print('-'*100)

	for lines in zip(*map(str.splitlines,I_die)):
		print(*(line.ljust(15) for line in lines))


	print('-'*100)
	print("{}'s disks:".format(Player2.name))
	for lines in zip(*map(str.splitlines,I_arr2[1])):
		print(*(line.ljust(15) for line in lines))

	for lines in zip(*map(str.splitlines,I_arr2[2])):
		print(*(line.ljust(15) for line in lines))

    	

		
#Check function cheks if user already exists in database or not,
def check(id):
 mycursor.execute("SELECT * FROM gamers")
 GamerL=mycursor.fetchall()
 quickSort(GamerL,0,len(GamerL)-1)

 if binary_search(GamerL, 0, len(GamerL)-1, id)==-1:
 	return 0
 else:
  return 1

start()
