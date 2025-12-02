import json
import glob
import os
import re

def extract_info():
    files = []
    # Generate the list of files from 8 to 19
    for i in range(8, 20):
        files.append(f"c:/Users/chinm/Downloads/EVENTS-QSR 2/EVENTS-QSR/{i}-event-en.json")
    
    results = []

    for file_path in files:
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            continue
            
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            origin = data.get('store_location', {}).get('address', 'Unknown Origin')
            
            events_list = []
            if 'events_assessment' in data:
                for category in data['events_assessment']:
                    if 'events' in category:
                        for event in category['events']:
                            location = event.get('location')
                            distance = event.get('distance_from_store')
                            name = event.get('name')
                            
                            # Skip if location is generic or "0 miles" which usually implies same location or irrelevant
                            if location and distance and distance != "0 miles" and "All McDonald's" not in location:
                                events_list.append({
                                    'name': name,
                                    'location': location,
                                    'current_distance': distance
                                })
            
            results.append({
                'file': os.path.basename(file_path),
                'origin': origin,
                'destinations': events_list
            })
            
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    extract_info()
