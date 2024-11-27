import tkinter as tk
import time
from datetime import datetime
import os
import random
open("Patients_Data.txt", "a")
open("Admin_Data.txt", "a")
open("Doctor_Data.txt", "a")
open("Appointment_Data.txt", "a")
class LoginValidator:
    def __init__(self, filename):
        self.filename = filename

    def validate_login(self, email, password):
        with open(self.filename, "r") as file:
            #reads all the lines in the file
            lines = file.readlines()

        # Check if the number of lines is divisible by 6 (cos each time a doctor signs up, 6 datapoints are taken, this confirms a doctor(s) have signed up)
        if len(lines) % 6 == 0:
            # Iterate over pairs of lines using zip     lines[4::6]  and lines[5::6]    This means out of    6  lines,    it extracts the 4th line [4::6]    and    the   5th line [5::6] out of that block of 6 lines.  
            #Thus for every doctor submission (6 lines), the email and password are available to be compared against the input.
            for email_line, password_line in zip(lines[4::6], lines[5::6]):
                #.strip() removes leading and trailing whitespace
                #.split(": ")[1]  removes everything before adn incl colon in 'Doctor Email: bob@gmail.com'
                #then [1] stores it into the first element of the list stored_email
                stored_email = email_line.strip().split(": ")[1]
                stored_password = password_line.strip().split(": ")[1]

                if email == stored_email and password == stored_password:
                    return True
        return False




#---START DASHBOARD-----

class Start_Dashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Medical Management System")
        
        self.create_dashboard_widgets()

    def create_dashboard_widgets(self):
        tk.Label(self.root, text="Are You A Doctor, Patient or Adminstrator?").grid(column=3, row=0)

        tk.Button(self.root, text="I am a Patient", command=self.show_patient_signup).grid(row=1, column=0)

        tk.Button(self.root, text="I am a Doctor", command=self.show_doctor_signup).grid(row=1, column=1)

        tk.Button(self.root, text="I am an Admin", command=self.show_admin_signup).grid(row=1, column=2)


    def show_patient_signup(self):
        # Create an instance of Patient_SignUp_GUI when the patient button is clicked
        patient_window = tk.Toplevel(self.root)
        patient_signup = Patient_SignUp_GUI(patient_window)

    def show_doctor_signup(self):
        doctor_window = tk.Toplevel(self.root)
        doctor_signup = Doctor_Signup_GUI(doctor_window)

    def show_admin_signup(self):
        admin_window = tk.Toplevel(self.root)
        admin_signup = Admin_Signup_GUI(admin_window)




#----PATIENT CLASSES-----
class Patient_SignUp_GUI:
    def __init__(self, patient_window):
        self.patient_window = patient_window 
        self.patient_window.title("Patient Data Signup")
        
        self.Name = tk.StringVar()
        self.Age = tk.StringVar()
        self.Address = tk.StringVar()
        self.Phone = tk.StringVar()
        self.Email = tk.StringVar()
        self.Password = tk.StringVar()

        # Make entry widgets instance attributes
        self.Name_Entry = tk.Entry(self.patient_window, textvariable=self.Name)
        self.Age_Entry = tk.Entry(self.patient_window, textvariable=self.Age)
        self.Address_Entry = tk.Entry(self.patient_window, textvariable=self.Address)
        self.Phone_Entry = tk.Entry(self.patient_window, textvariable=self.Phone)
        self.Email_Entry = tk.Entry(self.patient_window, textvariable=self.Email)

        self.Password_Entry = tk.Entry(self.patient_window, textvariable=self.Password)

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.patient_window, text="Patient's Name:").grid(row=0, column=0, padx=10, pady=10)
        self.Name_Entry.grid(row=0, column=1)

        tk.Label(self.patient_window, text="Patient's Age:").grid(row=1, column=0, padx=10, pady=10)
        self.Age_Entry.grid(row=1, column=1)

        tk.Label(self.patient_window, text="Patient's Address:").grid(row=2, column=0, padx=10, pady=10)
        self.Address_Entry.grid(row=2, column=1)

        tk.Label(self.patient_window, text="Patient's Phone:").grid(row=3, column=0, padx=10, pady=10)
        self.Phone_Entry.grid(row=3, column=1)

        tk.Label(self.patient_window, text="Patient's Email:").grid(row=4, column=0, padx=10, pady=10)
        self.Email_Entry.grid(row=4, column=1)

        tk.Label(self.patient_window, text="Set Your Password:").grid(row=5, padx=10, pady=10)
        self.Password_Entry.grid(row=5, column=1)

        tk.Button(self.patient_window, text="Submit", command=self.submit).grid(row=6, column=0, columnspan=2, pady=20)


        tk.Label(self.patient_window, text="Already Registered?").grid(row=8, column=0, columnspan=2)

        tk.Button(self.patient_window, text="Login as Patient ", command=self.Show_Patient_Login).grid(row=9, column=0, columnspan=2, pady=1)


        

    def submit(self):
        Patients_Name = self.Name.get()
        Patients_Age = int(self.Age.get())
        Patients_Address = self.Address.get()
        Patients_Phone = self.Phone.get()
        Patients_Email = self.Email.get()
        Patients_Password = self.Password.get()

        # Clear Input Fields
        self.Name_Entry.delete(0, 'end')
        self.Age_Entry.delete(0, 'end')
        self.Address_Entry.delete(0, 'end') 
        self.Phone_Entry.delete(0, 'end')        
        self.Email_Entry.delete(0, 'end')
        self.Password_Entry.delete(0, 'end')
        
        # Use file.write with formatted string
        #this block of code does not allow patients to sign up with duplicate emails
        open("Patients_Data.txt", "a")

        with open("Patients_Data.txt", "r") as file:
            if Patients_Email in file.read():
                email_used = tk.Label(self.patient_window, text="Email already in use. Choose a different one.")
                email_used.grid(row=10, columnspan=2, pady=1)


            else:
                with open("Patients_Data.txt", "a") as append_file: 
                    append_file.write("Patient: {}\nAge: {}\nAddress: {}\nPhone: {}\nEmail: {}\nPassword: {}\n".format(
                    Patients_Name, Patients_Age, Patients_Address, Patients_Phone, Patients_Email, Patients_Password))


    def Show_Patient_Login(self):
        Patient_Login_Window = tk.Toplevel(self.patient_window)
        Patient_Login_win = Patient_Login_Window_GUI(Patient_Login_Window)




class Patient_Login_Window_GUI:
    def __init__(self, Patient_Login_Window):
        self.Patient_Login_Window = Patient_Login_Window
        
        self.Patient_Login_Window.title("Patient Login")

        self.Email = tk.StringVar()
        self.Password = tk.StringVar()

        self.Email_Entry = tk.Entry(self.Patient_Login_Window, textvariable=self.Email)
        self.Password_Entry = tk.Entry(self.Patient_Login_Window, textvariable=self.Password)

        self.create_patient_login_widgets()
        self.Patient_Login_Window.mainloop()

    def create_patient_login_widgets(self):
        tk.Label(self.Patient_Login_Window, text="Patient Login").grid(row=0, columnspan=2, padx=10, pady=10)
        tk.Label(self.Patient_Login_Window, text="Enter Your Email:").grid(row=1, column=0, padx=10, pady=10)
        self.Email_Entry.grid(row=1, column=1)
        tk.Label(self.Patient_Login_Window, text="Enter Your Password:").grid(row=2, column=0, padx=10, pady=10)
        self.Password_Entry.grid(row=2, column=1)
        tk.Button(self.Patient_Login_Window, text="Login", command=self.show_patient_dashboard).grid(columnspan=2, row=3, pady=1)

    def show_patient_dashboard(self):
        email = self.Email.get()
        password = self.Password.get()

        patient_validator = LoginValidator("Patients_Data.txt")

        if patient_validator.validate_login(email, password):
            print("Patient Login Successful")
            self.Show_Patient_Dashboard(email)
        else:
            incorrect_creds = tk.Label(self.Patient_Login_Window, text="Invalid email or password")
            print("Invalid email or password") 
            incorrect_creds.grid(row=4, columnspan=2, pady=10)
        


    def Show_Patient_Dashboard(self, email):
        Patient_Dashboard_Window = tk.Toplevel(self.Patient_Login_Window)
        Patient_Dashboard_Win = Patient_Dashboard(Patient_Dashboard_Window, email) 



class Patient_Dashboard:
    def __init__(self, Patient_Dashboard_Window, email):
        self.Patient_Dashboard_Window = Patient_Dashboard_Window
        self.Patient_Dashboard_Window.title("Patient Dashboard")
        self.email = email
        self.patient_name = self.get_patient_name()
        self.patient_age = self.get_patient_age()
        self.patient_address = self.get_patient_address()
        self.patient_phone = self.get_patient_phone()
        self.create_pdash_widgets()
    
    def get_patient_name(self):
        with open("Patients_Data.txt", "r") as file:
            lines = file.readlines()


        #FINDING PATIENT EMAIL IN DOCUMENT
        for i, line in enumerate(lines):
            if "Email: {}".format(self.email) in line:
                #found email in doc, go back 4 lines to get name
                patient_name_line = lines[i-4].strip()
                return patient_name_line.split(": ")[1]
    
    def get_patient_age(self):
        with open("Patients_Data.txt", "r") as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            if "Email: {}".format(self.email) in line:
                patient_age_line = lines[i-3].strip()
                return patient_age_line.split(": ")[1]

    def get_patient_address(self):
        with open("Patients_Data.txt", "r") as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            if "Email: {}".format(self.email) in line:
                patient_address_line = lines[i-2].strip()
                return patient_address_line.split(": ")[1]

    def get_patient_phone(self):
        with open("Patients_Data.txt", "r") as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            if "Email: {}".format(self.email) in line:
                patient_phone_line = lines[i-1].strip()
                return patient_phone_line.split(": ")[1]


    def create_pdash_widgets(self):
    
        p_welcome = tk.Label(self.Patient_Dashboard_Window, text="Hello {},\nWelcome To Your Patient Dashboard".format(self.patient_name))

        p_welcome.grid(row=0, columnspan=2, pady=15)
        
        self.show_personal_details()
        #code showing appointments. approved and pending. (put in row 2)
        self.show_current_appointments() #come to this LATER

        self.Appoint_btn = tk.Button(self.Patient_Dashboard_Window, text="Book An Appointment", command=self.Show_Book_Appointment)
                               
        self.Appoint_btn.grid(row=4, columnspan=2, pady=10)


    def Show_Book_Appointment(self):
        #text variables
        self.Appoint_btn.grid_forget() 
        self.Condition = tk.StringVar()
        self.Date = tk.StringVar()
        self.patient_details.grid_forget()


        self.hide_current_appointments()

       
        
        self.Condition_Label = tk.Label(self.Patient_Dashboard_Window, text="What Are You Suffering From?")
        self.Condition_Label.grid(row=1, column=0)
        self.Condition_Entry = tk.Entry(self.Patient_Dashboard_Window, textvariable=self.Condition)
        self.Condition_Entry.grid(row=1, column=1)
        
        self.Date_Label = tk.Label(self.Patient_Dashboard_Window, text="Choose Appointment Date (dd/mm/yy)")
        self.Date_Label.grid(row=2, column=0)
        self.Date_Entry = tk.Entry(self.Patient_Dashboard_Window, textvariable=self.Date)
        self.Date_Entry.grid(row=2, column=1)

        self.Approval_btn = tk.Button(self.Patient_Dashboard_Window, text="Submit Appointment For Approval", command=self.Submit_Appointment)
        self.Approval_btn.grid(row=4, columnspan=2, pady=15)

        self.backdash = tk.Button(self.Patient_Dashboard_Window, text="Back To Dashboard\n(Refresh Appointments)", command=self.back_to_dashboard)
        self.backdash.grid(row=6, columnspan=2, pady=15)

    def hide_current_appointments(self):
        # Hide the current appointments section
        try:
            self.appointments.grid_forget()
        except AttributeError:
            pass

    def back_to_dashboard(self):
        self.Date_Entry.grid_forget()
        self.Date_Label.grid_forget()
        self.Condition_Entry.grid_forget()
        self.Condition_Label.grid_forget()
        self.backdash.grid_forget()
        self.Approval_btn.grid_forget()
        try:
            self.appoint_submitted.grid_forget()
        except AttributeError:
            pass

        self.show_current_appointments()
        self.create_pdash_widgets()



    def Submit_Appointment(self):
        Condition_submit = self.Condition.get()
        Date_submit = self.Date.get()
        Appoint_num = random.randint(1,10000)


        with open("Appointment_Data.txt", "a") as file:
            file.write("Patient Name: {}\nPatient Email: {}\nCondition: {}\nAppointment Date: {}\nStatus: PENDING APPROVAL\nDoctor: Not Assigned\nAppointment_Number: {}\n".format(self.patient_name, self.email, Condition_submit, Date_submit, Appoint_num))

        #clear fields
        self.Condition_Entry.delete(0, "end")
        self.Date_Entry.delete(0, "end")

        self.appoint_submitted = tk.Label(self.Patient_Dashboard_Window, text="Thanks! Your appointment has been submitted.")

        self.appoint_submitted.grid(row=5, columnspan=2) 

    def show_personal_details(self):
        #show logged in patiens personal details
        self.patient_details = tk.Label(self.Patient_Dashboard_Window, text="Name: {}\nAge: {}\nAddress: {}\nPhone: {}\nEmail: {}".format(self.patient_name, self.patient_age, self.patient_address, self.patient_phone, self.email))
        self.patient_details.grid(row=2, column=0)

    #gathering data for the show_current_appointments function
    def get_appointment_reason(self):
        with open("Appointment_Data.txt", "r") as file:
            lines = file.readlines()
        for i, line in enumerate(lines):
            if "Email: {}".format(self.email) in line:
                appointment_reason_line = lines[i+1].strip()
                return appointment_reason_line.split(": ")[1]

    def get_appointment_date(self):
        with open("Appointment_Data.txt", "r") as file:
            lines = file.readlines()
        for i, line in enumerate(lines):
            if "Email: {}".format(self.email) in line:
                appointment_date_line = lines[i+2].strip()
                return appointment_date_line.split(": ")[1]

    def get_appointment_status(self):
        with open("Appointment_Data.txt", "r") as file:
            lines = file.readlines()
        for i, line in enumerate(lines):
            if "Email: {}".format(self.email) in line:
                appointment_status_line = lines[i+3].strip()
                return appointment_status_line.split(": ")[1]

    def get_appointment_doctor(self):
        with open("Appointment_Data.txt", "r") as file:
            lines = file.readlines()
        for i, line in enumerate(lines):
            if "Email {}".format(self.email) in line:
                appointment_doctor_line = lines[i+4].strip()
                return appointment_doctor_line.split(": ")[1]

    def show_current_appointments(self):
        print("showing current appointments")
        # Display current appointments in the Tkinter window
        appointment_data = self.read_appointment_data()
        if appointment_data:
            tk.Label(self.Patient_Dashboard_Window, text="Current Appointments").grid(row=7, column=0, columnspan=2, pady=10)

            # Display appointments side by side
            for i, appointment in enumerate(appointment_data, start=4):
                self.appointments = tk.Label(self.Patient_Dashboard_Window, text=appointment)
                self.appointments.grid(row=[i+5], column=0, columnspan=2, pady=5)
        else:
            tk.Label(self.Patient_Dashboard_Window, text="No appointments to display.").grid(row=3, column=0, columnspan=2, pady=10)

    def read_appointment_data(self):
        # Read appointment data from the file based on patient's email
        appointment_data = []
        with open("Appointment_Data.txt", "r") as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                if "Patient Email: {}".format(self.email) in line:
                    appointment_reason_line = lines[i + 1].strip()
                    appointment_date_line = lines[i + 2].strip()
                    appointment_status_line = lines[i + 3].strip()
                    appointment_doctor_line = lines[i + 4].strip()

                    appointment_info = (
                        f"Reason: {appointment_reason_line.split(': ')[1]}",
                        f"Date: {appointment_date_line.split(': ')[1]}",
                        f"Status: {appointment_status_line.split(': ')[1]}",
                        f"Doctor: {appointment_doctor_line.split(': ')[1]}",
                        "-" * 30  # Separation line
                    )
                    appointment_data.extend(appointment_info)

        return appointment_data





#----DOCTOR CLASSES------
class Doctor_Signup_GUI:
    def __init__(self, doctor_window):
       self.doctor_window = doctor_window
       self.doctor_window.title("Doctor Signup")

       self.Name = tk.StringVar()
       self.Age = tk.StringVar()
       self.Address = tk.StringVar()
       self.Phone = tk.StringVar()
       self.Email = tk.StringVar()
       self.Password = tk.StringVar()

       #Entry Widgets
       self.Name_Entry = tk.Entry(self.doctor_window, textvariable=self.Name)
       self.Age_Entry = tk.Entry(self.doctor_window, textvariable=self.Age)
       self.Address_Entry = tk.Entry(self.doctor_window, textvariable=self.Address)
       self.Phone_Entry = tk.Entry(self.doctor_window, textvariable=self.Phone)
       self.Email_Entry = tk.Entry(self.doctor_window, textvariable=self.Email)
       self.Password_Entry = tk.Entry(self.doctor_window, textvariable=self.Password)

       self.create_doctor_widgets()

    def create_doctor_widgets(self):
        tk.Label(self.doctor_window, text="Doctor's Name:").grid(row=0, column=0, padx=10, pady=10)
        self.Name_Entry.grid(row=0, column=1)

        tk.Label(self.doctor_window, text="Doctor's Age:").grid(row=1, column=0, padx=10, pady=10)
        self.Age_Entry.grid(row=1, column=1)

        tk.Label(self.doctor_window, text="Doctor's Address:").grid(row=2, column=0, padx=10, pady=10)
        self.Address_Entry.grid(row=2, column=1)

        tk.Label(self.doctor_window, text="Doctor's Phone:").grid(row=3, column=0, padx=10, pady=10)
        self.Phone_Entry.grid(row=3, column=1)

        tk.Label(self.doctor_window, text="Doctor's Email:").grid(row=4, column=0, padx=10, pady=10)
        self.Email_Entry.grid(row=4, column=1)

        tk.Label(self.doctor_window, text="Set Your Password:").grid(row=5, column=0, padx=10, pady=10)
        self.Password_Entry.grid(row=5, column=1)

        tk.Button(self.doctor_window, text="Submit", command=self.submit).grid(row=6, column=0, columnspan=2, pady=10)

        tk.Label(self.doctor_window, text="Already Registered?").grid(row=7, column=0, columnspan=2)

        tk.Button(self.doctor_window, text="Login as Doctor", command=self.Show_Doctor_Login).grid(row=8, column=0, columnspan=2, pady=1)


    def submit(self):
        #Get submitted info
        Doctor_Name = self.Name_Entry.get()
        Doctor_Email = self.Email_Entry.get()
        Doctor_Password = self.Password_Entry.get()
        Doctor_Age = self.Age_Entry.get()
        Doctor_Address = self.Address_Entry.get()
        Doctor_Phone = self.Phone_Entry.get()

        #Clear Fields
        self.Name_Entry.delete(0, "end")
        self.Email_Entry.delete(0, "end")
        self.Password_Entry.delete(0, "end")
        self.Age_Entry.delete(0, "end")
        self.Address_Entry.delete(0, "end")
        self.Phone_Entry.delete(0, "end")

        #write to file (this occurs each time btn is clicked) 
        #this block of code also checks if a different doc ahs already signed up with the email or not.
        open("Doctor_Data.txt", "a")

        with open("Doctor_Data.txt", "r") as file:
            if Doctor_Email in file.read():
                email_used = tk.Label(self.doctor_window, text="Email already in use. Choose a different one.")
                email_used.grid(row=10, columnspan=2, pady=1)


            else:
                with open("Doctor_Data.txt", "a") as append_file:
                    append_file.write("Doctor Name: {}\nDoctor Age: {}\nDoctor Address: {}\nDoctor Phone: {}\nDoctor Email: {}\nDoctor Password: {}\n".format(Doctor_Name, Doctor_Age, Doctor_Address, Doctor_Phone, Doctor_Email, Doctor_Password))


    def Show_Doctor_Login(self):
        #Function to create the initial doctor login window on btn click, then gets passed to unique Doctor_Login_Window class
        Doctor_Window = tk.Toplevel(self.doctor_window)
        doctor_login_win = Doctor_Login_Window_GUI(Doctor_Window)

class Doctor_Login_Window_GUI:
    def __init__(self, Doctor_Window):
        self.Doctor_Login_Window = Doctor_Window
        self.Doctor_Login_Window.title("Doctor Login")

        self.Email = tk.StringVar()
        self.Password = tk.StringVar()

        self.Email_Entry = tk.Entry(self.Doctor_Login_Window, textvariable=self.Email)

        self.Password_Entry = tk.Entry(self.Doctor_Login_Window, textvariable=self.Password)

        self.create_DL_widgets()
        self.Doctor_Login_Window.mainloop()

    def create_DL_widgets(self):
        tk.Label(self.Doctor_Login_Window, text="Doctor Login").grid(row=0, columnspan=2, padx=10, pady=10)
        tk.Label(self.Doctor_Login_Window, text="Enter Your Email:").grid(row=1, column=0, padx=10, pady=10)
        self.Email_Entry.grid(row=1, column=1)
        tk.Label(self.Doctor_Login_Window, text="Enter Your Password:").grid(row=2, column=0, padx=10, pady=10)
        self.Password_Entry.grid(row=2, column=1)
        tk.Button(self.Doctor_Login_Window, text="Login", command=self.show_doctor_dashboard).grid(row=3, columnspan=2, pady=1)

    def show_doctor_dashboard(self):
        email = self.Email.get()
        password = self.Password.get()

        doctor_validator = LoginValidator("Doctor_Data.txt")

        if doctor_validator.validate_login(email, password):
            print("Doctor Login Successful")
            self.Show_Doctor_Dashboard(email)
        else:
            print("Invalid email or password")


    def Show_Doctor_Dashboard(self, email):
        Doctor_Dashboard_Window = tk.Toplevel(self.Doctor_Login_Window)
        Doctor_Dashboard_Win = Doctor_Dashboard(Doctor_Dashboard_Window, email)

# ---- DOCTOR DASHBOARD ----
class Doctor_Dashboard:
    def __init__(self, Doctor_Dashboard_Window, email):
        self.Doctor_Dashboard_Window = Doctor_Dashboard_Window
        self.Doctor_Dashboard_Window.title("Doctor Dashboard")
        self.email = email
        self.doctor_name = self.get_doctor_name()
        self.create_ddash_widgets()
        print(self.email)
    def get_doctor_name(self):
        with open("Doctor_Data.txt", "r") as file:
            lines = file.readlines()


        #FINDING DOCTOR EMAIL IN DOCUMENT
        for i, line in enumerate(lines):
            if "Email: {}".format(self.email) in line:
                #found email in doc, go back 4 lines to get name
                doctor_name_line = lines[i-4].strip()
                return doctor_name_line.split(": ")[1]

    def get_assigned_patients(self):
        assigned_patients = []
        with open("Appointment_Data.txt", "r") as file:
            lines = file.readlines()

        # FINDING APPOINTMENTS FOR THE SPECIFIC DOCTOR
        for i in range(0, len(lines), 7):  # Assuming appointments are structured in blocks of 7 lines
            if f"Doctor: {self.email}" in lines[i + 5].strip():
                patient_name = lines[i].strip().split(": ")[1]
                patient_email = lines[i + 1].strip().split(": ")[1]
                condition = lines[i + 2].strip().split(": ")[1]
                appointment_date = lines[i + 3].strip().split(": ")[1]
                appointment_number = lines[i + 6].strip().split(": ")[1]

                formatted_data = (
                    f"Name: {patient_name}, "
                    f"Email: {patient_email}, "
                    f"Condition: {condition}, "
                    f"Date: {appointment_date}, "
                    f"Appointment Number: {appointment_number}"
                )
                assigned_patients.append(formatted_data)

        return assigned_patients

    def create_ddash_widgets(self):
        d_welcome = tk.Label(self.Doctor_Dashboard_Window, text="Hello {},\nWelcome To Your Doctor Dashboard".format(self.doctor_name))

        d_welcome.grid(row=0, columnspan=2, pady=15)

        assigned_patients = self.get_assigned_patients()
        #create more doctor dashboard widgets

                # Display assigned patients
        if assigned_patients:
            tk.Label(self.Doctor_Dashboard_Window, text="Assigned Patients:").grid(row=1, column=0, columnspan=2, pady=10)

            for i, patient in enumerate(assigned_patients, start=2):
                tk.Label(self.Doctor_Dashboard_Window, text=patient).grid(row=i, column=0, columnspan=2, pady=5, sticky="w")

        else:
            tk.Label(self.Doctor_Dashboard_Window, text="No patients assigned.").grid(row=1, column=0, columnspan=2, pady=10)
    #def more doctor dashboard functioality


#---ADMIN CLASSES

class Admin_Signup_GUI:
    def __init__(self, admin_window):
        self.admin_window = admin_window
        self.admin_window.title("Admin Signup")

        self.Name = tk.StringVar()
        self.Email = tk.StringVar()
        self.Password = tk.StringVar()
        self.Address = tk.StringVar()
        self.Phone = tk.StringVar()
        self.Age = tk.StringVar()


        #Entry Widgets
        self.Name_Entry = tk.Entry(self.admin_window, textvariable=self.Name)
        self.Age_Entry = tk.Entry(self.admin_window, textvariable=self.Age)
        self.Address_Entry = tk.Entry(self.admin_window, textvariable=self.Address)
        self.Phone_Entry = tk.Entry(self.admin_window, textvariable=self.Phone)
        self.Email_Entry = tk.Entry(self.admin_window, textvariable=self.Email)
        self.Password_Entry = tk.Entry(self.admin_window, textvariable=self.Password)
        self.create_admin_widgets()

    def create_admin_widgets(self):
        tk.Label(self.admin_window, text="Admin's Name:").grid(row=0, column=0, padx=10, pady=10)
        self.Name_Entry.grid(row=0, column=1)

        tk.Label(self.admin_window, text="Admin's Age:").grid(row=1, column=0, padx=10, pady=10)
        self.Age_Entry.grid(row=1, column=1)

        tk.Label(self.admin_window, text="Admin's Address:").grid(row=2, column=0, padx=10, pady=10)
        self.Address_Entry.grid(row=2, column=1)

        tk.Label(self.admin_window, text="Admin's Phone:").grid(row=3, column=0, padx=10, pady=10)
        self.Phone_Entry.grid(row=3, column=1)

        tk.Label(self.admin_window, text="Admin's Email:").grid(row=4, column=0, padx=10, pady=10)
        self.Email_Entry.grid(row=4, column=1)

        tk.Label(self.admin_window, text="Set Your Password:").grid(row=5, column=0, padx=10, pady=10)
        self.Password_Entry.grid(row=5, column=1)

        tk.Button(self.admin_window, text="Submit", command=self.submit).grid(row=6, column=0, columnspan=2, pady=10)

        tk.Label(self.admin_window, text="Already Registered?").grid(row=7, column=0, columnspan=2)

        tk.Button(self.admin_window, text="Login as Admin ", command=self.Show_Admin_Login).grid(row=8, column=0, columnspan=2, pady=1)

    def submit(self):
        Admin_Name = self.Name_Entry.get()
        Admin_Email = self.Email_Entry.get()
        Admin_Password = self.Password_Entry.get()
        Admin_Address = self.Address_Entry.get()
        Admin_Phone = self.Phone_Entry.get()
        Admin_Age = self.Age_Entry.get()

        #Clear Fields
        self.Name_Entry.delete(0, "end")
        self.Email_Entry.delete(0, "end")
        self.Password_Entry.delete(0, "end")
        self.Address_Entry.delete(0, "end")
        self.Phone_Entry.delete(0, "end")
        self.Age_Entry.delete(0, "end")


        open("Admin_Data.txt", "a")

        with open("Admin_Data.txt", "r") as file:
            if Admin_Email in file.read():
                email_used = tk.Label(self.admin_window, text="Email already in use. Choose a different one.")
                email_used.grid(row=10, columnspan=2, pady=1)


            else:
                with open("Admin_Data.txt", "a") as append_file:
                    append_file.write("Admin Name: {}\nAdmin Age: {}\nAdmin Address: {}\nAdmin Phone: {}\nAdmin Email: {}\nAdmin Password: {}\n".format(Admin_Name, Admin_Age, Admin_Address, Admin_Phone, Admin_Email, Admin_Password))

    def Show_Admin_Login(self):
        Admin_Login_Window = tk.Toplevel(self.admin_window)
        Admin_Login_Win = Admin_Login_Window_GUI(Admin_Login_Window)




class Admin_Login_Window_GUI:
    def __init__(self, Admin_Login_Window):
        self.Admin_Login_Window = Admin_Login_Window
        self.Admin_Login_Window.title("Admin Login")

        self.Email = tk.StringVar()
        self.Password = tk.StringVar()

        self.Email_Entry = tk.Entry(self.Admin_Login_Window, textvariable=self.Email)
        self.Password_Entry = tk.Entry(self.Admin_Login_Window, textvariable=self.Password)

        self.create_admin_login_widgets()
        self.Admin_Login_Window.mainloop()

    def create_admin_login_widgets(self):
        tk.Label(self.Admin_Login_Window, text="Admin Login").grid(row=0, columnspan=2, padx=10, pady=10)
        tk.Label(self.Admin_Login_Window, text="Enter Your Email:").grid(row=1, column=0, padx=10, pady=10)
        self.Email_Entry.grid(row=1, column=1)
        tk.Label(self.Admin_Login_Window, text="Enter Your Password:").grid(row=2, column=0, padx=10, pady=10)
        self.Password_Entry.grid(row=2, column=1)
        tk.Button(self.Admin_Login_Window, text="Login", command=self.show_admin_dashboard).grid(columnspan=2, row=3, pady=1)

    def show_admin_dashboard(self):
        email = self.Email.get()
        password = self.Password.get()

        admin_validator = LoginValidator("Admin_Data.txt")

        if admin_validator.validate_login(email, password):
            print("Admin Login Successful")
            self.Show_AppointmentsViewer()
        else:
            print("Invalid email or password")



    def Show_AppointmentsViewer(self):
        appointments_window = tk.Toplevel(self.Admin_Login_Window)
        AppointmentsViewer_Win = AppointmentsViewer(appointments_window)


class AppointmentsViewer:
    def __init__(self, appointments_window):
        self.appointments_window = appointments_window
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.appointments_window, text="All Appointments").grid(row=0, column=0, columnspan=3, pady=10)

        # Read appointments data from the file
        appointment_data = self.read_appointments_data()

        # Configure row to expand with window size
        self.appointments_window.grid_rowconfigure(1, weight=1)

        # Display appointments with "Assign Doctor" button
        for i, appointment in enumerate(appointment_data, start=1):
            tk.Label(self.appointments_window, text=appointment).grid(row=i, column=0, columnspan=2, pady=5, sticky="w")

            # Button to assign a doctor
            assign_button = tk.Button(self.appointments_window, text="Assign Doctor",
                                      command=lambda app_info=appointment, app_number=i: self.show_assign_doctor_window(appointment, i))
            assign_button.grid(row=i, column=2, pady=5, sticky="e")

            tk.Label(self.appointments_window, text="-" * 30).grid(row=i + 1, column=0, columnspan=3, pady=2, sticky="w")
            i += 2

    def read_appointments_data(self):
        # Read all appointments data from the file
        appointment_data = []
        with open("Appointment_Data.txt", "r") as file:
            lines = file.readlines()

        # Process the lines and format the data
        i = 0
        while i < len(lines):
            # Assuming each appointment has at least 4 lines of relevant information
            patient_name = lines[i].strip().split(": ")[1]
            patient_email = lines[i + 1].strip().split(": ")[1]
            condition = lines[i + 2].strip().split(": ")[1]
            appointment_date = lines[i + 3].strip().split(": ")[1]
            appoint_number = lines[i+ 6].strip().split(": ")[1]

            formatted_data = (
                f"Name: {patient_name}, "
                f"Email: {patient_email}, "
                f"Condition: {condition}, "
                f"Date: {appointment_date}, "
                f"Appointment Number: {appoint_number}"
            )
            appointment_data.append(formatted_data)

            # Increment i to skip the lines for "Status", "Doctor", and "Appointment Number"
            i += 7

        return appointment_data

    def show_assign_doctor_window(self, appointment_info, appoint_number):
        patient_email = appointment_info.split(", ")[1].split(": ")[1]
        appointment_date = appointment_info.split(", ")[3].split(": ")[1]
        condition = appointment_info.split(", ")[2].split(": ")[1]
        assign_doctor_window = tk.Toplevel(self.appointments_window)
        assign_doctor_win = AssignDoctorWindow(assign_doctor_window, appointment_info, appoint_number, patient_email, appointment_date, condition)

    # ... (Your existing code remains unchanged below)

class AssignDoctorWindow:
    def __init__(self, assign_doctor_window, appointment_info, appoint_number, patient_email, appointment_date, condition):
        self.assign_doctor_window = assign_doctor_window
        self.appointment_info = appointment_info
        self.appoint_number = appoint_number
        self.patient_email = patient_email
        self.appointment_date = appointment_date
        self.condition = condition
        self.create_widgets()

    def create_widgets(self):
        print(self.patient_email, self.condition)
        tk.Label(self.assign_doctor_window, text="Assign Doctor").grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(self.assign_doctor_window, text="Enter Doctor's Email:").grid(row=1, column=0, padx=10, pady=10)

        self.docemail = tk.StringVar()

        self.doctor_email_entry= tk.Entry(self.assign_doctor_window, textvariable=self.docemail)

        self.doctor_email_entry.grid(row=1, column=1)

        tk.Button(self.assign_doctor_window, text="Assign", command=self.assign_doctor).grid(row=2, column=0, columnspan=2, pady=10)



    def assign_doctor(self):

        doc_email = self.docemail.get()
        if self.is_doctor_email_valid(doc_email):
            with open("Appointment_Data.txt", "r") as file:
                lines = file.readlines()
                for i, line in enumerate(lines):
                    if "Patient Email: {}".format(self.patient_email) in line.strip() and "Condition: {}".format(self.condition) in lines[i+1].strip() and "Date: {}".format(self.appointment_date) in lines[i+2].strip():

                        lines[i+4] = f"Doctor: {doc_email}\n"
                        lines[i+3] = f"Status: APPROVED\n"
                        print("overwritten")
                        print(self.appoint_number)
                        break
            with open("Appointment_Data.txt", "w") as file:
                file.writelines(lines)


            # Display a success message
            success_label = tk.Label(self.assign_doctor_window, text=f"Doctor {doc_email} assigned to the appointment.")
            success_label.grid(row=3, column=0, columnspan=2, pady=5)
        else:
            # Display an error message if the doctor's email doesn't exist
            error_label = tk.Label(self.assign_doctor_window, text="Error: Doctor's email not found.")
            error_label.grid(row=3, column=0, columnspan=2, pady=5)

    def is_doctor_email_valid(self, doc_email):
        #see if doctor emai inputted is in Doctor_Data.text
        with  open("Doctor_Data.txt", "r") as file:
            return any(doc_email in line for line in file)


#--MAIN--

if __name__ == "__main__":
    root = tk.Tk()
    app = Start_Dashboard(root) 
    root.mainloop()

