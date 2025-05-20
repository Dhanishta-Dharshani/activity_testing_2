# General instructions
# time in am/pm

#productive time
#study
#exercise
#errands
def intro_productive_time():
  print("Which productive activity would you like to do today?")
  print("1. Study")
  print("2. Exercise")
  print("3. Errands")
  print()

def instructions_productive_time():  
  print("Instructions :-")
  print("1. Maximum number of subjects / exercises / errands allowed is 5")
  print("2. Please arrange the activities based on your preference starting from the most preferred to the least preferred")
  print()

def productive_time():  
  if p=='1' or p=="Study" or p=="study":
    h=int(input("Enter the number of minutes you would like to study for: "))
    s=int(input("Enter the number of subjects you would like to study: "))
    if s==1:
        s1=input("Enter subject 1: ")
        print("The amount of time dedicated for",s1,"is",h,"minutes")
    if s==2:
        s1=input("Enter subject 1: ")
        s2=input("Enter subject 2: ")
        times1=70*h//100
        times2=30*h//100
        print("The amount of time dedicated for",s1,"is",times1,"minutes")
        print("The amount of time dedicated for",s2,"is",times2,"minutes")
    if s==3:
        s1=input("Enter subject 1: ")
        s2=input("Enter subject 2: ")
        s3=input("Enter subject 3: ")
        times1=45*h//100
        times2=30*h//100
        times3=25*h//100
        print("The amount of time dedicated for",s1,"is",times1,"minutes")
        print("The amount of time dedicated for",s2,"is",times2,"minutes")
        print("The amount of time dedicated for",s3,"is",times3,"minutes")
    if s==4:
        s1=input("Enter subject 1: ")
        s2=input("Enter subject 2: ")
        s3=input("Enter subject 3: ")
        s4=input("Enter subject 4: ")
        times1=35*h//100
        times2=30*h//100
        times3=20*h//100
        times4=15*h//100
        print("The amount of time dedicated for",s1,"is",times1,"minutes")
        print("The amount of time dedicated for",s2,"is",times2,"minutes")
        print("The amount of time dedicated for",s3,"is",times3,"minutes")
        print("The amount of time dedicated for",s4,"is",times4,"minutes")
    if s==5:
        s1=input("Enter subject 1: ")
        s2=input("Enter subject 2: ")
        s3=input("Enter subject 3: ")
        s4=input("Enter subject 4: ")
        s5=input("Enter subject 5: ")
        times1=30*h//100
        times2=25*h//100
        times3=20*h//100
        times4=15*h//100
        times5=10*h//100
        print("The amount of time dedicated for",s1,"is",times1,"minutes")
        print("The amount of time dedicated for",s2,"is",times2,"minutes")
        print("The amount of time dedicated for",s3,"is",times3,"minutes")
        print("The amount of time dedicated for",s4,"is",times4,"minutes")
        print("The amount of time dedicated for",s5,"is",times5,"minutes")
    if s>5:
        print("ERROR! Only a maximum of 5 subjects is allowed. Please try again! ")
        
  if p=='2' or p=="exercise" or p=="Exercise":
    h=int(input("Enter the number of minutes you would like to exercise for: "))
    s=int(input("Enter the number of exercises you would like to do today: "))
    if s==1:
        s1=input("Enter exercise 1: ")
        print("The amount of time dedicated for",s1,"is",h,"minutes")
    if s==2:
        s1=input("Enter exercise 1: ")
        s2=input("Enter exercise 2: ")
        times1=70*h//100
        times2=30*h//100
        print("The amount of time dedicated for",s1,"is",times1,"minutes")
        print("The amount of time dedicated for",s2,"is",times2,"minutes")
    if s==3:
        s1=input("Enter exercise 1: ")
        s2=input("Enter exercise 2: ")
        s3=input("Enter exercise 3: ")
        times1=45*h//100
        times2=30*h//100
        times3=25*h//100
        print("The amount of time dedicated for",s1,"is",times1,"minutes")
        print("The amount of time dedicated for",s2,"is",times2,"minutes")
        print("The amount of time dedicated for",s3,"is",times3,"minutes")
    if s==4:
        s1=input("Enter exercise 1: ")
        s2=input("Enter exercise 2: ")
        s3=input("Enter exercise 3: ")
        s4=input("Enter exercise 4: ")
        times1=35*h//100
        times2=30*h//100
        times3=20*h//100
        times4=15*h//100
        print("The amount of time dedicated for",s1,"is",times1,"minutes")
        print("The amount of time dedicated for",s2,"is",times2,"minutes")
        print("The amount of time dedicated for",s3,"is",times3,"minutes")
        print("The amount of time dedicated for",s4,"is",times4,"minutes")
    if s==5:
        s1=input("Enter exercise 1: ")
        s2=input("Enter exercise 2: ")
        s3=input("Enter exercise 3: ")
        s4=input("Enter exercise 4: ")
        s5=input("Enter exercise 5: ")
        times1=30*h//100
        times2=25*h//100
        times3=20*h//100
        times4=15*h//100
        times5=10*h//100
        print("The amount of time dedicated for",s1,"is",times1,"minutes")
        print("The amount of time dedicated for",s2,"is",times2,"minutes")
        print("The amount of time dedicated for",s3,"is",times3,"minutes")
        print("The amount of time dedicated for",s4,"is",times4,"minutes")
        print("The amount of time dedicated for",s5,"is",times5,"minutes")
    if s>5:
        print("ERROR! Only a maximum of 5 subjects is allowed. Please try again! ")
        
  if p=='3' or p=="errand":
    h=int(input("Enter the number of minutes you would like to do errands for: "))
    s=int(input("Enter the number of errands you would like to do today: "))
    if s==1:
        s1=input("Enter errand 1: ")
        print("The amount of time dedicated for",s1,"is",h,"minutes")
    if s==2:
        s1=input("Enter errand 1: ")
        s2=input("Enter errand 2: ")
        times1=70*h//100
        times2=30*h//100
        print("The amount of time dedicated for",s1,"is",times1,"minutes")
        print("The amount of time dedicated for",s2,"is",times2,"minutes")
    if s==3:
        s1=input("Enter errand 1: ")
        s2=input("Enter errand 2: ")
        s3=input("Enter errand 3: ")
        times1=45*h//100
        times2=30*h//100
        times3=25*h//100
        print("The amount of time dedicated for",s1,"is",times1,"minutes")
        print("The amount of time dedicated for",s2,"is",times2,"minutes")
        print("The amount of time dedicated for",s3,"is",times3,"minutes")
    if s==4:
        s1=input("Enter errand 1: ")
        s2=input("Enter errand 2: ")
        s3=input("Enter errand 3: ")
        s4=input("Enter errand 4: ")
        times1=35*h//100
        times2=30*h//100
        times3=20*h//100
        times4=15*h//100
        print("The amount of time dedicated for",s1,"is",times1,"minutes")
        print("The amount of time dedicated for",s2,"is",times2,"minutes")
        print("The amount of time dedicated for",s3,"is",times3,"minutes")
        print("The amount of time dedicated for",s4,"is",times4,"minutes")
    if s==5:
        s1=input("Enter errand 1: ")
        s2=input("Enter errand 2: ")
        s3=input("Enter errand 3: ")
        s4=input("Enter errand 4: ")
        s5=input("Enter errand 5: ")
        times1=30*h//100
        times2=25*h//100
        times3=20*h//100
        times4=15*h//100
        times5=10*h//100
        print("The amount of time dedicated for",s1,"is",times1,"minutes")
        print("The amount of time dedicated for",s2,"is",times2,"minutes")
        print("The amount of time dedicated for",s3,"is",times3,"minutes")
        print("The amount of time dedicated for",s4,"is",times4,"minutes")
        print("The amount of time dedicated for",s5,"is",times5,"minutes")
    if s>5:
        print("ERROR! Only a maximum of 5 subjects is allowed. Please try again! ") 
  if p not in ('Study','study','errands','Errands','exercise','Exercise', '1', '2', '3'):
      print("ERROR! Please choose only one of the given 3 activities")


# relaxation time
# hobbies
# gadget time
# sleep time
def intro_relaxation_time():
  print("What type of relaxation would you like to do today?")
  print("1. Hobbies")
  print("2. Gadgets")
  print()

def instructions_relaxation_time():
  print("Instructions :-")
  print("1. The maximum number of activities allowed is 5")
  print("2. Please arrange your activities based on your preference starting from the most preferred to the least preferred")
  print()

def relaxation_time():
  if p=='1' or p=="hobbies" or p=="Hobbies":
    h=int(input("Enter the number of minutes you would like to spend for hobbies: "))
    s=int(input("Enter the number of hobbies you would like to do: "))
    if s==1:
        s1=input("Enter hobby 1: ")
        print("The amount of time dedicated for",s1,"is",h,"minutes")
    if s==2:
        s1=input("Enter hobby 1: ")
        s2=input("Enter hobby 2: ")
        times1=70*h//100
        times2=30*h//100
        print("The amount of time dedicated for",s1,"is",times1,"minutes")
        print("The amount of time dedicated for",s2,"is",times2,"minutes")
    if s==3:
        s1=input("Enter hobby 1: ")
        s2=input("Enter hobby 2: ")
        s3=input("Enter hobby 3: ")
        times1=45*h//100
        times2=30*h//100
        times3=25*h//100
        print("The amount of time dedicated for",s1,"is",times1,"minutes")
        print("The amount of time dedicated for",s2,"is",times2,"minutes")
        print("The amount of time dedicated for",s3,"is",times3,"minutes")
    if s==4:
        s1=input("Enter hobby 1: ")
        s2=input("Enter hobby 2: ")
        s3=input("Enter hobby 3: ")
        s4=input("Enter hobby 4: ")
        times1=35*h//100
        times2=30*h//100
        times3=20*h//100
        times4=15*h//100
        print("The amount of time dedicated for",s1,"is",times1,"minutes")
        print("The amount of time dedicated for",s2,"is",times2,"minutes")
        print("The amount of time dedicated for",s3,"is",times3,"minutes")
        print("The amount of time dedicated for",s4,"is",times4,"minutes")
    if s==5:
        s1=input("Enter hobby 1: ")
        s2=input("Enter hobby 2: ")
        s3=input("Enter hobby 3: ")
        s4=input("Enter hobby 4: ")
        s5=input("Enter hobby 5: ")
        times1=30*h//100
        times2=25*h//100
        times3=20*h//100
        times4=15*h//100
        times5=10*h//100
        print("The amount of time dedicated for",s1,"is",times1,"minutes")
        print("The amount of time dedicated for",s2,"is",times2,"minutes")
        print("The amount of time dedicated for",s3,"is",times3,"minutes")
        print("The amount of time dedicated for",s4,"is",times4,"minutes")
        print("The amount of time dedicated for",s5,"is",times5,"minutes")
    if s>5:
        print("ERROR! Only a maximum of 5 subjects is allowed. Please try again! ")
        
  if p=='2' or p=="gadgets" or p=="Gadgets":
    h=int(input("Enter the number of minutes you would like to use gadgets for: "))
    s=int(input("Enter the number of gadgets that you would like to use today: "))
    if s==1:
        s1=input("Enter gadget 1: ")
        print("The amount of time dedicated for",s1,"is",h,"minutes")
    if s==2:
        s1=input("Enter gadget 1: ")
        s2=input("Enter gadget 2: ")
        times1=70*h//100
        times2=30*h//100
        print("The amount of time dedicated for",s1,"is",times1,"minutes")
        print("The amount of time dedicated for",s2,"is",times2,"minutes")
    if s==3:
        s1=input("Enter gadget 1: ")
        s2=input("Enter gadget 2: ")
        s3=input("Enter gadget 3: ")
        times1=45*h//100
        times2=30*h//100
        times3=25*h//100
        print("The amount of time dedicated for",s1,"is",times1,"minutes")
        print("The amount of time dedicated for",s2,"is",times2,"minutes")
        print("The amount of time dedicated for",s3,"is",times3,"minutes")
    if s==4:
        s1=input("Enter gadget 1: ")
        s2=input("Enter gadget 2: ")
        s3=input("Enter gadget 3: ")
        s4=input("Enter gadget 4: ")
        times1=35*h//100
        times2=30*h//100
        times3=20*h//100
        times4=15*h//100
        print("The amount of time dedicated for",s1,"is",times1,"minutes")
        print("The amount of time dedicated for",s2,"is",times2,"minutes")
        print("The amount of time dedicated for",s3,"is",times3,"minutes")
        print("The amount of time dedicated for",s4,"is",times4,"minutes")
    if s==5:
        s1=input("Enter gadget 1: ")
        s2=input("Enter gadget 2: ")
        s3=input("Enter gadget 3: ")
        s4=input("Enter gadget 4: ")
        s5=input("Enter gadget 5: ")
        times1=30*h//100
        times2=25*h//100
        times3=20*h//100
        times4=15*h//100
        times5=10*h//100
        print("The amount of time dedicated for",s1,"is",times1,"minutes")
        print("The amount of time dedicated for",s2,"is",times2,"minutes")
        print("The amount of time dedicated for",s3,"is",times3,"minutes")
        print("The amount of time dedicated for",s4,"is",times4,"minutes")
        print("The amount of time dedicated for",s5,"is",times5,"minutes")
    if s>5:
        print("ERROR! Only a maximum of 5 exercises is allowed. Please try again!")
  if p not in ('Hobbies','hobbies','Gadgets','gadgets','1', '2'):
      print("ERROR! Please choose only one of the given 2 activities")

# productive time execution
intro_productive_time()
instructions_productive_time()
p=input("Choose the productive activity that you would like to do today from the above: ")
productive_time()
ptime=1
while ptime<3:
  pro_time=input('Would you like to perform another productive activity for the day?\nPlease enter Yes / No: ')
  if pro_time in 'Yesyes':
    p=input("Choose the productive activity that you would like to do today from the above: ")
    productive_time()
    ptime=ptime+1
    break
  else:
    break
print()


# self_care time
# skin care
# hair care
# journalling

# Simple Self-Care Time Allocator with Ratio Options
print("=== Self-Care Time Allocator ===")
print("\nChoose your preferred time distribution:")
print("1. Balanced (Hair:Skin:Journal = 1:1:1)")
print("2. Skin Focus (Hair:Skin:Journal = 1:2:1)")
print("3. Hair Focus (Hair:Skin:Journal = 2:1:1)")
print("4. Journal Focus (Hair:Skin:Journal = 1:1:2)")
print("5. Intensive Care (Hair:Skin:Journal = 1:3:1)")

# Switch-case using dictionary mapping
ratio_choices = {'1': (1, 1, 1), '2': (1, 2, 1), '3': (2, 1, 1), '4': (1, 1, 2), '5': (1, 3, 1)}

# Get user's ratio choice
while True:
  choice = input("\nEnter your choice (1-5): ")
  if choice in ratio_choices:
    hair_ratio, skin_ratio, journal_ratio = ratio_choices[choice]
    break
  else:
    print("Invalid choice. Please enter 1-5.")

# Get total available time
while True:
  try:
    total_time = int(input("Enter total minutes available: "))
    if total_time > 0:
      break
    else:
      print("Please enter a positive number.")
  except ValueError:
    print("Please enter a whole number (e.g., 30, 60).")
    
# Calculate time allocation
total_ratio = hair_ratio + skin_ratio + journal_ratio
hair_time = (total_time * hair_ratio) // total_ratio
skin_time = (total_time * skin_ratio) // total_ratio
journal_time = total_time - hair_time - skin_time

# Display results
print("\n=== Recommended Time Allocation ===")
print(f"Hair Care: {hair_time} minutes")
print(f"Skin Care: {skin_time} minutes")
print(f"Journaling: {journal_time} minutes")
print(f"\nTotal: {hair_time + skin_time + journal_time} minutes")


# relaxation time execution
intro_relaxation_time()
instructions_relaxation_time()
p=input("Choose the relaxation activity that you would like to do today from the above: ")
relaxation_time()
rtime=1
while rtime<2:
  rel_time=input('Would you like to perform another productive activity for the day?\nPlease enter Yes / No: ')
  if rel_time in 'Yesyes':
    p=input("Choose the relaxation activity that you would like to do today from the above: ")
    relaxation_time()
    rtime=rtime+1
    break
  else:
    break
print()

print("'Sleep is the best meditation.' said Dalai Lama")
print('Hence, we must sleep for 8 hours to live a healthy and happy life!')
