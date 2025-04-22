from datetime import datetime, timedelta

def generate_exam_slots(start_date_str="2025-05-01", num_slots=100):
    slots = {}
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    current_slot = 1
    current_date = start_date

    while current_slot <= num_slots:
        # Add morning slot
        if current_slot <= num_slots:
            slots[current_slot] = current_date.strftime("%Y-%m-%d") + " 09:00 AM - 12:00 PM"
            current_slot += 1

        # Add afternoon slot
        if current_slot <= num_slots:
            slots[current_slot] = current_date.strftime("%Y-%m-%d") + " 02:00 PM - 05:00 PM"
            current_slot += 1

        # Move to next day
        current_date += timedelta(days=1)

    return slots

# Example usage
exam_slots = generate_exam_slots()
