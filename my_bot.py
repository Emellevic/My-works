

def make_an_enquiry():
    print("Make an enquiry about:\n1.Our work hours.\n2.Our services\n3.Our location")
    try:
        enquiry = int(input("please select a number: "))
    except ValueError:
        print ("select either 1 or 2")
    except UnboundLocalError:
        return
    if enquiry == 1:
        print("we are open from 8:00am till 9:00pm.")
    elif enquiry == 2:
        print("we offer:\n-> Data topups and other Vtu's.\n-> Graphics and logo designing. \n-> computer programming.")
    elif enquiry == 3:
        print ("We are currently located in Tungan-Maje Gwagwalada Area Council F.C.T Abuja")
    else:
        print ("Select either 1, 2, or 3.")
        return()


def place_an_order():
    print("How can we help you today?\n1.Data Purchase \n2.Graphics designing\n3.Logo designing\n4.computer programming\n5.Other Vtu's")
    try:
        order = int(input("please select a number: "))
    except ValueError:
        return
    if order == 1:
        network = input("type in network name: ")
        if not network:
            return
        chosen_network = network.upper()

        if chosen_network == "MTN":
            print("\n1.500mb -> N200\n2.1Gb -> N350\n3.2Gb -> N700\n4.3Gb -> N1050\n5.4Gb -> 1400\n ALL PLANS ARE VALID FOR 30 DAYS")
            try:
                plan = int(input("Choose a plan: "))
            except ValueError:
                print("Select a digit!")
                return
            try:
                recipient = int(input("Enter recipient number: "))
                recipient_num = str(recipient)
                if len(recipient_num) > 10 or len(recipient_num) < 10:
                    print ("invalid number! Check the recipient number and try again")
                    return
            except ValueError:
                print ("Enter recipient nummber")
                return
            print(f"YOUR ORDER:\nNetwork: {chosen_network}\nPlan: {plan}\nRecipient: {recipient}")
            print ("Is your above order correct? ")
            confirmation = input("YES/NO: ").upper()
            if confirmation == "YES":
                print ("Make payment to \n9114962166\nOpay Digital Services Limited\nObiete Uzoamaka Patricia\nSend me the reciept of your payment and you will recieve your order shortly after.")
            else:
                return

        elif chosen_network == "AIRTEL":
            print("\n1.500mb -> N200\n2.1Gb -> N350\n3.2Gb -> N700\n4.3Gb -> N1050\n5.4Gb -> 1400\n ALL PLANS ARE VALID FOR 30 DAYS")
            try:
                plan = int(input("Choose a plan: "))
            except ValueError:
                print("Select a digit!")
                return
            try:
                recipient = int(input("Enter recipient number: "))
                recipient_num = str(recipient)
                if len(recipient_num) > 10 or len(recipient_num) < 10:
                    print ("invalid number! Check the recipient number and try again")
                    return
            except ValueError:
                print ("Enter recipient nummber")
                return
            print(f"YOUR ORDER:\nNetwork: {chosen_network}\nPlan: {plan}\nRecipient: {recipient}")
            print ("Is your above order correct? ")
            confirmation = input("YES/NO: ").upper()
            if confirmation == "YES":
                print ("Make payment to \n9114962166\nOpay Digital Services Limited\nObiete Uzoamaka Patricia\nSend me the reciept of your payment and you will recieve your order shortly after.")
            else:
                return

        elif chosen_network == "GLO":
            print("\n1.500mb -> N200\n2.1Gb -> N300\n3.2Gb -> N600\n4.3Gb -> N900\n5.4Gb -> 1200\n ALL PLANS ARE VALID FOR 30 DAYS")
            try:
                plan = int(input("Choose a plan: "))
            except ValueError:
                print("Select a digit!")
                return
            try:
                recipient = int(input("Enter recipient number: "))
                recipient_num = str(recipient)
                if len(recipient_num) > 10 or len(recipient_num) < 10:
                    print ("invalid number! Check the recipient number and try again")
                    return
            except ValueError:
                print ("Enter recipient nummber")
                return
            print(f"YOUR ORDER:\nNetwork: {chosen_network}\nPlan: {plan}\nRecipient: {recipient}")
            print ("Is your above order correct? ")
            confirmation = input("YES/NO: ").upper()
            if confirmation == "YES":
                print ("Make payment to \n9114962166\nOpay Digital Services Limited\nObiete Uzoamaka Patricia\nSend me the reciept of your payment and you will recieve your order shortly after.")
            else:
                return

        elif chosen_network == "9MOBILE":
            print("\n1.500mb -> N200\n2.1Gb -> N300\n3.2Gb -> N600\n4.3Gb -> N900\n5.4Gb -> 1200\n ALL PLANS ARE VALID FOR 30 DAYS")
            try:
                plan = int(input("Choose a plan: "))
            except ValueError:
                print("Select a digit!")
                return
            try:
                recipient = int(input("Enter recipient number: "))
                recipient_num = str(recipient)
                if len(recipient_num) > 10 or len(recipient_num) < 10:
                    print ("invalid number! Check the recipient number and try again")
                    return
            except ValueError:
                print ("Enter recipient nummber")
                return
            print(f"YOUR ORDER:\nNetwork: {chosen_network}\nPlan: {plan}\nRecipient: {recipient}")
            print ("Is your above order correct? ")
            confirmation = input("YES/NO: ").upper()
            if confirmation == "YES":
                print ("Make payment to \n9114962166\nOpay Digital Services Limited\nObiete Uzoamaka Patricia\nSend me the reciept of your payment and you will recieve your order shortly after.")
            else:
                return

    elif order == 2:
        print("Make a well detailed description of the kind of graphics you need and include relevant details. e.g flyers for birthday or events")
        graphics_desc = input("Description: ")
    elif order == 3:
        print("Give details of the kind of logo you desire for your brand. Include brand colour if any.")
        logo_desc = input("Description: ")
    elif order == 4:
        print("Make a well detailed description of the kind of computer program you need and include relevant details. e.g samples if any.")
        comp_prog_desc = input("Description: ")
    else:
        print("Give details of the Virtual Topup Services you are in need of")
        vtu_desc = input("Description: ")


def run():
    print ("Hi, nice to meet you. ")
    name = input("please what's your name? ")
    if not name:
        return
    print (f"Good day {name} how can i help you today?\n1.Make an enquiry\n2.Place an order")
    try:
        choice = int(input("Enter 1 or 2: " ))
    except ValueError:
        return
    if choice == 1:
        make_an_enquiry()
    elif choice == 2:
        place_an_order()
    else:
        return()

run()





# To integrate your existing functions into a Tkinter application, we'll follow a structured approach. Each function (`make_an_enquiry` and `place_an_order`) will be connected to GUI elements such as buttons and entry fields. Here’s how you can do it:

# import tkinter as tk
# from tkinter import messagebox

# # Function to make an enquiry
# def make_an_enquiry():
#     enquiry_text = (
#         "Make an enquiry about:\n1. Our work hours.\n2. Our services\n3. Our location"
#     )
#     enquiry_text.config(text=enquiry_text)

#     def process_enquiry():
#         try:
#             enquiry = int(enquiry_entry.get())
#             if enquiry == 1:
#                 result_text = "We are open from 8:00am till 9:00pm."
#             elif enquiry == 2:
#                 result_text = "We offer:\n-> Data topups and other Vtu's.\n-> Graphics and logo designing.\n-> Computer programming."
#             elif enquiry == 3:
#                 result_text = "We are currently located in Tungan-Maje Gwagwalada Area Council F.C.T Abuja"
#             else:
#                 result_text = "Select either 1, 2, or 3."
#             enquiry_result.config(text=result_text)
#         except ValueError:
#             messagebox.showerror("Error", "Please enter a valid number.")

#     enquiry_frame = tk.Frame(root, padx=10, pady=10)
#     enquiry_frame.grid(row=1, column=0, columnspan=2)

#     enquiry_entry = tk.Entry(enquiry_frame, width=10)
#     enquiry_entry.grid(row=0, column=0)

#     enquiry_button = tk.Button(enquiry_frame, text="Enquire", command=process_enquiry)
#     enquiry_button.grid(row=0, column=1)

#     enquiry_result = tk.Label(enquiry_frame, text="")
#     enquiry_result.grid(row=1, column=0, columnspan=2)


# # Function to place an order
# def place_an_order():
#     order_text = (
#         "How can we help you today?\n1. Data Purchase\n2. Graphics designing\n3. Logo designing\n4. Computer programming\n5. Other Vtu's"
#     )
#     order_text.config(text=order_text)

#     def process_order():
#         try:
#             order = int(order_entry.get())
#             if order == 1:
#                 network = network_entry.get().upper()
#                 if network not in ["MTN", "AIRTEL", "GLO", "9MOBILE"]:
#                     messagebox.showerror("Error", "Invalid network name.")
#                     return

#                 plans = {
#                     "MTN": "\n1. 500mb -> N200\n2. 1Gb -> N350\n3. 2Gb -> N700\n4. 3Gb -> N1050\n5. 4Gb -> 1400\n ALL PLANS ARE VALID FOR 30 DAYS",
#                     "AIRTEL": "\n1. 500mb -> N200\n2. 1Gb -> N350\n3. 2Gb -> N700\n4. 3Gb -> N1050\n5. 4Gb -> 1400\n ALL PLANS ARE VALID FOR 30 DAYS",
#                     "GLO": "\n1. 500mb -> N200\n2. 1Gb -> N300\n3. 2Gb -> N600\n4. 3Gb -> N900\n5. 4Gb -> 1200\n ALL PLANS ARE VALID FOR 30 DAYS",
#                     "9MOBILE": "\n1. 500mb -> N200\n2. 1Gb -> N300\n3. 2Gb -> N600\n4. 3Gb -> N900\n5. 4Gb -> 1200\n ALL PLANS ARE VALID FOR 30 DAYS",
#                 }

#                 if network in plans:
#                     order_result.config(
#                         text=f"{plans[network]}\n\nEnter recipient number:"
#                     )
#                 else:
#                     messagebox.showerror("Error", "Invalid network name.")
#             elif order == 2:
#                 graphics_desc = graphics_entry.get()
#                 # Process graphics order as needed
#             elif order == 3:
#                 logo_desc = logo_entry.get()
#                 # Process logo order as needed
#             elif order == 4:
#                 comp_prog_desc = comp_prog_entry.get()
#                 # Process computer programming order as needed
#             elif order == 5:
#                 vtu_desc = vtu_entry.get()
#                 # Process other VTU services order as needed
#             else:
#                 messagebox.showerror("Error", "Invalid order number.")
#         except ValueError:
#             messagebox.showerror("Error", "Please enter a valid number.")

#     order_frame = tk.Frame(root, padx=10, pady=10)
#     order_frame.grid(row=1, column=0, columnspan=2)

#     order_entry = tk.Entry(order_frame, width=10)
#     order_entry.grid(row=0, column=0)

#     order_button = tk.Button(order_frame, text="Place Order", command=process_order)
#     order_button.grid(row=0, column=1)

#     order_result = tk.Label(order_frame, text="")
#     order_result.grid(row=1, column=0, columnspan=2)

#     network_entry = tk.Entry(order_frame, width=10)
#     network_entry.grid(row=2, column=0)

#     graphics_entry = tk.Entry(order_frame, width=30)
#     logo_entry = tk.Entry(order_frame, width=30)
#     comp_prog_entry = tk.Entry(order_frame, width=30)
#     vtu_entry = tk.Entry(order_frame, width=30)


# # Create the main application window
# root = tk.Tk()
# root.title("Service Inquiry and Ordering")

# # Welcome message
# welcome_label = tk.Label(root, text="Hi, nice to meet you.")
# welcome_label.grid(row=0, column=0, columnspan=2)

# name_label = tk.Label(root, text="Please enter your name:")
# name_label.grid(row=1, column=0)

# name_entry = tk.Entry(root, width=20)
# name_entry.grid(row=1, column=1)


# # Run the Tkinter main loop
# root.mainloop()
