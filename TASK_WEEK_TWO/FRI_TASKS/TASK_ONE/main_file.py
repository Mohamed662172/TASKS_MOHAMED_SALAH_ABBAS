import wep_url

def print_menu():
    print("Favorite Websites:")
    for index, website in enumerate(wep_url.favorite_websites.keys()):
        print(f"{index + 1}. {website}")

def main():
    print_menu()

    choice = int(input("Enter the number of the website you want to open: "))
    
    if 1 <= choice <= len(wep_url.favorite_websites):
        website_name = list(wep_url.favorite_websites.keys())[choice - 1]
        website_url = wep_url.favorite_websites[website_name]
        print(f"Opening {website_name}...")
        wep_url.open_website(website_url)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
