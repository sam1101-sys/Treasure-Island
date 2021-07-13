print('''
                                  _..-""""-.._                             
                              _.-'            `-._                         
                             /                    \                        
                            :    .-';      ;'-.    :                       
                            |   / _.-:    :-._ \   |                       
                            :  ; ;  o/    \o  ; ;  :                       
                           /    \_!-'      '-!_/    \                      
                          :'-..__              __..-':                     
                         /       \            /       \                    
                       .'\        \          /        /'.                  
                     .'   ;        `-.    .-'        ;   '.                
                    ;     :           '..'           :     ;               
                   :      |         __...__          |      :              
                   ;      |      .-'       `-.       |      ;              
                   :      :     /             \      :      :              
                  :      /     /               \      \      :             
                  ;    .'     :                 :      '.    ;             
                  ;   :      :                   :       :   ;             
                  ;   :      :                   :       :   ;             
                  :  /       :                   :        \  :             
                   ;;         \                 /          ;;              
                    ;-.        '-.     ,     .-'         .-;               
                     ;;'-...      '-..___..-'       ...-';;                
                      ";, \ ""--....________....--""/  ,;"                 
                           '.       .'    '.      .'                       
                             \     /        \    /                         
                              :   :          :  :                          
                              :    \        /   :        
                             /      '.    .'     \                         
                           .' _.  /  :   :        '.                       
        ____________________"/_) : ') \_/ (' : ( \"_______________fsc__  
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

choice1=input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left" or choice1 =="l":
  choice2=input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    choice3 =input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
    if choice3 =="yellow":
      print("You win!")
    elif choice3 =="red":
      print("Burned by Fire. Game over!")
    elif choice3 =="blue":
      print("Eaten by beasts. Game over!!")
    else:
      print("Wrong option")
  elif choice2 == "swim":
    input("Swim or anything else?")
    print("Game over")
  else:
    print("Wrong option")
elif choice1 == "right" or choice1 == "r":
  input("Right or anything else?")
  print("Fall into hole.Gameover")
else:
  print("Wrong option")