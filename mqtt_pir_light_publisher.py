import json
import time
import paho.mqtt.client as mqtt

# ===== REQUIRED FIELDS =====
student_name = "Sreenivasulu"
unique_id = "42732074"
topic_base = "home/sreenu-2025/sensor"   # replace YOURNAME

broker = "localhost"
port = 1883

def main():
    client = mqtt.Client()
    client.connect(broker, port, 60)
    print("Connected to MQTT broker")

    while True:
        temperature = 25
        humidity = 60
        light_level = 300
        pir_motion = 1  # 1 = motion, 0 = no motion

        payloads = {
            "temperature": {"sensor":"temperature","value":temperature},
            "humidity": {"sensor":"humidity","value":humidity},
            "light": {"sensor":"light","value":light_level},
            "pir": {"sensor":"pir","value":pir_motion},
        }

        for key, p in payloads.items():
            p["student_name"] = student_name
            p["unique_id"] = unique_id
            client.publish(f"{topic_base}/{key}", json.dumps(p))
            print(f"Published {key}: {p}")

        time.sleep(5)

if __name__ == "__main__":
    main()
