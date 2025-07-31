"""This hospital system includes five classes: 
Patient (stores patient info and visits),
 Doctor (manages assigned patients), 
 Department (holds doctors in a department), 
 Appointment (represents a scheduled visit between a doctor and a patient),
 and Room (assigns patients to hospital rooms)."""

class Patient:
    _id_counter = 1

    def __init__(self, name):
        self.patient_id = Patient._id_counter
        Patient._id_counter += 1
        self.name = name
        self.visits = []

    def __str__(self):
        return f"Patient ID: {self.patient_id}, Name: {self.name}, Visits: {len(self.visits)}"

    def add_visit(self, visit):
        if visit not in self.visits:
            self.visits.append(visit)
            print("Visit added successfully")
        else:
            print("Visit already recorded")


class Doctor:
    _id_counter = 1

    def __init__(self, name):
        self.doctor_id = Doctor._id_counter
        Doctor._id_counter += 1
        self.name = name
        self.patients = []

    def __str__(self):
        return f"Doctor ID: {self.doctor_id}, Name: {self.name}, Patients: {len(self.patients)}"

    def assign_patient(self, patient):
        if patient not in self.patients:
            self.patients.append(patient)
            print("Patient assigned to doctor")
        else:
            print("Patient already assigned")

    def remove_patient(self, patient):
        if patient in self.patients:
            self.patients.remove(patient)
            print("Patient removed from doctor")
        else:
            print("Patient not found")


class Department:
    _id_counter = 1

    def __init__(self, name):
        self.department_id = Department._id_counter
        Department._id_counter += 1
        self.name = name
        self.doctors = []

    def __str__(self):
        return f"Department ID: {self.department_id}, Name: {self.name}, Doctors: {len(self.doctors)}"

    def add_doctor(self, doctor):
        if doctor not in self.doctors:
            self.doctors.append(doctor)
            print("Doctor added to department")
        else:
            print("Doctor already in department")

    def remove_doctor(self, doctor):
        if doctor in self.doctors:
            self.doctors.remove(doctor)
            print("Doctor removed from department")
        else:
            print("Doctor not found")


class Appointment:
    _id_counter = 1

    def __init__(self, patient, doctor, date):
        self.appointment_id = Appointment._id_counter
        Appointment._id_counter += 1
        self.patient = patient
        self.doctor = doctor
        self.date = date

    def __str__(self):
        return f"Appointment ID: {self.appointment_id}, Patient: {self.patient.name}, Doctor: {self.doctor.name}, Date: {self.date}"


class Room:
    _id_counter = 1

    def __init__(self, number):
        self.room_id = Room._id_counter
        Room._id_counter += 1
        self.number = number
        self.assigned_patients = []

    def __str__(self):
        return f"Room ID: {self.room_id}, Number: {self.number}, Assigned Patients: {len(self.assigned_patients)}"

    def assign_patient(self, patient):
        if patient not in self.assigned_patients:
            self.assigned_patients.append(patient)
            print("Patient assigned to room")
        else:
            print("Patient already in this room")

    def remove_patient(self, patient):
        if patient in self.assigned_patients:
            self.assigned_patients.remove(patient)
            print("Patient removed from room")
        else:
            print("Patient not found in this room")
