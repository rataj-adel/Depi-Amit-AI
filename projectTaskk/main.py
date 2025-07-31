from projectTaskk.core import Doctor, Patient

doc = Doctor("Dr. Sarah", 40, "Cardiology")
pat = Patient("Ali", 25, "Flu")

print(f"{doc.name} - {doc.specialty}")
print(f"{pat.name} - {pat.illness}")
