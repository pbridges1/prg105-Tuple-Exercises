# Creating the Parts Database
# You will have a List that contains Tuples
# parts = [("Part ID", "Part", "Room", "Cabinet Location", "Vendor ID", "Price", "Quantity in Stock"),
#         ("T-01", "Tower Case", "S110", "Cabinet B, Shelf 1", "V-010", 79.99, 3, ),
#         ("P-02", "CPU", "S110", "Drawer C", "V-010", 199.99, 2)]
textbooks = [("Textbook ID", "Textbook Name", "Courses", "# Books", "Price Per Book", "Publisher ID", ),
             ("TEXT-0001", "Basic Anatomy and Physiology", "BIO-100", 400, 94.00, "PUB-1003", ),
             ("TEXT-0002", "Chemistry for Biology Students", "BIO-101-102", 400, 105.30, "PUB-1002", ),
             ("TEXT-0003", "Anatomy and Physiology", "BIO-141-142", 330, 159.75, "PUB-1003")]
publisher = [("Publisher ID", "Publisher Name", "Address", "City", "State", "Zip", "Phone Number", ),
             ("PUB-1001", "Science Books Galore", "525 Allen St", "Trenton", "NJ", "08620", "609-555-2554", ),
             ("PUB-1002", "Books for Chemistry Students Ltd", "142 N Springs St", "Los Angeles", "CA", "90012", "213-555-8362", ),
             ("PUB-1003", "Carliz Publishers Corp", "24 King Ave", "Columbus", "OH", "43201", "614-555-3322")]
# c = 0
# pts = []
# while c < len(parts):
#    pts.append(parts[c][0])
#    pts.append(parts[c][5])
#    pts.append(parts[c][6])
#    c += 1
#    print pts
# pts = []

t = 0
txt = []
while t < len(textbooks):
    txt.append(textbooks[t][1])
    txt.append(textbooks[t][4])
    t += 1
    print txt
txt = []

p = 0
pub = []
while p < len(publisher):
    pub.append(publisher[p][1])
    pub.append(publisher[p][6])
    p += 1
    print pub
pub = []
