# Exercise 2

# Satellites:
sat_database = {"METEOSAT" : 3000,
                "LANDSAT"  : 30,
                "MODIS"    : 500
               }

# The dictionary above contains the names and spatial resolutions of some satellite systems.

# 1) Add the "GOES" and "worldview" satellites with their 2000/0.31m resolution to the dictionary [2P]

sat_database["GOES"]=2000
sat_database["worldview"]=0.31

# 2) print out all satellite names contained in the dictionary [2P]

print("I have the following satellites in my database:","\n",sat_database.keys())

# 3) Ask the user to enter the satellite name from which she/he would like to know the resolution [2P]

print("I have the following satellites in my database:","\n",sat_database.keys())
answer=input("From which satellite do you wish to get the resolution?")
answer=answer.upper()
    
# 4) Check, if the satellite is in the database and inform the user, if it is not [2P]

if answer == "METEOSAT":
    print("The satellite METEOSAT is in the database")
elif answer == "LANDSAT":
    print(" The satellite LANDSAT is in the database")
elif answer == "MODIS":
    print("The satellite MODIS is in the database")
elif answer== "GOES":
    print("The satellite GOES is in the database.")
elif answer == "WORLDVIEW":#how do I get a case "unsensitive" search for values?!?
    print("The satellite worldview is in the database.")
else:
    print("Your satellite","\"", answer,"\"", "is not in the database.")
    
# 5) If the satellite name is in the database, print a meaningful message containing the satellite name and it's resolution [2P] 

if answer == "METEOSAT":
    print("The satellite METEOSAT has the following resolution:",sat_database[answer],".")
elif answer == "LANDSAT":
    print("The satellite LANDSAT has the following resolution:",sat_database.get(answer),".")
elif answer == "MODIS":
    print("The satellite MODIS has the following resolution:",sat_database["MODIS"],".")
elif answer == "GOES":
    print("The satellite GOES has the following resolution:",sat_database.get("GOES"),".")
elif answer == "WORLDVIEV":#again the question, is it possible to do it like upper(worldview)?
    print("The satellite worldview has the following resolution: 0.31m")