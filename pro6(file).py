class JournalManager:
    def __init__(self, filename="journal.txt"):
        self.filename = filename

    def add_entry(self):
        """Option 1: Appends a new journal entry with a manual timestamp to the file."""
        print("\nAdd a New Entry:")
        date_input = input("Enter date and time (e.g., 2026-12-25 10:00:00): ")
        entry_text = input("Enter your journal entry:\n")
        
        try:
            with open(self.filename, mode='a') as file:
                file.write(f"[{date_input}]\n{entry_text}\n\n")
            print("Entry added successfully!")
        except PermissionError:
            print("Error: Permission denied. Cannot write to file.")

    def view_all_entries(self):
        """Option 2: Displays all entries from the journal file with error handling."""
        try:
            
            with open(self.filename, mode='r') as file:
                content = file.read().strip()
                
            if not content:
                print("\nOutput (If the file does not exist / empty):")
                print("No journal entries found. Start by adding a new entry!")
                return
                
            print("\nOutput (If the file exists):")
            print("Your Journal Entries:")
            print("-" * 35)
            print(content)
            
        except FileNotFoundError:
            print("\nOutput:")
            print("Error: The journal file does not exist. Please add a new entry first.")
        except PermissionError:
            print("Error: Permission denied. Cannot read file.")

    def search_entry(self):
        """Option 3: Searches the journal file for a specific keyword or date."""
        try:
            with open(self.filename, mode='r') as file:
                content = file.read()
                
    
            entries = content.strip().split('\n\n')
            search_query = input("\nEnter a keyword or date to search: ").lower()
            
            found = False
            print("\nOutput (If a match is found):")
            print("Matching Entries:")
            print("-" * 35)
            
            for entry in entries:
                if entry and search_query in entry.lower():
                    print(entry)
                    print() 
                    found = True
                    
            if not found:
                print(f"No entries were found for the keyword: {search_query}.")
                
        except FileNotFoundError:
            print("Error: The journal file does not exist. No entries to search.")

    def delete_all_entries(self):
        """Option 4: Clears the journal after getting user confirmation."""
    
        try:
            
            with open(self.filename, mode='r') as file:
                if not file.read().strip():
                    print("\nOutput (If the file does not exist):")
                    print("No journal entries to delete.")
                    return
        except FileNotFoundError:
            print("\nOutput (If the file does not exist):")
            print("No journal entries to delete.")
            return

        confirm = input("\nAre you sure you want to delete all entries? (yes/no): ").strip().lower()
        if confirm == 'yes':
            try:
                
                with open(self.filename, mode='w') as file:
                    pass 
                print("\nOutput (If the file is deleted successfully):")
                print("All journal entries have been deleted.")
            except PermissionError:
                print("Error: Permission denied. Could not delete file contents.")
        else:
            print("Deletion cancelled.")


def main():
    
    manager = JournalManager()
    
    while True:
        
        print("\nWelcome to Personal Journal Manager!")
        print("Please select an option:")
        print("1. Add a New Entry")
        print("2. View All Entries")
        print("3. Search for an Entry")
        print("4. Delete All Entries")
        print("5. Exit")
        
        user_input = input("\nUser Input:\n")
        
        if user_input == '1':
            manager.add_entry()
        elif user_input == '2':
            manager.view_all_entries()
        elif user_input == '3':
            manager.search_entry()
        elif user_input == '4':
            manager.delete_all_entries()
        elif user_input == '5':
            print("\nOutput:")
            print("Thank you for using Personal Journal Manager. Goodbye!")
            break
        else:
            print("\nOutput:")
            print("Invalid option. Please select a valid option from the menu.")

if __name__ == "__main__":
    main()
