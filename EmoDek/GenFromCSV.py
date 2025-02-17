import os
import qrcode
import csv
import random

try:
    from PIL import Image
except ImportError:
    print("Pillow (PIL) library is not installed. Please install it using 'pip install Pillow'")
    exit()

# generate a random number (same for all students)
def generate_random_number():
    return random.randint(1000, 9999) 

# generate a QR code
def generate_qr(data, filename):
    qr = qrcode.make(data)
    qr.save(filename)
    print(f"QR code saved as {filename}")

# read CSV file and generate QR codes for each student
def generate_qrs_from_csv(csv_filename):
    random_number = generate_random_number() 
    print(f"Generated Random Number for all students: {random_number}")

    # Open the CSV file for reading
    with open(csv_filename, mode='r') as file:
        csv_reader = csv.DictReader(file)
        
        for row in csv_reader:
            student_data =  f"{row['Registration_Number']}\n"\
                            f"{random_number}\n"\
                            f"{1001}"
            
            filename = f"{row['Registration_Number']}_QR.png"
            generate_qr(student_data, filename)

if __name__ == "__main__":
    csv_filename = r"C:\Users\aryan\Desktop\EmoDek\Data.csv"
    if os.path.isfile(csv_filename):
        generate_qrs_from_csv(csv_filename)
    else:
        print("Error: The file does not exist.")