def diagnose(symptoms):
    rules = {
        "fever cough": ("Flu", "Take rest, drink fluids, consult doctor if severe."),
        "fever headache": ("Migraine or Viral Fever", "Take paracetamol and rest."),
        "chest pain breathlessness": ("Possible Heart Issue", "Seek immediate medical attention!"),
        "stomach pain nausea": ("Food Poisoning", "Stay hydrated and consult doctor."),
        "sore throat cough": ("Common Cold", "Warm fluids and rest recommended."),
        "fever rash": ("Possible Infection (e.g., Dengue)", "Visit hospital immediately."),
        "fatigue weight_loss": ("Possible Diabetes/Thyroid", "Get blood tests done."),
    }

    for rule in rules:
        rule_symptoms = set(rule.split())
        if rule_symptoms.issubset(symptoms):
            return rules[rule]

    return ("Unknown Condition", "Consult a doctor for proper diagnosis.")

def main():
    print("🏥 Welcome to Hospital Expert System")
    print("Enter symptoms separated by space (e.g., fever cough): ")

    user_input = input("Symptoms: ").lower()
    symptoms = set(user_input.split())

    diagnosis, advice = diagnose(symptoms)

    print("\n🩺 Diagnosis:", diagnosis)
    print("💡 Advice:", advice)

if __name__ == "__main__":
    main()
