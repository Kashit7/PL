class ClinicAppointment:
    def __init__(self):
        # Available time slots and max appointments per slot per doctor
        self.time_slots = ['10am', '11am', '12pm', '2pm', '3pm']
        self.max_per_slot = 3
        self.doctors = set()
        self.appointments = []  # List to store all appointments

    def add_doctor(self, doctor_name):
        # Adds a doctor to the system
        self.doctors.add(doctor_name)

    def show_doctors(self):
        # Shows all registered doctors
        if not self.doctors:
            print("No doctors registered yet.")
        else:
            print("Available doctors:")
            for doc in self.doctors:
                print("-", doc)

    def show_slots(self, doctor_name):
        # Shows available slots for a specific doctor
        available = []
        for slot in self.time_slots:
            count = sum(app['doctor'] == doctor_name and app['slot'] == slot for app in self.appointments)
            if count < self.max_per_slot:
                available.append(slot)
        print(f"Available slots for Dr. {doctor_name}:", available)
        return available

    def book_appointment(self):
        # Prompt for patient details
        name = input("Enter patient name: ").strip()
        age = input("Enter age: ").strip()
        mobile = input("Enter mobile number: ").strip()
        self.show_doctors()
        doctor = input("Enter preferred doctor: ").strip()
        if doctor not in self.doctors:
            print("Doctor not found.")
            return
        available_slots = self.show_slots(doctor)
        if not available_slots:
            print("No slots available for this doctor.")
            return
        slot = input(f"Enter preferred slot from {available_slots}: ").strip()
        if slot not in available_slots:
            print("Slot not available.")
            return
        # Book appointment
        self.appointments.append({
            'name': name,
            'age': age,
            'mobile': mobile,
            'doctor': doctor,
            'slot': slot
        })
        print("Appointment booked successfully!")

    def view_appointment(self):
        mobile = input("Enter mobile number to view your appointment: ").strip()
        found = [app for app in self.appointments if app['mobile'] == mobile]
        if not found:
            print("No appointment found with this mobile number.")
        else:
            print("Your Appointments:")
            for app in found:
                print(f"Name: {app['name']}, Age: {app['age']}, Doctor: {app['doctor']}, Slot: {app['slot']}")

    def cancel_appointment(self):
        mobile = input("Enter mobile number to cancel appointment: ").strip()
        for i, app in enumerate(self.appointments):
            if app['mobile'] == mobile:
                print(f"Cancelling appointment for {app['name']} with Dr. {app['doctor']} at {app['slot']}")
                del self.appointments[i]
                print("Appointment cancelled.")
                return
        print("No appointment found with this mobile number.")

    def run(self):
        # Simple CLI for testing the class
        while True:
            print("\nOptions: 1) Add Doctor  2) Book Appointment  3) View Appointment  4) Cancel Appointment  5) Exit")
            choice = input("Enter your choice: ").strip()
            if choice == '1':
                doc = input("Enter doctor name to add: ").strip()
                self.add_doctor(doc)
            elif choice == '2':
                self.book_appointment()
            elif choice == '3':
                self.view_appointment()
            elif choice == '4':
                self.cancel_appointment()
            elif choice == '5':
                print("Exiting system.")
                break
            else:
                print("Invalid choice. Try again.")


if __name__ == "__main__":
    clinic = ClinicAppointment()
    clinic.run()


class SchoolManagement:
    def __init__(self):
        self.students = {}  # key: student_id, value: student data dict
        self.next_id = 1

    def new_admission(self):
        name = input("Enter student name: ").strip()
        age_in = input("Enter age (5-18): ").strip()
        if not age_in.isdigit():
            print("Invalid age. Admission failed.")
            return
        age = int(age_in)
        if age < 5 or age > 18:
            print("Age must be between 5 and 18.")
            return

        class_in = input("Enter class (1-12): ").strip()
        if not class_in.isdigit() or not (1 <= int(class_in) <= 12):
            print("Invalid class. Admission failed.")
            return
        student_class = int(class_in)

        mobile = input("Enter guardian mobile number: ").strip()
        if len(mobile) != 10 or not mobile.isdigit():
            print("Mobile number must be 10 digits.")
            return

        student_id = self.next_id
        self.students[student_id] = {
            'name': name,
            'age': age,
            'class': student_class,
            'mobile': mobile
        }
        self.next_id += 1
        print(f"Admission successful! Student ID assigned: {student_id}")

    def view_student(self):
        sid_in = input("Enter student ID to view details: ").strip()
        if not sid_in.isdigit():
            print("Invalid student ID.")
            return
        sid = int(sid_in)
        if sid in self.students:
            s = self.students[sid]
            print(f"Student ID: {sid}\nName: {s['name']}\nAge: {s['age']}\nClass: {s['class']}\nGuardian Mobile: {s['mobile']}")
        else:
            print("Student not found.")

    def update_student(self):
        sid_in = input("Enter student ID to update: ").strip()
        if not sid_in.isdigit():
            print("Invalid student ID.")
            return
        sid = int(sid_in)
        if sid not in self.students:
            print("Student not found.")
            return
        print("Update Options: 1) Mobile Number 2) Class")
        choice = input("Enter option: ").strip()
        if choice == '1':
            new_mobile = input("Enter new mobile number: ").strip()
            if len(new_mobile) != 10 or not new_mobile.isdigit():
                print("Mobile number must be 10 digits.")
                return
            self.students[sid]['mobile'] = new_mobile
            print("Mobile number updated.")
        elif choice == '2':
            new_class = input("Enter new class (1-12): ").strip()
            if not new_class.isdigit() or not (1 <= int(new_class) <= 12):
                print("Invalid class.")
                return
            self.students[sid]['class'] = int(new_class)
            print("Class updated.")
        else:
            print("Invalid update option.")

    def remove_student(self):
        sid_in = input("Enter student ID to remove: ").strip()
        if not sid_in.isdigit():
            print("Invalid student ID.")
            return
        sid = int(sid_in)
        if sid in self.students:
            del self.students[sid]
            print(f"Student with ID {sid} removed.")
        else:
            print("Student not found.")

    def run(self):
        while True:
            print("\n1) New Admission 2) View Student 3) Update Student 4) Remove Student 5) Exit")
            choice = input("Enter your choice: ").strip()
            if choice == '1':
                self.new_admission()
            elif choice == '2':
                self.view_student()
            elif choice == '3':
                self.update_student()
            elif choice == '4':
                self.remove_student()
            elif choice == '5':
                print("Exiting System.")
                break
            else:
                print("Invalid choice. Try again.")

if __name__ == "__main__":
    school = SchoolManagement()
    school.run()


class BusReservation:
    def __init__(self):
        # Predefined routes with prices
        self.routes = {
            "Mumbai to Pune": 500,
            "Delhi to Jaipur": 600,
            "Bangalore to Chennai": 700,
            "Hyderabad to Goa": 800,
            "Kolkata to Patna": 550
        }
        self.tickets = {}  # key: ticket_id, value: ticket info dict
        self.seats = {}    # key: route, value: list of assigned seat numbers
        self.next_ticket_id = 1

    def show_routes(self):
        print("Available Routes:")
        for route, price in self.routes.items():
            print(f"- {route} - ₹{price}")

    def available_seats(self, route):
        return 40 - len(self.seats.get(route, []))

    def book_ticket(self):
        name = input("Enter passenger name: ").strip()
        age_in = input("Enter age: ").strip()
        if not age_in.isdigit() or int(age_in) <= 0:
            print("Invalid age.")
            return
        age = int(age_in)
        mobile = input("Enter mobile number: ").strip()
        if len(mobile) != 10 or not mobile.isdigit():
            print("Mobile number must be 10 digits.")
            return
        self.show_routes()
        route = input("Enter desired route exactly as shown above: ").strip()
        if route not in self.routes:
            print("Route not found.")
            return
        # Check seat availability
        seats_for_route = self.seats.setdefault(route, [])
        if len(seats_for_route) >= 40:
            print("No seats available on this route.")
            return
        seat_no = len(seats_for_route) + 1
        ticket_id = self.next_ticket_id
        self.next_ticket_id += 1
        # Assign ticket
        ticket = {
            "name": name,
            "age": age,
            "mobile": mobile,
            "route": route,
            "seat": seat_no,
            "ticket_id": ticket_id,
            "price": self.routes[route]
        }
        self.tickets[ticket_id] = ticket
        seats_for_route.append(seat_no)
        print(f"Ticket Booked! Ticket ID: {ticket_id}, Route: {route}, Seat No: {seat_no}, Price: ₹{self.routes[route]}")

    def view_ticket(self):
        tid_in = input("Enter ticket ID to view: ").strip()
        if not tid_in.isdigit():
            print("Invalid ticket ID.")
            return
        tid = int(tid_in)
        if tid not in self.tickets:
            print("Ticket not found.")
            return
        t = self.tickets[tid]
        print(f"--- Ticket Details ---\n"
              f"Ticket ID: {t['ticket_id']}\n"
              f"Name: {t['name']}\n"
              f"Age: {t['age']}\n"
              f"Mobile: {t['mobile']}\n"
              f"Route: {t['route']}\n"
              f"Seat: {t['seat']}\n"
              f"Price: ₹{t['price']}")

    def cancel_ticket(self):
        tid_in = input("Enter ticket ID to cancel: ").strip()
        if not tid_in.isdigit():
            print("Invalid ticket ID.")
            return
        tid = int(tid_in)
        if tid not in self.tickets:
            print("Ticket not found.")
            return
        ticket = self.tickets.pop(tid)
        # Remove seat assignment
        if ticket["route"] in self.seats and ticket["seat"] in self.seats[ticket["route"]]:
            self.seats[ticket["route"]].remove(ticket["seat"])
        print(f"Ticket ID {tid} cancelled successfully.")

    def run(self):
        while True:
            print("\n1) Show Available Routes 2) Book Ticket 3) View Ticket 4) Cancel Ticket 5) Exit")
            choice = input("Enter choice: ").strip()
            if choice == '1':
                self.show_routes()
            elif choice == '2':
                self.book_ticket()
            elif choice == '3':
                self.view_ticket()
            elif choice == '4':
                self.cancel_ticket()
            elif choice == '5':
                print("Exiting system.")
                break
            else:
                print("Invalid option.")

if __name__ == "__main__":
    bus_system = BusReservation()
    bus_system.run()



