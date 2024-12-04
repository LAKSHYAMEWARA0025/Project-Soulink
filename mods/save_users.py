from os import path, remove, rename
from colorama import Fore
from pickle import dump, load
import colorama

colorama.init(autoreset=True)

class User():
    def __init__(self):
        pass

    def load_users_file(self):
        if not path.exists("mods/data/users.txt"): self.file_obj = open("mods/data/users.txt", "w")
        else: self.file_obj = open("mods/data/users.txt", "a")

    def write_users(self, user_data: list[str]):
        self.load_users_file()
        self.file_obj.writelines(user_data)
        self.file_obj.write("\n")
        self.file_obj.close()

    def read_files(self) -> list[dict[str: str]] | bool:

        if path.exists("mods/data/users.txt"): self.file_obj = open("mods/data/users.txt", "r")
        else: return False
        users: list = self.file_obj.readlines()
        self.file_obj.close()
        return users

    def delete_users(self, username:str):
        users = self.read_files()

        for user in users:
            if user[0] != username:
                self.write_users(user)
        
    def count_users(self) -> int:
        users = self.read_files()
        return len(users)

    def check_user(self, username: str, mail: str = "") -> bool | str:
        users = self.read_files()

        if not users: return "error"

        for (user) in users:
            if user.split()[0] == username:
                return "username"
            elif user.split()[1] == mail:
                return "mail"
        
        return False
    
    def save_psswrd(self, username: str, password: str) -> None:

        if path.exists("mods/data/passwords.dat"): self.file_obj = open("mods/data/passwords.dat", "ab")
        else: self.file_obj = open("mods/data/passwords.dat", "wb")

        encoded_data = {"username": username, "password": password.encode('utf-8')}

        dump(encoded_data, self.file_obj)
        self.file_obj.close()
    
    def get_psswrd(self) -> bool | list[dict[str: str]]:
        if path.exists("mods/data/passwords.dat"): self.file_obj = open("mods/data/passwords.dat", "rb")
        else: return False

        users_list: list[dict[str: str]] = []

        while True:
            try: 
                data = load(self.file_obj)
                #print(data)
                data["password"] = data["password"].decode('utf-8')
                users_list.append(data)
            
            except EOFError:
                self.file_obj.close()
                return users_list

    def count_userPsswrd(self) -> int | bool:
        user_list = self.get_psswrd()

        if user_list: return len(user_list)
        else: False

    def delete_psswrd(self, username: str) -> bool:
        if path.exists("mods/data/passwords.dat"): self.file_obj = open("mods/data/passwords.dat", "rb")
        else: return False

        dup_fileObj = open("mods/data/temp.dat", "wb")

        while True:
            try:
                data = load(self.file_obj)
                if data["username"] != username:
                    dump(data, dup_fileObj)
            except EOFError:
                self.file_obj.close()
                dup_fileObj.close()

                remove("mods/data/passwords.dat")
                rename("mods/data/temp.dat", "mods/data/passwords.dat")
                return True

    def change_psswrd(self, username: str, new_password: str) -> bool:
        if path.exists("mods/data/passwords.dat"): self.file_obj = open("mods/data/passwords.dat", "rb+")
        else: return False

        while True:
            try:
                pos = self.file_obj.tell()
                data = load(self.file_obj)
                if data["username"] == username:
                    data["password"] = new_password.encode('utf-8')
                    self.file_obj.seek(pos)
                    dump(data, self.file_obj)

                    return True
                
            except EOFError:
                self.file_obj.close()
                return True


def main(is_textFile: bool) -> None:

    if is_textFile:
        while True:
            print(f"{Fore.LIGHTYELLOW_EX}1. Add user\n2. View all users\n3. Count Users\n4. Delete user\n5. Exit\n")
            user_input: int = int(input(f"{Fore.GREEN}Enter Your Choice: {Fore.WHITE}"))
            
            if user_input == 1:
                username: str = input(f"{Fore.GREEN}Username: {Fore.WHITE}")
                mail: str = input(f"{Fore.GREEN}mail: {Fore.WHITE}")
                users.write_users([username + " ", mail])

                print(f"\n{Fore.YELLOW}New User Registered !\n")

            elif user_input == 2:
                users_list = users.read_files()
                if users_list == "File doesn't exist !":
                    print(f"\n{Fore.RED}{users_list}\n")
                    continue
                count: int = 1
                for user in users_list:
                    print(f"{Fore.LIGHTBLACK_EX}{count}: {Fore.GREEN}{user.split()[0]}")
                    count += 1
                
                print("\n")

            elif user_input == 3:
                print(f"\n{Fore.GREEN}Current Users: {Fore.LIGHTBLACK_EX}{users.count_users()}\n")

            elif user_input == 4:
                username: str = input(f"{Fore.GREEN}Username: {Fore.WHITE}")
                mail: str = input(f"{Fore.GREEN}mail: {Fore.WHITE}")
                users.delete_users()

                print(f"\n{Fore.GREEN}User deleted successfully\n")

            elif user_input == 5:
                break
    
    else:
        while True:
            print(f"{Fore.LIGHTYELLOW_EX}1. Add user password\n2. View all users\n3. Count Users\n4. Delete user password\n5. Change user password\n6.Exit\n")
            try: user_input: int = int(input(f"{Fore.GREEN}Enter Your Choice: {Fore.WHITE}"))
            except ValueError:
                print(f"\n{Fore.RED}Invalid Option\n")
                continue
            
            if user_input == 1:
                username: str = input(f"{Fore.GREEN}Username: {Fore.WHITE}")
                password: str = input(f"{Fore.GREEN}password: {Fore.WHITE}")
                users.save_psswrd(username, password)

                print(f"\n{Fore.LIGHTGREEN_EX}New User Registered !\n")

            elif user_input == 2:
                show_passwrd: str = input(f"{Fore.GREEN}Show Passwords (y/n): {Fore.WHITE}").lower()
                users_list: list[dict[str: str]] = users.get_psswrd()
                if not users_list:
                    print(f"{Fore.RED}Error while reading users files !\n")
                    continue
                
                count: int = 1
                pwd: str = "********"
                print("\n")
                for user in users_list:
                    if show_passwrd == "y":
                        pwd = user["password"]
                    print(f"{Fore.LIGHTBLACK_EX}{count}: {Fore.GREEN}{user['username']} <{pwd}>")
                    count += 1
                
                print("\n")

            elif user_input == 3:
                user_count = users.count_userPsswrd()
                if user_count: print(f"\n{Fore.GREEN}Current Users: {Fore.LIGHTBLACK_EX}{user_count}\n")
                else: print(f"{Fore.RED}Error while retrieving users !\n")

            elif user_input == 4:
                username: str = input(f"{Fore.GREEN}Username: {Fore.WHITE}")
                status: bool = users.delete_psswrd(username)

                if status: print(f"\n{Fore.GREEN}User deleted successfully\n")
                else: print(f"{Fore.RED}Error while deletion !\n")

            elif user_input == 5:
                username: str = input( f"{Fore.GREEN}Username: {Fore.WHITE}")
                password: str = input(f"{Fore.GREEN}new password: {Fore.WHITE}")

                status: bool = users.change_psswrd(username, password)

                if status: print(f"\n{Fore.GREEN}Password changed successfully\n")
                else: print(f"{Fore.RED}Error while changing password !\n")
            
            elif user_input == 6:
                break

if __name__ == "__main__":
    users = User()

    main(False)
    print(f"{Fore.YELLOW}Thanks for using our Service,\nHave a nice day !")