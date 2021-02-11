#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
#for county, voters in counties_dict.items():
    #print(f"{county} county has {voters:,.0f} registered voters.")
voting_data = [''{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
for county, registered_voters in voting_data.items():
        print(f"{county} county has {voters:,.0f} registered voters.")
