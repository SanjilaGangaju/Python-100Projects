import time
import random
start_time=time.time()
def botname(bot_name):
    print("Hello! I am "+ bot_name + '.')
    
def username():
    global user_name
    print("What is your name you beautiful human?")
    user_name=input()
    user_name = user_name.capitalize()
    print(f"What a great name you have {user_name}.")

def guess_num():
    print("I have a power to guess the number u have on your mind right now. ")
    print("Think any number between 1 and 50")
    lower_bound=1
    upper_bound=50
    tries=0
    while True:
        guess=random.randint(lower_bound,upper_bound)
        user_guess=input(f"Is {guess} the number you are thinking of? (Type 'yes', 'higher', or 'lower'):").lower()
        if user_guess=='yes':
            print("Great! I guessed it in ",tries,"tries.")
            break
        elif user_guess=="higher":
            lower_bound=guess+1
            tries+=1
        elif user_guess=="lower":
            upper_bound=guess-1
            tries+=1
        else:
            print("Please respond with 'yes','higher',or 'lower'.")
def test():
    print("Lets see if u can guess the animal.")
    animal1 = r"""
              ___.-''''-.
/___  @    |
',,,,.     |         _.'''''''._
     '     |        /           \
     |     \    _.-'             \
     |      '.-'                  '-.
     |                               ',
     |                                '',
      ',,-,                           ':;
           ',,| ;,,                 ,' ;;
              ! ; !'',,,',',,,,'!  ;   ;:
             : ;  ! !       ! ! ;  ;   :;
             ; ;   ! !      ! !  ; ;   ;,
            ; ;    ! !     ! !   ; ;
            ; ;    ! !    ! !     ; ;
           ;,,      !,!   !,!     ;,;
           /_I      L_I   L_I     /_I
"""
    animal2 = r"""
                                            ,w.
                                             ,YWMMw  ,M  ,
                        _.---.._   __..---._.'MMMMMw,wMWmW,
                   _.-""        '''           YP"WMMMMMMMMMb,
                .-' __.'                   .'     MMMMW^WMMMM;
    _,        .'.-'"; `,       /`     .--""      :MMM[==MWMW^;
 ,mM^"     ,-'.'   /   ;      ;      /   ,       MMMMb_wMW"  @\
,MM:.    .'.-'   .'     ;     `\    ;     `,     MMMMMMMW `"=./`-,
WMMm__,-'.'     /      _.\      F'''-+,,   ;_,_.dMMMMMMMM[,_ / `=_}
"^MP__.-'    ,-' _.--""   `-,   ;       \  ; ;MMMMMMMMMMW^``; __|
           /   .'            ; ;         )  )`{  \ `"^W^`,   \  :
          /  .'             /  (       .'  /     Ww._     `.  `"
         /  Y,              `,  `-,=,_{   ;      MMMP`""-,  `-._.-,
        (--, )                `,_ / `) \/"")      ^"      `-, -;"\:
"""
    animal3 = r"""
          /|       |\
`__\\       //__'
   ||      ||
 \__`\     |'__/
   `_\\   //_'
   _.,:---;,._
   \_:     :_/
     |@. .@|
     |     |
     ,\.-./ \
     ;;`-'   `---__________-----.-.
     ;;;                         \_\
     ';;;                         |
      ;    |                      ;
       \   \     \        |      /
        \_, \    /        \     |\
          |';|  |,,,,,,,,/ \    \ \_
          |  |  |           \   /   |
          \  \  |           |  / \  |
           | || |           | |   | |
           | || |           | |   | |
           | || |           | |   | |
           |_||_|           |_|   |_|
          /_//_/           /_/   /_


"""
    print(animal1)
    while True: 
        guess_animal1 = input("Tell me the name of this animal: ").lower()
        if guess_animal1 == 'camel':
            print("You are an intelligent person.")
            break
        else:
            print("Work hard!!")

    print(animal2)
    while True: 
        guess_animal2 = input("Tell me the name of this animal: ").lower()
        if guess_animal2 == 'lion':
            print("You are an intelligent person.")
            break
        else:
            print("Work hard!!")

    print(animal3)
    while True: 
        guess_animal3 = input("Tell me the name of this animal: ").lower()
        if guess_animal3 == 'deer':
            print("You are an intelligent person.")
            break
        else:
            print("Work hard!!")
def end():
    print(f"It was nice spending time with you {user_name}.")

def creator():
    print("Do u wanna know the God who created me?")
    boss=input().lower()
    if boss=="yes":
        print("My Boss is 'Sanjila' the greatest!!")
    elif boss=="no":
        print("Oops! You unlucky one u couldnot know the greatest divine person!")
    else:
        print("answer me yes or no !!bro")
def bmi():
    user_weight=float(input("Enter your body weight in kilograms:"))
    user_height=float(input("Enter your height in centimeters:"))
    user_height=user_height/100
    BMI=user_weight/(user_height*user_height)
    print("Your Body Mass Index :",BMI)
    if BMI<18.5:
     print("Underweight.")
    elif 18.5<BMI<24.9:
      print("Normal Weight")
    elif 25<BMI<29.9:
     print("Overweight")
    elif BMI>=30:
      print("Obese")
    else:
      print("Enter Valid Details")
          





botname('Sanji')
username()
guess_num()
test()
end()
end_time=time.time()
print(f"Hola! We talked for {end_time-start_time:.3f} seconds")
creator()
bmi()
 
    