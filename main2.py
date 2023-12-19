import tkinter as tk
from tkinter import ttk, PhotoImage, Toplevel, Canvas, Scrollbar
from PIL import Image, ImageTk

# Options for the destination dropdown
destination_options = ["Cubbon Park", "Lalbagh Botanical Garden", "Vidhana Soudha", "Bangalore Palace",
                        "Iskcon Temple Bangalore", 
                        "Bannerghatta National Park", 
                        "HAL Aerospace Museum", "Jawaharlal Nehru Planetarium", "Wonderla Amusement Park",
                        "Commercial Street"]


def on_select_destination():
    selected_destination = destination_var.get()
    
    print(f"Selected Destination: {selected_destination}")

    # Now you can filter and recommend places based on user's selections
    # Add your recommendation logic here

    show_destination_page(selected_destination)

def on_select_destination():
    selected_destination = destination_var.get()
    print(f"Selected Destination: {selected_destination}")
    show_destination_page(selected_destination)

def show_destination_page(selected_destination):
    if selected_destination == "Cubbon Park":
        show_cubbon_park_page()
    elif selected_destination == "Lalbagh Botanical Garden":
        show_lalbagh_page()
    elif selected_destination == "Vidhana Soudha":
        show_vidhana_soudha_page()
    elif selected_destination == "Wonderla Amusement Park":
        show_wonderla_Amusement_Park_page()
    elif selected_destination== "Bangalore Palace":
        show_Banglore_Palace_page()
    elif selected_destination == "Iskcon Temple Bangalore":
        show_iskcon_page()
    elif selected_destination == "Bannerghatta National Park":
        show_bannerghatta_zoo_page()
    elif selected_destination == "HAL Aerospace Museum":
        show_Hal_Aerospace_Museum_page()
    elif selected_destination == "Jawaharlal Nehru Planetarium":
        show_Jawaharlal_Nehru_Planetarium_page()
    elif selected_destination == "Commercial Street":
        show_Commertial_Street_page()
    # Add more conditions for other destinations
        
###Cubbon Park###

def show_cubbon_park_page():
    cubbon_park_window = Toplevel(root)
    cubbon_park_window.title("Cubbon Park")

    # Create a Canvas with a Scrollbar
    canvas = Canvas(cubbon_park_window, width=600, height=400, scrollregion=(0, 0, 2000, 2000))
    scrollbar = Scrollbar(cubbon_park_window, command=canvas.yview, troughcolor="light gray", activerelief=tk.GROOVE, width=20, orient="vertical")
    canvas.config(yscrollcommand=scrollbar.set)

    # Add widgets to display detailed information about Cubbon Park
    heading_label = tk.Label(
        canvas,
        text="Discover the Beauty of Cubbon Park",
        font=("Great vibes", 20),
        fg="purple",
        
    )
    heading_label.pack(padx=20, pady=20)

    info_label = tk.Label(
        canvas,
        text="\nCubbon Park dons many hats: a green lung in the heart of the city that also hosts a library, museums, a tennis academy, an aquarium, a toy train, and many statues and pavilions. It’s probably one of the only parks to have a busy road cutting through it. In the wee hours of the morning or evenings, it’s a jogger’s paradise. Spring adds to the beauty of this park, with the lovely and colorful Tabebuia trees in full bloom.",
        font=("Great Vibes", 16),
        fg="red",
        wraplength=1000,
        justify=tk.LEFT
    )
    info_label.pack(padx=20, pady=20)

    additional_info_label = tk.Label(
        canvas,
       text="\nWeather : 20 - 27°C\nLabel : Must Visit\nTags : Garden & Park\nTimings : 6:00 AM - 6:00 PM\nClosed on Mondays and second Tuesdays of Every month.\nStrictly for morning walkers: 6:00 AM - 8:00 AM\nTime Required : 1 - 2 hours\nEntry Fee : Free\n",
        font=("Great Vibes", 12),
        fg="DARK GREEN",
        wraplength=500,
        justify=tk.LEFT
    )
    additional_info_label.pack(padx=20, pady=20)

    additional_info_label = tk.Label(
        canvas,
        text="Things To Do In Cubbon Park:\nA gentle amalgam of natural and man-made sights, Cubbon Park has multicoloured exotic floral beds lining its various avenues which are located close to important administrative buildings like:\n\n• Central Public Library\n• Government Museum\n• Sir Vishweshwariah Industrial and Technological Museum\n• Karnataka High Court\n• Venkatappa Art Gallery",
        font=("Great Vibes", 12),
        fg="blue",
        wraplength=800,
        justify=tk.LEFT
    )
    additional_info_label.pack(padx=20, pady=20)

    additional_info_label = tk.Label(
        canvas,
        text="""LOCATION :\nCubbon Park\nIn the heart of the city’s business hub is Bangalore’s most favourite garden. Cubbon Park is a beautifully maintained 120-hectare garden where all the local residents of the city take a break. A landmark ‘lung’ area of Bengaluru, the gardens are dotted with a lot of colonial heritage and charm, which are today a part of the state capital’s political centre. Home to the red-painted Gothic style State Central Library, the magnificent Vidhan Souda built in Mysore Neo-Dravidian architectural style, the neoclassical Attara Kacheri built in 1864 and housing the High Court, oldest museums and GPO in its vicinity, a trip to Cubbon Park is a great heritage walk. Sundays at the park are quite a treat with a plethora of activities to choose from - concerts, fun runs, yoga, tiny farmers market, the list is endless.""",
        font=("Great Vibes", 10),
        fg="maroon",
        wraplength=800,
        justify=tk.LEFT
    )
    additional_info_label.pack(padx=20, pady=20)

    # Example: Display multiple images
    image_paths = [
        r"images\cub1.jpg",
        r"images\cub2.jpg",
        r"images\cub3.jpg",
        r"images\cub4.jpg",
        # r"images\cub5.jpg",
        r"images\cub6.jpg"
    ]

    # Display images one after the other
    current_image_index = 0
    current_image_label = None

    def show_next_image():
        nonlocal current_image_index, current_image_label
        # Destroy the previous image label if it exists
        if current_image_label:
            current_image_label.destroy()
        current_image_index = (current_image_index + 1) % len(image_paths)
        update_image()

    def update_image():
        nonlocal current_image_index, current_image_label
        img = Image.open(image_paths[current_image_index])
        img = ImageTk.PhotoImage(img)
        current_image_label = tk.Label(canvas, image=img)
        current_image_label.image = img
        canvas.create_window(260, 50, anchor=tk.NW, window=current_image_label)  # Adjust the coordinates

        # Schedule to show the next image after 2000 milliseconds (2 seconds)
        cubbon_park_window.after(2000, show_next_image)

    # Initial image display
    update_image()

    # Pack the Canvas and Scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y", expand=False)

###Lalbagh Botanical Garden###

def show_lalbagh_page():
    lalbagh_window = Toplevel(root)
    lalbagh_window.title("Lalbagh Botanical Garden")

    # Create a Canvas with a Scrollbar
    canvas = Canvas(lalbagh_window, width=600, height=400, scrollregion=(0, 0, 2000, 2000))
    scrollbar = Scrollbar(lalbagh_window, command=canvas.yview, troughcolor="light gray", activerelief=tk.GROOVE, width=20, orient="vertical")
    canvas.config(yscrollcommand=scrollbar.set)

    # Add widgets to display detailed information about Lalbagh Botanical Garden
    heading_label = tk.Label(
        canvas,
        text="Welcome to Lalbagh Botanical Garden",
        font=("Great vibes", 20),
        fg="white",
    )
    heading_label.pack(padx=20, pady=20)

    info_label = tk.Label(
        canvas,
       text="\nLalbagh is one of Bengaluru’s major attractions. A sprawling garden situated in a 240 acres piece of land in the heart of the city, Lalbagh houses India’s largest collection of tropical plants and sub-tropical plants, including trees that are several centuries old. Exhibits like the Snow White and the seven dwarfs, and a topiary park, an expansive lake, a beautiful glasshouse modelled around the Crystal Palace in London adorn the park giving it a surrealistic atmosphere. A watchtower perched on top of a 3000 million years old rocky outcrop (which is a National Geological Monument), built by Kempegowda, the founder of Bengaluru also adorns the picturesque garden.",
        font=("Great Vibes", 12),
        fg="green",
        wraplength=900,
        justify=tk.LEFT
    )
    info_label.pack(padx=20, pady=20)

    additional_info_label = tk.Label(
        canvas,
       text="\nWeather : 20 - 33.1°C\nLabel : Must Visit\nTags : Botanical Garden\nTimings : 6:00 AM - 7:00 PM \nOpen on all days\nTime Required : 2 - 3 hours\nEntry Fee :\nAdults: INR 20 per person.\nChildren below 12 years: Free entry.\nStill Camera: INR 501.\n",
        font=("Great Vibes", 10),
        fg="red",
        wraplength=500,
        justify=tk.LEFT
    )
    additional_info_label.pack(padx=20, pady=20)

    additional_info_label = tk.Label(
        canvas,
        text="""Things to do in Lalbagh Botanical Garden:\nExplore the Ganesh Temple: The Ganesh Temple is one of the most significant structures within the garden.\nWalk along the garden paths: The garden paths provide a glimpse into the rich flora of the garden.\nLearn about Bangalore’s history: The garden is a great place to learn about the rich history of Bangalore.\nTake a guided tour: A guided tour can provide in-depth information about the garden and its history.\nAttend cultural events: The garden often hosts various cultural events.\nCheck out the floral installations: Marvel at the amazing floral installations like the HMT clock and Snow White’s garden.\nMarvel at the Lotus lake: The pink beauty of the Lotus lake is a sight to behold.\nFeel the cool breeze along Lalbagh lake: Enjoy the serene environment along the lakeside of Lalbagh lake.\nDiscover ancient rocks: Discover 3000 million year old rocks at Peninsular Gneiss Rock.""",
        font=("Great Vibes", 10),
        fg="dark blue",
        wraplength=800,
        justify=tk.LEFT
    )
    additional_info_label.pack(padx=20, pady=20)

    additional_info_label = tk.Label(
        canvas,
        text="Location :\nLalbagh is located 7 km south of the city center (Majestic area) and 38 km from the Bengaluru airport. Lalbagh can be accessed using the Bengaluru metro rail network from different parts of Bengaluru city. Buses, autos or taxis are readily available to reach Lalbagh.",
        font=("Great Vibes", 8),
        fg="green",
        wraplength=800,
        justify=tk.LEFT
    )
    additional_info_label.pack(padx=20, pady=20)

    # Example: Display multiple images
    image_paths = [
        r"images\lalbagh.jpg",
        r"images\lalbagh1.jpg",
        r"images\lalbagh2.jpg",
        r"images\lalbagh3.jpg",
        r"images\lalbagh4.jpg",
        r"images\Lalbagh5.jpg",
        r"images\lalbagh6.jpg"
    ]

    # Display images one after the other
    current_image_index = 0
    current_image_label = None

    def show_next_image():
        nonlocal current_image_index, current_image_label
        # Destroy the previous image label if it exists
        if current_image_label:
            current_image_label.destroy()
        current_image_index = (current_image_index + 1) % len(image_paths)
        update_image()

    def update_image():
        nonlocal current_image_index, current_image_label
        img = Image.open(image_paths[current_image_index])
        img = ImageTk.PhotoImage(img)
        current_image_label = tk.Label(canvas, image=img)
        current_image_label.image = img
        canvas.create_window(260, 50, anchor=tk.NW, window=current_image_label)  # Adjust the coordinates

        # Schedule to show the next image after 2000 milliseconds (2 seconds)
        lalbagh_window.after(2000, show_next_image)

    # Initial image display
    update_image()

    # Pack the Canvas and Scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y", expand=False)

###Vidhana Soudha###

def show_vidhana_soudha_page():
    vidhana_soudha_window = Toplevel(root)
    vidhana_soudha_window.title("Vidhana Soudha")

  
    # Create a Canvas with a Scrollbar
    canvas = Canvas(vidhana_soudha_window, width=600, height=400, scrollregion=(0, 0, 2000, 2000))
    scrollbar = Scrollbar(vidhana_soudha_window, command=canvas.yview, troughcolor="light gray", activerelief=tk.GROOVE, width=20, orient="vertical")
    canvas.config(yscrollcommand=scrollbar.set)

    # Add widgets to display detailed information about Vidhana Soudha
    heading_label = tk.Label(
        canvas,
        text="Discover the Beauty of Vidhana Soudha",
        font=("Great vibes", 20),
        fg="purple",
        
    )
    heading_label.pack(padx=20, pady=20)

    info_label = tk.Label(
        canvas,
        text="\nDescribed by Pandit Jawaharlal Nehru as 'a temple dedicated to the nation', Vidhana Soudha houses the State Legislature and the Secretariat of Karnataka and is one of the most popular attractions in the lively and colourful city of Bengaluru. It also proudly boasts the title of being the largest state legislative building in the country. With four entrances in all four directions and four floors above the ground level and one below it, we surely don't doubt the title. Popularly known as the 'Taj Mahal of South India', it is counted as one of the most magnificent buildings in the city and is sure to impress the onlooker with its sophisticated poise and glorified grandiose. The entire monument is illuminated on Sundays and public holidays and is a sight for sore eyes.",
        font=("Great Vibes", 16),
        fg="red",
        wraplength=1000,
        justify=tk.LEFT
    )
    info_label.pack(padx=20, pady=20)

    additional_info_label = tk.Label(
        canvas,
       text="\nWeather : 20 - 27°C\nLabel : Must Visit\nTags : Monument\nTimings : 10:00 AM - 5:30 PM \nClosed on weekends and public holidays.\nTime Required : 1 - 2 hours\nEntry Fee :\nAdults: INR 20 per person.\nChildren below 12 years: Free entry.\nStill Camera: INR 501.\n",
        font=("Great Vibes", 12),
        fg="DARK GREEN",
        wraplength=500,
        justify=tk.LEFT
    )
    additional_info_label.pack(padx=20, pady=20)

    additional_info_label = tk.Label(
        canvas,
        text="Things To Do In Vidhana Soudha:\nExplore the Building’s Architecture and Art: The building is a splendid structure that covers an area of 60 acres. It boasts of an elegant and truly exquisite Neo-Dravidian style of architecture.\nVisit the Assembly Hall and Council Hall: The building has an assembly hall and a council hall where the legislative assembly and the legislative council of the state meet respectively.\nEnjoy the Light Show and Fountain Show: The entire monument is illuminated on Sundays and public holidays and is a sight for sore eyes.\nExperience the Events and Activities: The Vidhana Soudha often hosts various cultural and official events.",
        font=("Great Vibes", 12),
        fg="blue",
        wraplength=800,
        justify=tk.LEFT
    )
    additional_info_label.pack(padx=20, pady=20)

    additional_info_label = tk.Label(
        canvas,
        text="""LOCATION :\nVidhana Soudha is located in the city of Bangalore, India. The exact address is Dr Ambedkar Rd, Sampangi Ramnagar, Bengaluru, Karnataka, 5600011. It’s situated in the heart of Bangalore, on the northwestern side of Cubbon Park.""",
        font=("Great Vibes", 10),
        fg="maroon",
        wraplength=800,
        justify=tk.LEFT
    )
    additional_info_label.pack(padx=20, pady=20)

    # Example: Display multiple images
    image_paths = [
        r"images\Bengaluru’s-Vidhana-Soudha-1.jpg",
        r"images\VS 2.jpg",
        r"images\vidhana soudha 5.jpg",
        r"images\vidhana soudha 3.jpg"
    ]

    # Display images one after the other
    current_image_index = 0
    current_image_label = None

    def show_next_image():
        nonlocal current_image_index, current_image_label
        # Destroy the previous image label if it exists
        if current_image_label:
            current_image_label.destroy()
        current_image_index = (current_image_index + 1) % len(image_paths)
        update_image()

    def update_image():
        nonlocal current_image_index, current_image_label
        img = Image.open(image_paths[current_image_index])
        img = ImageTk.PhotoImage(img)
        current_image_label = tk.Label(canvas, image=img)
        current_image_label.image = img
        canvas.create_window(260, 50, anchor=tk.NW, window=current_image_label)  # Adjust the coordinates

        # Schedule to show the next image after 2000 milliseconds (2 seconds)
        vidhana_soudha_window.after(2000, show_next_image)

    # Initial image display
    update_image()

    # Pack the Canvas and Scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y", expand=False)

###Wonderla Amusement Park###

def show_wonderla_Amusement_Park_page():
    wonderla_Amusement_Park_window = Toplevel(root)
    wonderla_Amusement_Park_window.title("Wonderla")

    # Create a Canvas with a Scrollbar
    canvas = Canvas(wonderla_Amusement_Park_window, width=600, height=400, scrollregion=(0, 0, 2000, 2000))
    scrollbar = Scrollbar(wonderla_Amusement_Park_window, command=canvas.yview, troughcolor="light gray", activerelief=tk.GROOVE, width=20, orient="vertical")
    canvas.config(yscrollcommand=scrollbar.set)

    # Add widgets to display detailed information about Cubbon Park
    heading_label = tk.Label(
        canvas,
        text="Discover the Beauty of Wonderla",
        font=("Great vibes", 20),
        fg="purple",
        
    )
    heading_label.pack(padx=20, pady=20)

    info_label = tk.Label(
        canvas,
        text="\nWonderLa is one of India’s largest amusement and water theme parks. Located on the outskirts of Bengaluru in Ramanagara district, Wonderla Bangalore is spread across 82 acres and has over 60 thrill-packed rides offering entertainment and fun for all age groups. It also has a resort inside the amusement park – making it the first amusement park in India to have a resort built right inside it.",
        font=("Great Vibes", 16),
        fg="red",
        wraplength=1000,
        justify=tk.LEFT
    )
    info_label.pack(padx=20, pady=20)

    additional_info_label = tk.Label(
        canvas,
       text="\nWeather : 15.8 - 27.9°C\nLabel : Must Visit\nTags : Dry and Water games\nTimings : Weekdays (Monday to Friday): The park is open from 11:00 AM to 06:00 PM. The water park operates from 12:30 PM to 05:00 PM.\n          Weekends and Holidays: The park is open from 11:00 AM to 07:00 PM. The water park operates from 12:00 PM to 06:00 PM.\nTime Required : 5 - 7 hours\nEntry Fee : Weekdays (Monday to Friday):\nRegular Tickets:\nAdult: Rs.1249/-\nChild: Rs.999/-\nSenior Citizen: Rs.937/-\nAdult (with College ID): Rs.999/-\nFastrack Tickets:\nAdult: Rs.2498/-\nChild: Rs.1998/-\nWeekends and Holidays:\nRegular Tickets:\nAdult: Rs.1499/-\nChild: Rs.1199/-\nSenior Citizen: Rs.1124/-\nAdult (with College ID): Rs.1199/-\nFastrack Tickets:\nAdult: Rs.2998/-\nChild: Rs.2398/-\nPlease note that child ticket rates are applicable for children with a height ranging between 85 to 140 cm. For senior citizen tickets, photo ID with age proof is mandatory. For college students, original college ID needs to be displayed at the gate during check-in.\n",
        font=("Great Vibes", 12),
        fg="DARK GREEN",
        wraplength=500,
        justify=tk.LEFT
    )
    additional_info_label.pack(padx=20, pady=20)

    additional_info_label = tk.Label(
        canvas,
        text="Things To Do In Wonderla:\nExplore the Park: Take a stroll throughout its various areas to explore the attractions and games.\nEnjoy the Rides: The park features a diverse variety of fun electric games. Highlights include Recoil, a reverse-loop roller coaster; the free-fall Flash Tower; and the topsy-turvy Hurricane.\nKids' Games: The park has a number of kids' games that provide an alluring experience for the whole family.\nYoungster Games: There are games designed to fit the taste of youngsters such as rise and fall games, flying chairs, and rollercoasters.\nMazes Game: Spend an enjoyable time trying out the mazes game.\nWater Games: Enjoy a variety of water games.\nUnique Games: Try out some unique games such as Drop Tower Game, Ferris Wheel Game, Bumper Car Game, and Swinging Ship Game.",
        font=("Great Vibes", 12),
        fg="blue",
        wraplength=800,
        justify=tk.LEFT
    )
    additional_info_label.pack(padx=20, pady=20)

    additional_info_label = tk.Label(
        canvas,
        text="""LOCATION :\nWonderla Amusement Park in Bangalore is located on Mysore Road, 28 km from Bengaluru city. The exact address is 28th km, Mysore Road, Before Bidadi, Bengaluru, Karnataka, 562109, India.""",
        font=("Great Vibes", 10),
        fg="maroon",
        wraplength=800,
        justify=tk.LEFT
    )
    additional_info_label.pack(padx=20, pady=20)

    # Example: Display multiple images
    image_paths = [
        r"images\Bengaluru’s-Vidhana-Soudha-1.jpg",
        r"images\VS4.jpg",
        r"images\VS 2.jpg",
        r"images\vidhana soudha 5.jpg",
        r"images\vidhana soudha 3.jpg"
    ]

    # Display images one after the other
    current_image_index = 0
    current_image_label = None

    def show_next_image():
        nonlocal current_image_index, current_image_label
        # Destroy the previous image label if it exists
        if current_image_label:
            current_image_label.destroy()
        current_image_index = (current_image_index + 1) % len(image_paths)
        update_image()

    def update_image():
        nonlocal current_image_index, current_image_label
        img = Image.open(image_paths[current_image_index])
        img = ImageTk.PhotoImage(img)
        current_image_label = tk.Label(canvas, image=img)
        current_image_label.image = img
        canvas.create_window(260, 50, anchor=tk.NW, window=current_image_label)  # Adjust the coordinates

        # Schedule to show the next image after 2000 milliseconds (2 seconds)
        wonderla_Amusement_Park_window.after(2000, show_next_image)

    # Initial image display
    update_image()

    # Pack the Canvas and Scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y", expand=False)


###Iskcon Temple###

def show_iskcon_page():
    iskcon_window = Toplevel(root)
    iskcon_window.title("Iskcon Temple")

    # Create a Canvas with a Scrollbar
    canvas = Canvas(iskcon_window, width=600, height=400, scrollregion=(0, 0, 2000, 2000))
    scrollbar = Scrollbar(iskcon_window, command=canvas.yview, troughcolor="light gray", activerelief=tk.GROOVE, width=20, orient="vertical")
    canvas.config(yscrollcommand=scrollbar.set)

    # Add widgets to display detailed information about Iskcon Temple
    heading_label = tk.Label(
        canvas,
        text="Welcome to Iskcon Temple",
        font=("Great vibes", 20),
        fg="purple"
    )
    heading_label.pack(padx=20, pady=20)

    info_label = tk.Label(
        canvas,
       text="\nISKCON Sri Radha Krishna temple was inaugurated in the year 1997. It is not just a temple, but a cultural complex housing the temples dedicated to the Deities of Sri Sri Radha Krishnachandra, Sri Sri Krishna Balarama, Sri Sri Nitai Gauranga, Sri Srinivasa Govinda, Sri Prahlada Narasimha, Bhakta Hanuman, Garudadeva and Srila Prabhupada, Founder Acharya of ISKCON. ISKCON Bangalore is a charitable society with the objective of propagating Krishna Consciousness all over the world, as explained by Srila Prabhupada, whose teachings are based on Bhagavad-gita and Srimad Bhagavatam.",
        font=("Great Vibes", 12),
        fg="green",
        wraplength=900,
        justify=tk.LEFT
    )
    info_label.pack(padx=20, pady=20)

    additional_info_label = tk.Label(
        canvas,
       text="\nWeather : 17 - 26°C\nLabel : Must Visit\nTags : Shrine and Temple\nTimings : Weekdays: 7.15 AM to 1 PM, 4.15 PM to 8.20 PM\n Weekends: 7.15 AM till 8.30 PM.\nPhotography is NOT allowed inside temple premises and modest dress code is recommended. Locker rooms are available to store bags and cameras.\nOpen everyday\nTime Required : 1 - 3 hours\nEntry Fee :Free\n",
        font=("Great Vibes", 10),
        fg="red",
        wraplength=500,
        justify=tk.LEFT
    )
    additional_info_label.pack(padx=20, pady=20)

    additional_info_label = tk.Label(
        canvas,
        text="""Things to do in Iskcon Temple:\nDarshan: You can have darshan of the deities of Sri Sri Radha Krishnachandra, Sri Sri Krishna Balarama, Sri Sri Nitai Gauranga, Sri Srinivasa Govinda, and Sri Prahlada Narasimha.\nKirtan and Chanting: The temple organizes kirtan (devotional songs) and chanting sessions.\nPhilosophy Talks: You can attend talks on philosophy.\nFestivals: The temple conducts special programs for Hindu festivals and other important holidays.\nShopping: There are various shops within the temple complex where you can buy snacks and religious materials.""",
        font=("Great Vibes", 10),
        fg="dark blue",
        wraplength=800,
        justify=tk.LEFT
    )
    additional_info_label.pack(padx=20, pady=20)

    additional_info_label = tk.Label(
        canvas,
        text="Location :\nThe ISKCON temple in Bangalore is located at Hare Krishna Hill, Chord Road, Rajajinagar, Bangalore 560010. It’s one of the largest Krishna-Hindu temples in the world.",
        font=("Great Vibes", 8),
        fg="green",
        wraplength=800,
        justify=tk.LEFT
    )
    additional_info_label.pack(padx=20, pady=20)

    # Example: Display multiple images
    image_paths = [
        r"images\ISCON1.jpg",
        r"images\ISCON2.jpg",
        r"images\ISKCON3.jpg",
        r"images\ISCON4.jpg",
    ]

    # Display images one after the other
    current_image_index = 0
    current_image_label = None

    def show_next_image():
        nonlocal current_image_index, current_image_label
        # Destroy the previous image label if it exists
        if current_image_label:
            current_image_label.destroy()
        current_image_index = (current_image_index + 1) % len(image_paths)
        update_image()

    def update_image():
        nonlocal current_image_index, current_image_label
        img = Image.open(image_paths[current_image_index])
        img = ImageTk.PhotoImage(img)
        current_image_label = tk.Label(canvas, image=img)
        current_image_label.image = img
        canvas.create_window(260, 50, anchor=tk.NW, window=current_image_label)  # Adjust the coordinates

        # Schedule to show the next image after 2000 milliseconds (2 seconds)
        iskcon_window.after(2000, show_next_image)

    # Initial image display
    update_image()

    # Pack the Canvas and Scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y", expand=False)

##Bannerghatta Zoo###

def show_bannerghatta_zoo_page():
    bannerghatta_zoo_window = Toplevel(root)
    bannerghatta_zoo_window.title("Bannerghatta National Park")

    # Create a Canvas with a Scrollbar
    canvas = Canvas(bannerghatta_zoo_window, width=600, height=400, scrollregion=(0, 0, 2000, 2000))
    scrollbar = Scrollbar(bannerghatta_zoo_window, command=canvas.yview, troughcolor="light gray", activerelief=tk.GROOVE, width=20, orient="vertical")
    canvas.config(yscrollcommand=scrollbar.set)

    # Add widgets to display detailed information about Bannerghatta Zoo
    heading_label = tk.Label(
        canvas,
        text="Discover the Beauty of Bannerghatta Nationak Park",
        font=("Great vibes", 20),
        fg="purple",
        
    )
    heading_label.pack(padx=20, pady=20)

    info_label = tk.Label(
        canvas,
        text="\nThe Bannerghatta National Park is a sanctuary for a large variety of flora and fauna. Spread over a massive area of around 104.27 sq. km, this national park was established in the year 1971. The park itself has a number of establishments within its confines, which includes the country's first butterfly park as well.",
        font=("Great Vibes", 16),
        fg="red",
        wraplength=1000,
        justify=tk.LEFT
    )
    info_label.pack(padx=20, pady=20)

    additional_info_label = tk.Label(
        canvas,
        text="\n\n\n\n\n\n\\n\n\n\n\n\n\n\n\n\nWeather : 20 - 27°C\nLabel : Must Visit\nTags : National Park\nTimings :\nButterfly park and boating: 9:30 AM - 5:00 PM\nGrand Safari: 10:00 AM - 4:30 PM\nClosed on Tuesdays\nTime Required : 5 - 6 hours\nEntry Fee :\nIndians:\n Adults: INR 80,Kids (6 - 12 years): INR 40\n Senior citizens: INR 50\nForeigners:\n Adults: INR 400\n Kids: INR 300\n",
        font=("Great Vibes", 12),
        fg="DARK GREEN",
        wraplength=500,
        justify=tk.LEFT
    )
    additional_info_label.pack(padx=20, pady=20)

    additional_info_label = tk.Label(
        canvas,
        text="Things To Do In Bannerghatta National Park:\nZoo: The zoo is spread over 12 hectares and houses several wild animals such as King Cobra, Panthers, Crocodiles, Bears, Deer, and birds.\nLion Safari: You can spot lions from close quarters during the Lion Safari.\nTiger Safari: The park houses 33 tigers, including 7 white tigers. Tigers are maintained in three groups.\nButterfly Park: The park has a dedicated butterfly park consisting of a butterfly garden which is a dedicated 7.5 acres, a butterfly conservatory, a museum, a research laboratory, and a curio shop.\nBoating: Boating is another activity that you can enjoy.\nHiking and Trekking: The park is also a popular hiking and trekking site.",
        font=("Great Vibes", 12),
        fg="blue",
        wraplength=800,
        justify=tk.LEFT
    )
    additional_info_label.pack(padx=20, pady=20)

    additional_info_label = tk.Label(
        canvas,
        text="""LOCATION :\nThe Bannerghatta National Park is located at Bannerghatta Road, Bannerghatta, Bengaluru, Karnataka 560083. It’s situated almost midway between the city center of Bengaluru and the Anekal town, at about 25 km from Vidhana Soudha and at about 20 km to the North West of Anekal town. It’s well connected by adequate transport facilities (in the form of city buses and cabs) from various locations in Bangalore. """,
        font=("Great Vibes", 10),
        fg="maroon",
        wraplength=800,
        justify=tk.LEFT
    )
    additional_info_label.pack(padx=20, pady=20)

    # Example: Display multiple images
    image_paths = [
        r"images\bannerghatta 2.jpg",
        r"images\Bannerghatta-NationalPark-4.jpg",
        r"images\bannerghattanationalpark3.jpg",
        r"images\BG1.jpg"
    ]

    # Display images one after the other
    current_image_index = 0
    current_image_label = None

    def show_next_image():
        nonlocal current_image_index, current_image_label
        # Destroy the previous image label if it exists
        if current_image_label:
            current_image_label.destroy()
        current_image_index = (current_image_index + 1) % len(image_paths)
        update_image()

    def update_image():
        nonlocal current_image_index, current_image_label
        img = Image.open(image_paths[current_image_index])
        img = ImageTk.PhotoImage(img)
        current_image_label = tk.Label(canvas, image=img)
        current_image_label.image = img
        canvas.create_window(260, 50, anchor=tk.NW, window=current_image_label)  # Adjust the coordinates

        # Schedule to show the next image after 2000 milliseconds (2 seconds)
        bannerghatta_zoo_window.after(2000, show_next_image)

    # Initial image display
    update_image()

    # Pack the Canvas and Scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y", expand=False)

##Jawaharlal_Nehru_Planetarium###

def show_Jawaharlal_Nehru_Planetarium_page():
    Jawaharlal_Nehru_Planetarium_window = Toplevel(root)
    Jawaharlal_Nehru_Planetarium_window.title("Jawaharlal Nehru Planetarium")

    # Create a Canvas with a Scrollbar
    canvas = Canvas(Jawaharlal_Nehru_Planetarium_window, width=600, height=400, scrollregion=(0, 0, 2000, 2000))
    scrollbar = Scrollbar(Jawaharlal_Nehru_Planetarium_window,command=canvas.yview, troughcolor="light gray", activerelief=tk.GROOVE, width=20, orient="vertical")
    canvas.config(yscrollcommand=scrollbar.set)

    # Add widgets to display detailed information about Jawaharlal Nehru Planetarium
    heading_label = tk.Label(
        canvas,
        text="Discover the Beauty of Jawaharlal Nehru Planetarium ",
        font=("Great vibes", 20),
        fg="purple",
        
    )
    heading_label.pack(padx=20, pady=20)

    info_label = tk.Label(
        canvas,
        text="\nJawaharlal Nehru Planetarium in Bangalore is a popular attraction in the city that is administered by the Bangalore Association for Science Education (BASE). The entire establishment is meant for science enthusiasts with an aim to impart knowledge of the aspects of earth and space in a fun and exciting way.People1,especially kids,from around the city visit this place as well as tourists who visit banglore",
        font=("Great Vibes", 16),
        fg="red",
        wraplength=1000,
        justify=tk.LEFT
    )
    info_label.pack(padx=20, pady=20)

    additional_info_label = tk.Label(
        canvas,
        text="\n\n\n\n\n\n\\n\n\n\n\n\n\n\n\n\nWeather : 20 - 27°C\nLabel : Fun for kids\nTags : pianetarium\nTimings : 10:00 AM - 5:30 PM (closed on Mondays, second Tuesdays, local and national holidays)\nTime Required : 2-3 hrs\nEntry Fee:adults:INR 60 School students/children(up to 16 years):INR 35", 
        font=("Great Vibes", 12),
        fg="DARK GREEN",
        wraplength=500,
        justify=tk.LEFT
    )
    additional_info_label.pack(padx=20, pady=20)

    additional_info_label = tk.Label(
        canvas,
        text="Sky theater show:\nSky Theatre is one of the main attractions of the JN Planetarium whose roof is a perfect hemispherical dome to imitate the way sky looks to us. This theatre, seating around 210 in recliners, holds shows projected on the domed roof and has a unidirectional view all around.\nExibition Hall:The Exhibition Hall is a gallery full of knowledge about space, stars and everything else about astronomy - meteors, asteroids, eclipses and so on. The place is full of space-related scientific facts and trivia all around.\nScience Park:The Science Park is a campus inside the premises of the planetarium where there are more than 40 scientific exhibits which are interactive and explain difficult and complex concepts of physics and astronomy in simple, game-like manners",
        wraplength=800,
        justify=tk.LEFT
    )
    additional_info_label.pack(padx=20, pady=20)

    additional_info_label = tk.Label(
        canvas,
        text="""LOCATION :\nJawaharlal Nehru Planetarium is located in the heart of the city, only 2 km from the railway station and 1.5 km from the Dr. BR Ambedkar metro station. It can also be reached by the public buses, cabs or hired cars""",
        font=("Great Vibes", 10),
        fg="blue",
        wraplength=800,
        justify=tk.LEFT
    )
    additional_info_label.pack(padx=20, pady=20)

    # Example: Display multiple images
    image_paths = [
        r"images\bannerghatta 2.jpg",
        r"images\Bannerghatta-NationalPark-4.jpg",
        r"images\bannerghattanationalpark3.jpg",
        r"images\BG1.jpg"
    ]

    # Display images one after the other
    current_image_index = 0
    current_image_label = None

    def show_next_image():
        nonlocal current_image_index, current_image_label
        # Destroy the previous image label if it exists
        if current_image_label:
            current_image_label.destroy()
        current_image_index = (current_image_index + 1) % len(image_paths)
        update_image()

    def update_image():
        nonlocal current_image_index, current_image_label
        img = Image.open(image_paths[current_image_index])
        img = ImageTk.PhotoImage(img)
        current_image_label = tk.Label(canvas, image=img)
        current_image_label.image = img
        canvas.create_window(260, 50, anchor=tk.NW, window=current_image_label)  # Adjust the coordinates

        # Schedule to show the next image after 2000 milliseconds (2 seconds)
        Jawaharlal_Nehru_Planetarium_window.after(2000, show_next_image)

    # Initial image display
    update_image()

    # Pack the Canvas and Scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y", expand=False)

##Hal Aerospace Museum###

def show_Hal_Aerospace_Museum_page():
    Hal_Aerospace_Museum_window = Toplevel(root)
    Hal_Aerospace_Museum_window.title("Hal Aerospace Museum")

    # Create a Canvas with a Scrollbar
    canvas = Canvas(Hal_Aerospace_Museum_window, width=600, height=400, scrollregion=(0, 0, 2000, 2000))
    scrollbar = Scrollbar(Hal_Aerospace_Museum_window, command=canvas.yview, troughcolor="light gray", activerelief=tk.GROOVE, width=20, orient="vertical")
    canvas.config(yscrollcommand=scrollbar.set)

    # Add widgets to display detailed information about Hal Aerospace Museum  
    heading_label = tk.Label(
        canvas,
        text="Discover the Beauty of Hal Aerospace Museum ",
        font=("Great vibes", 20),
        fg="purple",
        
    )
    heading_label.pack(padx=20, pady=20)

    info_label = tk.Label(
        canvas,
        text="\nHAL Aerospace Museum is one of the major public attractions of Bangalore. Inaugurated in 2001 at the Hindustan Aeronautics Limited premises, the museum was established with an objective of educating the public about everything the journey of HAL, one of Asia's largest and most important aeronautical companies, had to offer - be it historical, scientific or academic",
        font=("Great Vibes", 16),
        fg="red",
        wraplength=1000,
        justify=tk.LEFT
    )
    info_label.pack(padx=20, pady=20)

    additional_info_label = tk.Label(
        canvas,
        text="\nWeather : 20 - 27°C\nLabel : Must Visit\nTags : Museum\nTimings : 9:00 AM - 5:00 PM\nTime Required : 2-3 hours\nEntry Fee : Adults: INR 50,Kids (4-18 years)\nAdditinal Charge:nstill camera:50 ",
        font=("Great Vibes", 12),
        fg="green",
        wraplength=500,
        justify=tk.LEFT
    )
    additional_info_label.pack(padx=20, pady=20)

    additional_info_label = tk.Label(
        canvas,
        text="Things To See at HAL Aerospace Museum:\nThe Gallery of the museum:The museum itself is the most prominent attraction in the heritage center's premises. It is spread over an area of 4 acres and is India's first such establishment devoted entirely towards the aeronautical history and science of the country. This one of a kind museum divides its public display into two halls.\nAir Traffic Control Tower:Apart from witnessing numerous helicopters and aircraft, you can even feel the working of aviation Industry. This place houses a mock Air Traffic Control Tower, which provides the visitors with an incomparable experience of viewing the landing and take-off of plane insight and thus is an amazing experience for everyone visiting the place.\nSustainability Development Park:This patch of yet another scientific facts and models educates the public about the various ways we can practice sustainability to save us, nature and the earth. It includes explained mechanisms of how solar energy works, how power is generated from turbines and windmills, why is biogas important and so on",
        font=("Great Vibes", 12),
        fg="blue",
        wraplength=800,
        justify=tk.LEFT
    )
    additional_info_label.pack(padx=20, pady=20)

    additional_info_label = tk.Label(
        canvas,
        text="""LOCATION :\nThe HAL Aerospace Museum is situated near HAL Police Station at Old Airport Road, around 10 km away from the Bangalore City Railway Station. From the station, or from any other destination in the city, you can hire a cab to reach the museum. It is very popular a site and finding it will not be a difficult task""",
        font=("Great Vibes", 10),
        fg="maroon",
        wraplength=800,
        justify=tk.LEFT
    )
    additional_info_label.pack(padx=20, pady=20)

    # Example: Display multiple images
    image_paths = [
        r"images\bannerghatta 2.jpg",
        r"images\Bannerghatta-NationalPark-4.jpg",
        r"images\bannerghattanationalpark3.jpg",
        r"images\BG1.jpg"
    ]

    # Display images one after the other
    current_image_index = 0
    current_image_label = None

    def show_next_image():
        nonlocal current_image_index, current_image_label
        # Destroy the previous image label if it exists
        if current_image_label:
            current_image_label.destroy()
        current_image_index = (current_image_index + 1) % len(image_paths)
        update_image()

    def update_image():
        nonlocal current_image_index, current_image_label
        img = Image.open(image_paths[current_image_index])
        img = ImageTk.PhotoImage(img)
        current_image_label = tk.Label(canvas, image=img)
        current_image_label.image = img
        canvas.create_window(260, 50, anchor=tk.NW, window=current_image_label)  # Adjust the coordinates

        # Schedule to show the next image after 2000 milliseconds (2 seconds)
        Hal_Aerospace_Museum_window.after(2000, show_next_image)

    # Initial image display
    update_image()

    # Pack the Canvas and Scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y", expand=False)

##Commertial Street###

def show_Commertial_Street_page():
    Commertial_Street_window = Toplevel(root)
    Commertial_Street_window.title("Commertial Street")

    # Create a Canvas with a Scrollbar
    canvas = Canvas(Commertial_Street_window, width=600, height=400, scrollregion=(0, 0, 2000, 2000))
    scrollbar = Scrollbar(Commertial_Street_window, command=canvas.yview, troughcolor="light gray", activerelief=tk.GROOVE, width=20, orient="vertical")
    canvas.config(yscrollcommand=scrollbar.set)

    # Add widgets to display detailed information about Commertial Stree 
    heading_label = tk.Label(
        canvas,
        text="Discover the Beauty of Commertial Street ",
        font=("Great vibes", 20),
        fg="purple",
        
    )
    heading_label.pack(padx=20, pady=20)

    info_label = tk.Label(
        canvas,
        text="\nLocated in the Central Business District of Bangalore, Commercial Street is home to a number of small stores to brand outlets which sell the most delightful variety of products you can find. One of the first shopping areas a newcomer to the city is told about, Commercial Street is a fix for all your shopping needs and weekend entertainment. Needless to say, it is one of the most popular and visited shopping destinations in Bangalore. The lively atmosphere which is always abuzz with activity and the mad, mad rush of the local market make Commercial Street every shopaholic's delight",
        font=("Great Vibes",16),
        fg="red",
        wraplength=1000,
        justify=tk.LEFT
    )
    info_label.pack(padx=20, pady=20)

    additional_info_label = tk.Label(
        canvas,
        text="\nWeather : 20 - 27°C\nLabel : Must Visit\nTimings : 11:00 AM - 8:00 PM",
        font=("Great Vibes", 12),
        fg="green",
        wraplength=500,
        justify=tk.LEFT
    )
    additional_info_label.pack(padx=20, pady=20)

    additional_info_label = tk.Label(
        canvas,
        text="Shopping at Commercial Street:\nCommercial Street a paradise for all the people who wish to own good clothes which won't be heavy on their pocket either. You'll find everything here ranging from quirky outfits for your daily wear to shimmery dresses for your night out, and even beautiful traditional lehengas and saree for that approaching wedding in your family!\nRestaurants at Commercial Streets:Commercial Street has a number of eateries to quench that hunger of yours. From well-known food chains like McDonald's, Krispy Kreme and Tibbs Frankie to small outlets like Khan Saheb Grills and Rolls and Konark restaurant, you'll find everything you can munch on while you find the perfect dress for yourself. You can eat all of this without having to spend too much, which again is amazing for all food junkies out there",
        font=("Great Vibes", 12),
        fg="blue",
        wraplength=800,
        justify=tk.LEFT
    )
    additional_info_label.pack(padx=20, pady=20)

    additional_info_label = tk.Label(
        canvas,
        text="""LOCATION :\nCommercial Street has a number of eateries to quench that hunger of yours. From well-known food chains like McDonald's, Krispy Kreme and Tibbs Frankie to small outlets like Khan Saheb Grills and Rolls and Konark restaurant, you'll find everything you can munch on while you find the perfect dress for yourself. You can eat all of this without having to spend too much, which again is amazing for all food junkies out there""",
        font=("Great Vibes", 10),
        fg="maroon",
        wraplength=800,
        justify=tk.LEFT
    )
    additional_info_label.pack(padx=20, pady=20)

    # Example: Display multiple images
    image_paths = [
        r"images\Commercial_Street,1.jpg",
        r"images\COM2.jpg",
    ]

    # Display images one after the other
    current_image_index = 0
    current_image_label = None

    def show_next_image():
        nonlocal current_image_index, current_image_label
        # Destroy the previous image label if it exists
        if current_image_label:
            current_image_label.destroy()
        current_image_index = (current_image_index + 1) % len(image_paths)
        update_image()

    def update_image():
        nonlocal current_image_index, current_image_label
        img = Image.open(image_paths[current_image_index])
        img = ImageTk.PhotoImage(img)
        current_image_label = tk.Label(canvas, image=img)
        current_image_label.image = img
        canvas.create_window(260, 50, anchor=tk.NW, window=current_image_label)  # Adjust the coordinates

        # Schedule to show the next image after 2000 milliseconds (2 seconds)
        Commertial_Street_window.after(2000, show_next_image)

    # Initial image display
    update_image()

    # Pack the Canvas and Scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y", expand=False)

##Bangalore Palace###

def show_Banglore_Palace_page():
    Bangalore_Palace_window = Toplevel(root)
    Bangalore_Palace_window.title("Bangalore Palace")

    # Create a Canvas with a Scrollbar
    canvas = Canvas(Bangalore_Palace_window, width=600, height=400, scrollregion=(0, 0, 2000, 2000))
    scrollbar = Scrollbar(Bangalore_Palace_window, command=canvas.yview, troughcolor="light gray", activerelief=tk.GROOVE, width=20, orient="vertical")
    canvas.config(yscrollcommand=scrollbar.set)

    # Add widgets to display detailed information about  Bangalore Palace
    heading_label = tk.Label(
        canvas,
        text="Discover the Beauty of Bangalore Palace ",
        font=("Great vibes", 20),
        fg="purple",
        
    )
    heading_label.pack(padx=20, pady=20)

    info_label = tk.Label(
        canvas,
        text="\nThe palace reflects the Tudor style of architecture. Its complex, along with the garden, spreads over an area of 454 acres. The interior of the palace finds motifs, cornices, and wooden carvings on it. Many physical elements inside are the imports from Britain. A gift from the British to the Wadiyars, the coat of arms is painted on the wall in red and white colour. It consists of mythological impressions and intricate floral design. In the centre is Ganda Bherunda, a mythological two-headed bird while the other side has a mythological animal with features of the head of both the elephant and lion, symbolising royalty and power",
        font=("Great Vibes", 16),
        fg="red",
        wraplength=1000,
        justify=tk.LEFT
    )
    info_label.pack(padx=20, pady=20)

    additional_info_label = tk.Label(
        canvas,
        text="\nWeather : 20 - 27°C\nLabel : Must Visit\nTags : Palace\nTimings : 10:00 AM - 5:30 PM ",
        font=("Great Vibes", 12),
        fg="green",
        wraplength=500,
        justify=tk.LEFT
    )
    additional_info_label.pack(padx=20, pady=20)

    additional_info_label = tk.Label(
        canvas,
        text="Things To Do In Bangalore Palace:\nMassive 454 acre campus\n•Bengaluru Palace building spreads over one acre (45000 sq ft)\n•34 bedrooms and a swimming pool\n•palaceified watch towers, turrets\n•Elegant interiors with wooden carvings, paintings and motifs\n•Well maintained exterior with green plants covering portion of the palace walls\n•Wooden fan and imported artifacts",
        font=("Great Vibes", 12),
        fg="blue",
        wraplength=800,
        justify=tk.LEFT
    )
    additional_info_label.pack(padx=20, pady=20)

    additional_info_label = tk.Label(
        canvas,
        text="""LOCATION :\nBengaluru Palace is 5.3 kms north of Bengaluru city centre (Majestic) and 33 kms from Bengaluru international airport. Bengaluru Cantonment is the nearest railway station (3 kms). Mantri Mall Malleshwaram is the closest metro (4 kms). Bengaluru Palace can be reached using public transport or taxi from all parts of Bengaluru""",
        font=("Great Vibes", 10),
        fg="maroon",
        wraplength=800,
        justify=tk.LEFT
    )
    additional_info_label.pack(padx=20, pady=20)

    # Example: Display multiple images
    image_paths = [
        r"images\bannerghatta 2.jpg",
        r"images\Bannerghatta-NationalPark-4.jpg",
        r"images\bannerghattanationalpark3.jpg",
        r"images\BG1.jpg"
    ]

    # Display images one after the other
    current_image_index = 0
    current_image_label = None

    def show_next_image():
        nonlocal current_image_index, current_image_label
        # Destroy the previous image label if it exists
        if current_image_label:
            current_image_label.destroy()
        current_image_index = (current_image_index + 1) % len(image_paths)
        update_image()

    def update_image():
        nonlocal current_image_index, current_image_label
        img = Image.open(image_paths[current_image_index])
        img = ImageTk.PhotoImage(img)
        current_image_label = tk.Label(canvas, image=img)
        current_image_label.image = img
        canvas.create_window(260, 50, anchor=tk.NW, window=current_image_label)  # Adjust the coordinates

        # Schedule to show the next image after 2000 milliseconds (2 seconds)
        Bangalore_Palace_window.after(2000, show_next_image)

    # Initial image display
    update_image()

    # Pack the Canvas and Scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y", expand=False)



root = tk.Tk()
root.title("BON VOYAGE")
root.geometry("600x400")

background_image = PhotoImage(file=r"images\bonvoyage.png")  # Replace with your image file

# Create a label with the image
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

heading_label = tk.Label(
    root,
    text="Welcome to Our Website - Bon Voyage to an Exciting Journey",
    font=("Great Vibes", 32),
    fg="black",
    bg="white"
)
heading_label.pack()

destination_var = tk.StringVar()
destination_var.set(destination_options[0])

destination_combobox = ttk.Combobox(root, textvariable=destination_var, values=destination_options)
destination_combobox.pack(pady=20)


select_button = tk.Button(root, text="EXPLORE", command=on_select_destination)
select_button.pack(pady=20)

root.mainloop()
