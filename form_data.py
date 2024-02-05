terms_text_data = """
The standard Lorem Ipsum passage, used since the 1500s
    
"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor 
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud 
exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure 
dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt 
mollit anim id est laborum."
Section 1.10.32 of "de Finibus Bonorum et Malorum", written by Cicero in 45 BC

"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque
laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi
architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas
sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione
voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit
amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut
labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis
nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi
consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam
nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla
pariatur?"
1914 translation by H. Rackham

"But I must explain to you how all this mistaken idea of denouncing pleasure and
praising pain was born and I will give you a complete account of the system, and
expound the actual teachings of the great explorer of the truth, the master-builder
of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it
is pleasure, but because those who do not know how to pursue pleasure rationally
encounter consequences that are extremely painful. Nor again is there anyone who
loves or pursues or desires to obtain pain of itself, because it is pain, but
because occasionally circumstances occur in which toil and pain can procure him
some great pleasure. To take a trivial example, which of us ever undertakes laborious
physical exercise, except to obtain some advantage from it? But who has any right to
find fault with a man who chooses to enjoy a pleasure that has no annoying consequences,
or one who avoids a pain that produces no resultant pleasure?"
Section 1.10.33 of "de Finibus Bonorum et Malorum", written by Cicero in 45 BC
"""

occupation_data = ['Accountant', 'Architect', 'Biomedical Engineer', 'Chemical Engineer', 'Civil Engineer',
                   'Computer Systems Analyst', 'Construction Manager', 'Data Scientist', 'Dental Hygienist',
                   'Dentist', 'Electrical Engineer', 'Environmental Scientist', 'Event Planner',
                   'Fashion Designer', 'Financial Analyst', 'Financial Manager', 'Graphic Designer',
                   'Human Resources Manager', 'IT Manager', 'Interpreter/Translator', 'Lawyer',
                   'Management Analyst', 'Market Research Analyst', 'Market Researcher', 'Marketing Manager',
                   'Mechanical Engineer', 'Nurse Practitioner', 'Occupational Therapist',
                   'Operations Manager', 'Operations Research Analyst', 'Optometrist', 'Pharmacist',
                   'Pharmacy Technician', 'Phlebotomist', 'Physical Therapist', 'Physical Therapy Assistant',
                   'Physician', 'Psychologist', 'Public Relations Specialist', 'Radiologic Technologist',
                   'Registered Dietitian', 'Registered Nurse', 'Sales Manager', 'Social Worker',
                   'Software Developer', 'Software Engineer', 'Speech-Language Pathologist', 'Teacher',
                   'Technical Writer', 'Veterinarian', 'Web Developer']

phone_prefix_data = ['+1', '+1-246', '+1-268', '+1-473', '+1-767', '+1-809', '+1-829', '+1-849', '+20', '+212',
                     '+213', '+216', '+218', '+220', '+221', '+222', '+223', '+224', '+225', '+226', '+227',
                     '+228', '+229', '+230', '+231', '+232', '+233', '+234', '+235', '+236', '+237', '+238',
                     '+239', '+240', '+241', '+242', '+243', '+244', '+245', '+246', '+247', '+248', '+249',
                     '+250', '+251', '+252', '+253', '+254', '+255', '+256', '+257', '+258', '+260', '+261',
                     '+262', '+263', '+264', '+265', '+266', '+267', '+268', '+269', '+27', '+290', '+291', '+297',
                     '+298', '+299', '+30', '+31', '+32', '+33', '+34', '+350', '+351', '+352', '+353', '+354',
                     '+355', '+356', '+357', '+358', '+359', '+36', '+370', '+371', '+372', '+373', '+374', '+375',
                     '+376', '+377', '+378', '+379', '+380', '+381', '+382', '+383', '+385', '+386', '+387',
                     '+389', '+39', '+40', '+41', '+420', '+421', '+423', '+43', '+44', '+45', '+46', '+47', '+48',
                     '+49', '+500', '+501', '+502', '+503', '+504', '+505', '+506', '+507', '+508', '+509', '+51',
                     '+52', '+53', '+54', '+55', '+56', '+57', '+58', '+590', '+591', '+592', '+593', '+594',
                     '+595', '+596', '+597', '+598', '+599', '+60', '+61', '+62', '+63', '+64', '+65', '+66',
                     '+670', '+672', '+673', '+674', '+675', '+676', '+677', '+678', '+679', '+680', '+681',
                     '+682', '+683', '+684', '+685', '+686', '+687', '+688', '+689', '+690', '+691', '+692', '+7',
                     '+76', '+77', '+800', '+808', '+81', '+82', '+84', '+850', '+852', '+853', '+855', '+856',
                     '+86', '+870', '+871', '+872', '+873', '+874', '+875', '+876', '+877', '+878', '+879', '+880',
                     '+881', '+882', '+883', '+884', '+885', '+886', '+887', '+888', '+889', '+89', '+850', '+852',
                     '+853', '+855', '+856', '+86', '+870', '+871', '+872', '+873', '+874', '+875', '+876', '+877',
                     '+878', '+879', '+880', '+881', '+882', '+883', '+884', '+885', '+886', '+887', '+888',
                     '+889', '+89', '+850', '+852', '+853', '+855', '+856', '+86', '+870', '+871', '+872', '+873',
                     '+874', '+875', '+876', '+877', '+878', '+879', '+880', '+881', '+882', '+883', '+884',
                     '+885', '+886', '+887', '+888', '+889', '+89', '+850', '+852', '+853', '+855', '+856', '+86',
                     '+870', '+871', '+872', '+873', '+874', '+875', '+876', '+877', '+878', '+879', '+880',
                     '+881', '+882', '+883', '+884', '+885', '+886', '+887', '+888', '+889', '+89', '+850', '+852',
                     '+853', '+855', '+856', '+86', '+870', '+871', '+872', '+873', '+874', '+875', '+876', '+877',
                     '+878', '+879', '+880', '+881', '+882', '+883', '+884', '+885', '+886', '+887', '+888',
                     '+889', '+89', '+90', '+91', '+92', '+93', '+94', '+95', '+960']
