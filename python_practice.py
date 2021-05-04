print("Hello World")
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

if "El Paso" in counties:
    print("el paso is in list of counties")
else:
    print("el paso not in list")

for county in counties:
    print(county)

for i in range(len(counties)):
    print(counties[i])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
#All Prints keys
for county in counties_dict:
    print(county)
for county in counties_dict.keys():
    print(county)
#prints values
for voters in counties_dict.values():
    print(voters)
for county in counties_dict:
    print(counties_dict[county])
for county in counties_dict:
    print(counties_dict.get(county))
#prints both
for county, voters in counties_dict.items():
    print(county, voters)

#printing with concatenation
for county, voters in counties_dict.items():
     print(county + " county has " + str(voters) + " registered voters.")   

#printing with f string
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

#list of dictionaries
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

#values only from list of dictionaries
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

#only shows registered voters values, because registered voters is the key
for county_dict in voting_data:
     print(county_dict['registered_voters'])

#inputs
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")

#inputs with fstring
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

#multiline fstring message with number fomatting-add commas and limit decimals of percent
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)

# If else loop
temperature = int(input("what is the temperature outside?"))

if temperature > 80:
    print("turn on the AC")

else:
    print("open the window")

 # What is the score?
score = int(input("What is your test score? "))

# If ElseIf ElseIf Else Loop to Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')

x=0
while x <= 5:
    print(x)
    x=x+1