import json
import random

# Function to generate random age and email
def generate_random_data(first_name, last_name):
    age = random.randint(20, 60)
    email = f"{first_name.lower()}.{last_name.lower()}@example.com"
    return age, email

# List of first names and last names for generating random data
first_names = ["Ryan", "John", "Jane", "Emily", "Michael", "Sarah", "David", "Laura", "Robert", "Linda", "Rick", "Bob", "Alice", "Tom", "Jerry", "Peter", "Paul",
                "Mary", "Sue", "Chris", "Alex", "Sam", "Kate", "Emma", "Olivia", "Sophia", "Ava", "Isabella", "Mia", "Amelia", "Harper", "Evelyn", "Abigail", "Emily",
                  "Elizabeth", "Sofia", "Ella", "Madison", "Scarlett", "Victoria", "Aria", "Grace", "Chloe", "Camila", "Penelope", "Riley", "Layla", "Lillian", "Nora", "Zoey"]

last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", 
              "Taylor", "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", "Walker", "Young",
              "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores", "Green", "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell", "Carter"]


first_names_2 = ["Jack", "Sophie", "Oliver", "Ruby", "Mia", "Jacob", "Ella", "William", "Chloe", "James", "Emily", "Amelia", "Thomas", "Lily", "Isabella", "Charlie",
                  "Grace", "Lucas", "Harper", "Ethan", "Sophia", "Alexander", "Ava", "Henry", "Zoe", "Samuel", "Scarlett", "Max", "Evie", "Daniel", "Maddison", "Oscar",
                  "Sienna", "Lachlan", "Matilda", "Cooper", "Ruby", "Benjamin", "Eva", "Liam", "Charlotte", "Mason", "Isabelle", "Harrison", "Olivia", "Archie", "Isla", "Leo"]

last_names_2 = ["Brown", "Smith", "Patel", "Jones", "Williams", "Johnson", "Taylor", "Thomas", "Roberts", "Khan", "Lewis", "Jackson", "Clarke", "James", "Phillips", "Wilson",
                "Ali", "Mason", "Mitchell", "Rose", "Davis", "Davies", "Rodriguez", "Cox", "Alexander", "Mills", "Hill", "Scott", "Green", "Adams", "Baker", "Hall", "Rivera",
                "Campbell", "Mitchell", "Carter", "Young", "Allen", "King", "Wright", "Torres", "Nguyen", "Flores", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson"]


# Generate 50 entries
data_list = []
for _ in range(50):
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    age, email = generate_random_data(first_name, last_name)
    data_list.append({
        "firstName": first_name,
        "lastName": last_name,
        "age": age,
        "email": email
    })

# Write the data to a JSON file
with open('sample_data_50_entries.json', 'w') as f:
    json.dump(data_list, f, indent=4)

print("Sample JSON file 'sample_data_50_entries.json' with 50 entries created successfully.")


data_list = []
for _ in range(50):
    first_name = random.choice(first_names_2)
    last_name = random.choice(last_names_2)
    age, email = generate_random_data(first_name, last_name)
    data_list.append({
        "firstName": first_name,
        "lastName": last_name,
        "age": age,
        "email": email
    })

# Write the data to a JSON file
with open('sample_data_50_entries_second_upload.json', 'w') as f:
    json.dump(data_list, f, indent=4)

print("Sample JSON file 'sample_data_50_entries_second_upload.json' with 50 entries created successfully.")