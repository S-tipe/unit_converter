
print("Ovo je program koji pretvara kilometre u milje.")

while True:
    print("Molim te unesite broj kilometara koje želite pretvoriti u milje. Unesi samo broj!")

    km = input("Kilometers: ")

    km = float(km.replace(",", "."))  # zamjeni zarez sa točkom

    miles = km * 0.621371

    print("{0} kilometers is {1} miles.".format(km, miles))

    choice = input("Da li želiš ponoviti konverzaciju (y/n): ")

    if choice.lower() != "y" and choice.lower() != "yes":
        break