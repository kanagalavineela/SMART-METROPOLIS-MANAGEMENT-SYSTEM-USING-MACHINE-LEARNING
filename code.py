import hashlib
import pandas as pd
from sklearn.neighbors import NearestNeighbors
import numpy as np

# Simulated user database
shops_data = {
    'name': ['Shop 1', 'Shop 2', 'Shop 3', 'Shop 4', 'Shop 5'],
    'category': [1, 2, 3, 1, 2],
    'location': ['Location A', 'Location B', 'Location C', 'Location A', 'Location B'],
    'rating': [4.5, 4.2, 4.7, 4.3, 4.6],
}

shops_df = pd.DataFrame(shops_data)

def shop():
    print("1.MEN")
    print("2.WOMEN")
    print("3.KIDS")
    n=int(input("enter option: "))
    
    # Create a feature array for the user input
    user_input = np.array([n])
    
    # Create a Nearest Neighbors model
    nn = NearestNeighbors(n_neighbors=1, algorithm='ball_tree')
    nn.fit(shops_df[['category']])
    
    # Get the nearest neighbor (shop/mall) to the user's input
    distances, indices = nn.kneighbors(user_input.reshape(1, -1))
    
    # Get the index of the best match
    best_match_index = indices[0][0]
    
    # Print the suggested shop/mall
    print(f"Best match: {shops_df.iloc[best_match_index]['name']} (Category: {shops_df.iloc[best_match_index]['category']}, Location: {shops_df.iloc[best_match_index]['location']}, Rating: {shops_df.iloc[best_match_index]['rating']})")


users = {}
hotel_data = [
    ["Hotel A", 1, 1, 1, 1, 4.5],
    ["Hotel B", 1, 0, 1, 1, 4.2],
    ["Hotel C", 0, 1, 1, 0, 3.8],
    ["Hotel D", 1, 1, 0, 1, 4.0],
    ["Hotel E", 0, 0, 1, 1, 3.5],
    ["Hotel F", 1, 1, 1, 0, 4.3],
    ["Hotel G", 0, 1, 0, 1, 3.7],
    ["Hotel H", 1, 0, 0, 1, 3.9],
    ["Hotel I", 0, 0, 0, 0, 3.0],
    ["Hotel J", 1, 1, 1, 1, 4.7],
    ["Hotel K", 1, 0, 1, 0, 4.1],
    ["Hotel L", 0, 1, 1, 1, 3.6],
]

# Create a pandas DataFrame from the hotel data
df = pd.DataFrame(hotel_data, columns=["hotel_names", "Wi-Fi", "Parking", "Gym", "Pool", "Rating"])

# Simulated hospital database with treatment options and hospital names
hospital_data = {
    "treatment_options": [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4],
    "hospital_names": [
        "Hospital A",
        "Hospital B",
        "Hospital C",
        "Hospital D",
        "Hospital E",
        "Hospital F",
        "Hospital G",
        "Hospital H",
        "Hospital I",
        "Hospital J",
        "Hospital K",
        "Hospital L",
    ],
}
def recommend_hotel():
    """
    Recommends a hotel based on the user's preferences using a KNN algorithm.
    """
    # Get the user's preferences
    preferences = []
    print("Please rate the following options (0=dislike, 1=like):")
    print("- Wi-Fi:", end=" ")
    preferences.append(int(input()))
    print("- Parking:", end=" ")
    preferences.append(int(input()))
    print("- Gym:", end=" ")
    preferences.append(int(input()))
    print("- Pool:", end=" ")
    preferences.append(int(input()))

    # Fit a KNN model to the DataFrame
    knn = NearestNeighbors(n_neighbors=1)
    knn.fit(df[["Wi-Fi", "Parking", "Gym", "Pool"]])

    # Find the nearest hotel based on the user's preferences
    distances, indices = knn.kneighbors([preferences])

    # Print the recommended hotel
    print("Recommended hotel: " + df["hotel_names"][indices[0][0]])



def trans():
    print("1. Public")
    print("2. Private")
    tr=int(input("enter option"))
    if tr==1:
        print("1.Bus")
        print("2.Local train/metro")
    else:
        print("book cab/auto/bike")

def hos():
    print("select treatment")
    print("1.General treatment")
    print("2.Cardiac treatment")
    print("3.Orthopedic")
    print("4.ENT")
    op=int(input("enter option"))
    return op



def book_hotel():
    """
    Allows the user to book a hotel by asking for the hotel name, check-in date, and check-out date.
    """
    # Ask for hotel name, check-in date, and check-out date
    hotel_name = input("Enter hotel name: ")
    check_in_date = input("Enter check-in date (YYYY-MM-DD): ")
    check_out_date = input("Enter check-out date (YYYY-MM-DD): ")

    # Print confirmation
    print("Hotel booked successfully!")
    print("Hotel: " + hotel_name)
    print("Check-in date: " + check_in_date)
    print("Check-out date: " + check_out_date)

def hash_password(password):
    """
    Hashes a password using the SHA256 algorithm.
    """
    return hashlib.sha256(password.encode()).hexdigest()

def register():
    """
    Registers a new user by asking for a username and password and storing the hashed password in the user database.
    """
    username = input("Enter a username: ")

    if username in users:
        print("Username already exists. Please choose another username.")
        return

    password = input("Enter a password: ")
    users[username] = hash_password(password)
    print("Registration successful!")

def login():
    """
    Logs in a user by asking for a username and password and checking if the hashed password matches the one in the user database.
    """
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username not in users:
        print("Invalid username or password.")
        return

    if users[username] != hash_password(password):
        print("Invalid username or password.")
        return

    print("Login successful!")
    # Call main_menu() after successful login
    main_menu()

def main_menu():
    cityname=input("Enter city name:")

    """
    Displays the main menu and allows the user to book a hotel, view city information, or logout.
    """
    while True:
        print("Main Menu:")
        print("1. View City Information")
        print("2. Purpose")
        print("3. Logout")
        choice = int(input("Enter your choice: "))

        if choice == 2:
            purpose()
        elif choice == 1:
            view_city_information()
        elif choice == 3:
            print("Logging out...")
            break
        else:
            print("Invalid choice!")

def view_city_information():
    """
    Displays city information.
    """
    print("City information:")
    print("- Places of interest")
    print("- Tourist attractions")
    print("- Educational institutions")
    # Add more city information here

def purpose():
    while True:
        print("1. Hotel booking")
        print("2. Hotel Recommendation system")
        print("3. Shopping")
        print("4. Medical treatment")
        print("5. Transportation")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            book_hotel()
        elif choice == 2:
            recommend_hotel()
        elif choice == 3:
            shop()
        elif choice == 4:
            recommend_hospital()
        elif choice == 5:
            trans()
        elif choice == 6:
            print("Logging out...")
            break
        else:
            print("Invalid choice!")

def recommend_hospital():
    """
    Recommends a hospital based on the user's selected treatment option using a KNN algorithm.
    """
    # Load hospital data into a pandas DataFrame
    df = pd.DataFrame(hospital_data)

    # Fit a KNN model to the DataFrame
    knn = NearestNeighbors(n_neighbors=1)
    knn.fit(df[["treatment_options"]])

    # Get the user's selected treatment option
    treatment_option = hos()

    # Find the nearest hospital based on the user's selected treatment option
    distances, indices = knn.kneighbors([[treatment_option]])

    # Print the recommended hospital
    print("Recommended hospital: " + df["hospital_names"][indices[0][0]])

def main():
    """
    The main function of the program.
    """
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            register()
        elif choice == 2:
            login()
        elif choice == 3:
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()


