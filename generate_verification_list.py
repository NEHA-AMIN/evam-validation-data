import json
import os
import glob

def generate_list():
    files = []
    # Handle file 1 separately due to naming convention
    files.append("c:/Users/chinm/Downloads/EVENTS-QSR 2/EVENTS-QSR/1-event.json")
    
    # Handle files 2 through 19
    for i in range(2, 20):
        files.append(f"c:/Users/chinm/Downloads/EVENTS-QSR 2/EVENTS-QSR/{i}-event-en.json")
    
    verification_list = []

    for file_path in files:
        if not os.path.exists(file_path):
            continue
            
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            origin = data.get('store_location', {}).get('address', 'Unknown Origin')
            
            if 'events_assessment' in data:
                for category in data['events_assessment']:
                    if 'events' in category:
                        for event in category['events']:
                            location = event.get('location')
                            distance = event.get('distance_from_store')
                            name = event.get('name')
                            
                            if location and distance and distance != "0 miles" and "All McDonald's" not in location:
                                verification_list.append({
                                    'file': os.path.basename(file_path),
                                    'origin': origin,
                                    'destination': location,
                                    'current_distance': distance,
                                    'event_name': name
                                })
                                
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    with open('verification_list.json', 'w', encoding='utf-8') as f:
        json.dump(verification_list, f, indent=2)
    
    print(f"Generated list with {len(verification_list)} items.")

if __name__ == "__main__":
    generate_list()
