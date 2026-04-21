import time
import random

# Constants from SilentCare PPT
HR_THRESHOLD_HIGH = 120
SPO2_THRESHOLD_LOW = 92

def validate_alert(vitals_history):
    # Time-validation logic: Alert only if vitals are off for 3 consecutive readings
    # This reduces false alarms (Alarm Fatigue) by 85-90% [cite: 9, 26]
    if len(vitals_history) < 3: return False
    return all(v > HR_THRESHOLD_HIGH or v < SPO2_THRESHOLD_LOW for v in vitals_history[-3:])

def simulate_patient_monitor(bed_id):
    history = []
    print(f"--- Monitoring Bed {bed_id} ---")
    
    while True:
        # Simulating MAX30101 Sensor data [cite: 18]
        current_hr = random.randint(70, 130) 
        history.append(current_hr)
        
        if validate_alert(history):
            print(f"![CRITICAL] Bed {bed_id}: Heart Rate {current_hr} BPM. Sending Haptic Alert to Nurse Band...")
            break
        else:
            print(f"[Normal] Bed {bed_id}: {current_hr} BPM. Processing at Edge...")
        time.sleep(1)

simulate_patient_monitor("101")