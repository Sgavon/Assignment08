#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD():
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:
        writetofile(self): Formats object to save to a txt file
        __str__(self): Format to print when calling object
        __repr__(self): Format to print objects when printing a list

    """
    def __init__(self, ID, Title, Artist):
        
#----------------ATTRIBUTES--------------#
        self.ID = ID
        self.Title = Title
        self.Artist = Artist
#----------------PROPERTIES--------------#

    @property
    def ID(self):
        return self.__ID
    
    @ID.setter
    def ID(self, value):

        if not(str(value).isnumeric()):
            print('ID must be an Integer!')
        else:
            self.__ID = value
            
    @property
    def Title(self):
        return self.__Title.title()
    
    @Title.setter
    def Title(self, value):
        self.__Title = value
            
    @property
    def Artist(self):
        return self.__Artist.title()
    
    @Artist.setter
    def Artist(self, value):
        self.__Artist = value

# -- METHOD -- #

    def writetofile(self):
        return '{},{},{}\n'.format(self.ID, self.Title, self.Artist)

    def __str__(self):
        return '{}\t{} (by:{})'.format(self.ID, self.Title, self.Artist)
    
    def __repr__(self):
        return '{}\t{} (by:{})'.format(self.ID, self.Title, self.Artist)
    
# -- PROCESSING -- #
class FileIO():
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    @staticmethod
    def save_inventory(file_name, lst_Inventory):
        """Saves list of objects to a file:

        Args:
            file_name (string): Name of the file being accessed to save data
            lst_Inventory (list): List that holds the CD collection data to save to file

        Returns:
            None.
        """
        
        objFile = open(file_name, 'w')
        for obj in lst_Inventory:
            objFile.write(CD.writetofile(obj))
        objFile.close()
        return

        
    def load_inventory(file_name):
        """Loads list of objects to a file:

        Args:
            file_name (string): Name of the file being accessed to load data
            
        Returns:
            table (list): List with the CD objects.
        """
        table =[]
        try:
            objFile = open(file_name, 'r')
            for line in objFile:
                data = line.strip().split(',')
                table.append(CD(data[0], data[1],data[2]))
            objFile.close()
        except FileNotFoundError:
            print('File not Found!')
        except IndexError:
            print('File is formatted incorrectly')        
        return table

# -- PRESENTATION (Input/Output) -- #
class IO:
    
    """Processes inputs and outputs from/to the user:

    properties:
        
    methods:
        print_menu(): Displays a menu of choices to the user
        menu_choice(): Gets user input for menu selection
        show_inventory(table): Displays current inventory table
        CD_Choice_Add(): Collects the ID, CD Title, and Artist names to be added to the 2D CD Inventory List from the user

    """
    
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] exit\n')
        
        
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice
    
    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of obj): 2D data structure (list of objs) that holds the data during runtime.

        Returns:
            None.

        """
        try:
            print('======= The Current Inventory: =======')
            print('ID\tCD Title (by: Artist)\n')
            for obj in table:
                print(obj)
                #print('{}\t{} (by:{})'.format(row.ID, row.Title, row.Artist))
            print('======================================')
        except AttributeError:
            print("Loaded List is incorrectly formatted")
        
    @staticmethod
    def CD_Choice_Add():
        """Collects the ID, CD Title, and Artist names to be added to the 2D CD Inventory List from the user


        Args:
            None.

        Returns:
            CD(strID, strTitle, stArtist) (Object): Object to load into a new list

        """

        strID = input('Enter ID: ').strip()
        strTitle = input('What is the CD\'s title? ').strip()
        stArtist = input('What is the Artist\'s name? ').strip()
                
        return CD(strID, strTitle, stArtist)

# -- Main Body of Script -- #

# TODO Add Code to the main body

# Load data from file into a list of CD objects on script start

lstOfCDObjects = FileIO.load_inventory(strFileName)


# Display menu to user
    # show user current inventory
    # let user add data to the inventory
    # let user save inventory to file
    # let user load inventory from file
    # let user exit program
    
while True:
# 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()
    
    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
    # 3.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstOfCDObjects = FileIO.load_inventory(strFileName)
            IO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # 3.3 process add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist

            # 3.3.2 Add item to the table
            lstOfCDObjects.append(IO.CD_Choice_Add())
            
            continue  # start loop back at top.
    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.

    # 3.6 process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            FileIO.save_inventory(strFileName, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')

