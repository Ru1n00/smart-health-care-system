import json
doctors = [
    ['Dr. A. K. M. Fazlul Haque', 'Cardiology', 'MBBS, FCPS (Medicine), MD (Cardiology), FACC (USA), FESC (Europe)', 'Professor & Director', 'National Institute of Cardiovascular Diseases', 'Popular dhaka', '3pm - 9pm', '01711594594', ''],
    # create more doctors here
    ['Dr. Ziaur Rahman', 'Cardiology', 'MBBS, FCPS (Medicine), MD (Cardiology)', 'Consulting Cardiologist', 'Heart Foundation Hospital', 'Banani', '9am - 5pm', '01718075575', 'HeartFoundation.org'],

    ['Dr. Fazle Rabbi', 'Neurology', 'MBBS, FCPS (Medicine), MD (Neurology)', 'Consulting Neurologist', 'Universal Neuroscience Hospital', 'Dhanmondi', '9am - 5pm', '01719090909', ''],

    ['Dr. Sayma Sultana', 'Obstetrics & Gynaecology', 'MBBS, FCPS', 'Consulting OBGYN', 'Family Hospital & Maternity Center', 'Motijheel', '9am - 5pm', '01710670670', ''],

    ['Dr. Khandaker Golam Mohammad', 'Pediatrics', 'MBBS, FCPS', 'Consulting Pediatrician', 'National Institute of Child Health & Pediatrics', 'Purbachal', '9am - 5pm', '01718585858', ''],

    ['Dr. Md. Shahriar', 'Gastroenterology', 'MBBS, FCPS (Medicine), MD (Gastroenterology)', 'Consulting Gastroenterologist', 'Digestive and Liver Hospital', 'Dhanmondi', '9am - 5pm', '01719191919', ''],

    ['Dr. Farzana Haque', 'Endocrinology', 'MBBS, FCPS (Medicine), MD', 'Consulting Endocrinologist', 'Diabetes & Endocrine Care Center', 'Shalbagan', '9am - 5pm', '01712525252', ''],

    ['Dr. Mohammad Shoriful Islam', 'Neurology', 'MBBS, FCPS (Medicine), MD', 'Consulting Neurologist', 'National Institute of Neuroscience & Neuro-rehabilitation', 'Shahbagh', '9am - 5pm', '01711515151', ''],

    ['Dr. Mohammad Shoriful Islam', 'Neurology', 'MBBS, FCPS (Medicine), MD', 'Consulting Neurologist', 'National Institute of Neuroscience & Neuro-rehabilitation', 'Shahbagh', '9am - 5pm', '01711516512', ''],

    ['Dr. S. M. Sattar', 'Cardiology', 'MBBS, FCPS (Medicine), MD (Cardiology)', 'Consulting Cardiologist', 'Heart Foundation Hospital', 'Banani', '9am - 5pm', '01716500171', ''],

    ['Dr. Mohammad Shafiq Ul Islam', 'Pediatrics', 'MBBS, FCPS', 'Consulting Pediatrician', 'Family Hospital & Maternity Center', 'Motijheel', '9am - 5pm', '01710550550', ''],

    ['Dr. S. M. Ibrahim', 'Gastroenterology', 'MD (Gastroenterologie)', 'Consulting Gastroenterologist', 'National Institute of Gastroenterology', 'Badda', '9am - 5pm', '01715505505', ''],

    ['Dr. Abdul Aziz', 'Urology', 'MBBS, FCPS (Medicine), MD', 'Consulting Urologist', 'National Institute of Urology & Kidney Transplantation', 'Dhanmondi', '9am - 5pm', '01714545454', ''],

    ['Dr. Md. Sahabuddin', 'Cardiology', 'MBBS, FCPS (Medicine), MD (Cardiology)', 'Consulting Cardiologist', 'Heart Foundation Hospital', 'Banani', '9am - 5pm', '01716006006', ''],

    ['Dr. S. M. Nuruddin Ahmed', 'Orthopedics', 'MBBS, FCPS (Medicine), MD', 'Consulting Orthopedic Surgeon', 'National Institute of Orthopedic and Traumatology', 'Mohammadpur', '9am - 5pm', '01718080808', ''],

    ['Dr. Md. Abdur Rahman', 'Ophthalmology', 'MBBS, FCPS', 'Consulting Ophthalmologist', 'National Institute of Ophthalmology', 'Banani', '9am - 5pm', '01718585858', ''],

    ['Dr. S. M. Golam', 'Obstetricia', 'MBBS, FCPS (Medicine), MD', 'Consulting Obstetrician', 'Banani Maternity Hospital & Nursing Home', 'Banani', '9am - 5pm', '01710700700', ''],

    ['Dr. Mohammad Shahriar', 'Cardiology', 'MBBS, FCPS (Medicine), MD (Cardiology)', 'Consulting Cardiologist', 'Heart Foundation Hospital', 'Banani', '9am - 5pm', '01716500171', ''],

    ['Dr. S. M. Sadeque', 'Internal Medicine', 'MBBS, FCPS', 'Consulting Internist', 'Family Hospital & Maternity Center', 'Motijheel', '9am - 5pm', '01710670670', ''],

    ['Dr. Mohammad Shahlaque', 'Gastroenterology', 'MBBS, FCPS (Medicine), MD', 'Consulting Gastroenterologist', 'National Institute of Gastroenterology', 'Badda', '9am - 5pm', '01715505505', ''],

    ['Dr. S. M. Abdul Halim', 'Orthopedics', 'MBBS, FCPS (Medicine), MD', 'Consulting Orthopedic Surgeon', 'Heart Foundation Hospital', 'Banani', '9am - 5pm', '01716006006', ''],

    ['Dr. Md. Ziaul', 'Urology', 'MBBS, FCPS', 'Consulting Urologist', 'National Institute of Urology & Kidney Transplantation', 'Dhanmondi', '9am - 5pm', '01714545454', ''],

    ['Dr. Anowara', 'Obstetrics & Gynaecology', 'MBBS, FCPS', 'Consulting OBGYN', 'Heart Foundation Hospital', 'Banani', '9am - 5pm', '01718075575', ''],

    ['Dr. Mohammad Abdullah', 'Pediatrics', 'MBBS, FCPS', 'Consulting pediatric', 'Family Hospital & Maternity Center', 'Motijheel', '9am - 5pm', '01710550550', ''],

    ['Dr. Mohammad Abdullah', 'Pediatrics', 'MBBS, FCPS', 'Consulting pediatric', 'Family Hospital & Maternity Center', 'Motijheel', '9am - 5pm', '01710670670', ''],

    ['Dr. S. M. Mominul Islam', 'Cardiology', 'MBBS, FCPS (Medicine), MD (Cardiology)', 'Consulting Cardiologist', 'Heart Foundation Hospital', 'Banani', '9am - 5pm', '01716500171', ''],

    ['Dr. S. M. Shafiq', 'Neurology', 'MBBS, FCPS (Medicine), MD', 'Consulting Neurologist', 'Family Hospital & Maternity Center', 'Motijheel', '9am - 5pm', '01710550550', ''],

    ['Dr. Md. Shamsul Haque', 'Gastroenterology', 'MD (Gastroenterology)', 'Consulting Gastroenterologist', 'National Institute of Gastroenterology', 'Badda', '9am - 5pm', '01715505505', ''],

    ['Dr. Md. Mostafa', 'Nephrology', 'MBBS, FCPS (Medicine), MD', 'Consulting Nephrologist', 'Heart Foundation Hospital', 'Banani', '9am - 5pm', '01716500171', ''],

    ['Dr. S. M. Jahangir Hossain', 'Urology', 'MBBS, FCPS (Medicine), MD', 'Consulting Urologist', 'National Institute of Urology & Kidney Transplantation', 'Dhanmondi', '9am - 5pm', '01714545454', ''],

    ['Dr. Nurul Islam', 'Orthopedics', 'MBBS, FCPS', 'Consulting Orthopedic Surgeon', 'Family Hospital & Maternity Center', 'Motijheel', '9am - 5pm', '01710670670', ''],

    ['Dr. S. M. Khairul Basar', 'Cardiology', 'MBBS, FCPS (Medicine), MD (Cardiology)', 'Consulting Cardiologist', 'Heart Foundation Hospital', 'Banani', '9am - 5pm', '017165001', ''],

    ['Dr. S. M. Abu Sayem', 'Ophthalmology', 'MBBS, FCPS', 'Consulting Ophthalmologist', 'Heart Foundation Hospital', 'Banani', '9am - 5pm', '01718075575', ''],

    ['Dr. Md. Abdul Qayyum', 'Orthopedics', 'MBBS, FCPS', 'Consulting Orthopedic Surgeon', 'Family Hospital & Maternity Center', 'Motijheel', '9am - 5pm', '01710670670', ''],

    ['Dr. S. M. Selim', 'Dermatology', 'MBBS, FCPS', 'Consulting Dermatologist', 'Family Hospital & Maternity Center', 'Motijheel', '9am - 5pm', '01710550550', ''],

    ['Dr. Mohammad Ashraf Ali', 'Gastroenterology', 'MBBS, FCPS', 'Consulting Gastroenterologist', 'Dhanmondi Polyclinic', 'Dhanmondi', '9am - 5pm', '01713081542', ''],

    ['Dr. Md. Golam Kibria', 'Ophthalmology', 'MBBS, FCPS', 'Consulting Ophthalmologist', 'Family Hospital & Maternity Center', 'Motijheel', '9am - 5pm', '01710670670', ''],

    ['Dr. S. M. Mahbubur Rahman', 'Pediatrics', 'MBBS, FCPS', 'Consulting Pediatrician', 'Heart Foundation Hospital', 'Banani', '9am - 5pm', '01718075575', ''],

    ['Dr. S. M. Khayal Ud Din', 'Gastroenterology', 'MBBS, FCPS', 'Consulting Gastroenterologist', 'Family Hospital & Maternity Center', 'Motijheel', '9am - 5pm', '01710550550', ''],

    ['Dr. S. M. Shahadat Hossain', 'Cardiology', 'MBBS, FCPS (Medicine), MD (Cardiology)', 'Consulting Cardiologist', 'Heart Foundation Hospital', 'Banani', '9am - 5pm', '01716500171', ''],

    ['Dr. Mohammad Shahjalal', 'Neurology', 'MBBS, FCPS', 'Consulting Neurologist', 'Family Hospital & Maternity Center', 'Motijheel', '9am - 5pm', '01710550550', ''],

    ['Dr. Mohammad Belal', 'Dermatology', 'MBBS, FCPS', 'Consulting Dermatologist', 'Dhanmondi Polyclinic', 'Dhanmondi', '9am - 5pm', '01713081542', ''],

    ['Dr. Md. Golam Rahman', 'Pediatrics', 'MBBS, FCPS', 'Consulting Pediatrician', 'Family Hospital & Maternity Center', 'Motijheel', '9am - 5pm', '01710670670', ''],

    ['Dr. S. M. M. Shawkatuzzaman', 'Diabetic & Endocrine', 'MBBS, FCPS', 'Consulting Endocrinologist', 'Family Hospital & Maternity Center', 'Motijheel', '9am - 5pm', '01710670670', ''],

    ['Dr. S. M. Sahabuddin Ahmed', 'Internal Medicine', 'MBBS, FCPS', 'Consulting Internist', 'Family Hospital & Maternity Center', 'Motijheel', '9am - 5pm', '01710670670', ''],

    ['Dr. Mohammad Abu Tayeb', 'Gastroenterology', 'MBBS, FCPS', 'Consulting Gastroenterologist', 'Heart Foundation Hospital', 'Banani', '9am - 5pm', '01716500171', '']
]


blood_donors = [
    ['Abdul Mannan', 'O-', 'Chittagong', '01862555555'],

    ['Amirul Islam', 'O-', 'Sylhet', '01862222222'],

    ['Abul Hashem', 'O+', 'Khulna', '01867777777'],

    ['Abu Bakkar Siddique', 'AB-', 'Comilla', '01867444444'],

    ['Aslam Hossain', 'O+', 'Barishal', '01862333333'],

    ['Abul Khair', 'O+', 'Dhaka', '01711555555'],

    ['Ashikur Rahman', 'A+', 'Rangpur', '01862666666'],

    ['Abu Naser', 'O+', 'Rajshahi', '01867776666'],

    ['Abul Hasan', 'O+', 'Narayanganj', '01711757575'],

    ['Arafat Hossain', 'A+', 'Chittagong', '01867555555'],

    ['Abdur Rahman', 'O+', 'Mymensingh', '01711777777'],

    ['Abdul Karim', 'O+', 'Sylhet', '01862225555'],

    ['Abul Kalam', 'O+', 'Khulna', '01867775555'],

    ['Aslam', 'O+', 'Barishal', '01862336666'],

    ['Abu Ali', 'O+', 'Dhaka', '01711566666'],

    ['Abul Hossen', 'O+', 'Cumilla', '01867445555'],

    ['Arzoo', 'O-', 'Dhaka', '01711577777'],

    ['Habibullah Khan', 'O+', 'Khulna', '01867888888'],

    ['Abul Kalam Shaker', 'O+', 'Dhaka', '01711997777'],

    ['Aslam Azad', 'AB-', 'Comilla', '01867447777'],

    ['Abu Sayeed', 'O+', 'Dhaka', '01711010101'],

    ['Habibur Rahman', 'O+', 'Barishal', '01862335555'],

    ['Anwar Kabir', 'A+', 'Khulna', '01867889999'],

    ['Abul Hasnat', 'O+', 'Dhaka', '01711595555'],

    ['Abul Bari', 'AB-', 'Rajshahi', '01867770000'],

    ['Ashraful Islam', 'O+', 'Sylhet', '01862266666'],

    ['Akbar Ali', 'O-', 'Chittagong', '01862557777'],

    ['Abul Fateh', 'O+', 'Narayanganj', '01711788888'],

    ['Altaf Hossain', 'A+', 'Barishal', '01862337777'],

    ['Abul Basir', 'O-', 'Khulna', '01867772222'],

    ['Asif Iqbal', 'A+', 'Comilla', '01867446666'],

    ['Abul Hasnat', 'O+', 'Khulna', '01867881111'],

    ['Abdullah Al Mamun', 'O+', 'Dhaka', '01711592222'],

    ['Abdullah Shafik', 'O+', 'Chittagong', '01862556666'],

    ['Akbar Ali', 'A-', 'Comilla', '01867445566'],

    ['Abu Sahed', 'O+', 'Mymensingh', '01711775577'],

    ['Ahmed Ali', 'O+', 'Dhaka', '01711596666'],

    ['Amir Ali', 'B-', 'Sylhet', '01862277555'],

    ['Anwar Ali', 'O+', 'Khulna', '01867882222'],

    ['Asif Ahmed', 'O-', 'Rajshahi', '01867772222'],

    ['Ali Ahnaf', 'A+', 'Barishal', '01862338888'],

    ['Amir Abdul Karim', 'O+', 'Comilla', '01867446666'],

    ['Abul Kashem', 'O-', 'Chittagong', '01862557777'],

    ['Ashikuzzaman', 'O+', 'Khulna', '01867883333'],

    ['Atur Rahman', 'O+', 'Dhaka', '01711591111'],

    ['Anwar Ahmed', 'O-', 'Sylhet', '01862288888'],

    ['Atul', 'O+', 'Rajshahi', '01867774444'],

    ['Ali Abdullah', 'O+', 'Mymensingh', '01711779999'],

    ['Abul Hasnat', 'O+', 'Khulna', '01867884444'],

    ['Ashfakur Rahman', 'O+', 'Dhaka', '01711593333'],
]


ambulances = [
    ['Alif Ambulance Service', '01711594594', 'Dhaka'],
    ['Ali Taxi Service', '01867776666', 'Rajshahi'],
    ['Amin Ambulance Service', '01862222222', 'Barishal'],
    ['Ahmed Taxi Service', '01711555555', 'Sylhet'],
    ['Abu Taxi Service', '01711777777', 'Khulna'],
    ['Abu Sayed Ambulance Service', '01867777777', 'Dhaka'],
    ['Abul Taxi Service', '01862333333', 'Comilla'],
    ['Ali Taxi Service', '01711595555', 'Mymensingh'],
    ['Amir Taxi Service', '01867888888', 'Chittagong'],
    ['Anwar Ambulance Service', '01862266666', 'Sylhet'], 
    ['Ashraful Ambulance Service', '01867771111', 'Khulna'], 
    ['Abdullah Taxi Service', '01711596666', 'Rajshahi'],
    ['Ali Sayed Ambulance Service', '01867444444', 'Comilla'], 
    ['Altaf Taxi Service', '01711776666', 'Sylhet'],
    ['Akbar Ambulance Service', '01862335555', 'Barishal'], 
    ['Akram Ambulance Service', '01867774444', 'Khulna'],
    ['Abdullah Ambulance Service', '01711777777', 'Mymensingh'], 
    ['Babul Ambulance Service', '01867886666', 'Chittagong'],
    ['Anwar Taxi Service', '01862244444', 'Rajshahi'],
    ['Azad Ambulance Service', '01867446666', 'Dhaka'],
    ['Maksud Ambulance Service', '01862336666', 'Chittagong'],
    ['Mohammad Ambulance Service', '01867885555', 'Mymensingh'], 
    ['Aziz Ambulance Service', '01711773333', 'Barishal'],
    ['Nazib Ambulance Service', '01867447777', 'Sylhet'],
    ['Asif Ambulance Service', '01867788555', 'Khulna'],
    ['Omar Ambulance Service', '01711598888', 'Rajshahi'], 
    ['Rashid Ambulance Service', '01867883333', 'Dhaka'],
    ['Abul Kashem Ambulance Service', '01711774444', 'Comilla'], 
    ['Saiful Taxi Service', '01862332222', 'Barishal'],
    ['Shabnam Ambulance Service', '01867448888', 'Sylhet'], 
    ['Sabbir Ambulance Service', '01867772222', 'Chittagong'], 
    ['Sajid Taxi Service', '01711778888', 'Dhaka'],
    ['Tarek Ambulance Service', '01867889999', 'Mymensingh'], 
    ['Abul Hasnat Ambulance Service', '01771222222', 'Dhaka'],
    ['Anwar Ambulance Service', '01862288888', 'Rajshahi'],
    ['Ashik Ambulance Service', '01867449999', 'Comilla'],
    ['Jahangir Ambulance Service', '01867886666', 'Khulna'], 
    ['Liaquat Ambulance Service', '01711599999', 'Sylhet'],

]
