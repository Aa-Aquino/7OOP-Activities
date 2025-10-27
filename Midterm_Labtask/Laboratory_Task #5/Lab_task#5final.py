#LAB_Task#5

class User:
    def __init__(self, first_name, last_name, followers_count, friends_name):
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        self.followers_count = followers_count
        self.friends_name = [f.capitalize() for f in friends_name]

    def introduce_self(self):
        print(f"Hi I am {self.first_name} {self.last_name}")

    def view_full_profile(self):
        print(f"Profile Name is: {self.first_name} {self.last_name} with {self.followers_count} followers")
        print(f"Your friends are:  {', '.join(self.friends_name)}")
        print()
        print()


class TestUser:
    def __init__(self):
        self.users = []

    def add_user(self):
        while True:
            ans = input("Insert a Record?[y|n]: ").lower()
            if ans == "n":
                break
            elif ans == "y":
                fname = input("First Name: ")
                lname = input("Last Name: ")
                followers = int(input("Followers: "))
                print("Friends:")
                friends = []
                for i in range(3):
                    friend = input()
                    friends.append(friend)
                user = User(fname, lname, followers, friends)
                self.users.append(user)
            else:
                print("Please enter only y or n")

    def show_users(self):
        print()
        print("Here are the Records....")
        print()
        for user in self.users:
            user.introduce_self()
            user.view_full_profile()
        print(f"There are currently {len(self.users)} Members in the Social Media page")


#RUN PROGRAM
test = TestUser()
test.add_user()
test.show_users()
