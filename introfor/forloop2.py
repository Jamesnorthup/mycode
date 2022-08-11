#!/usr/bin/env python3

# create a list of strings

def getFarmData():
    farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
             {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
             {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
    return farms


# Function prints out farm data
def FarmsDataPrint():
    print("Farms data print")
    sb=""
    # Iterate through array
    for row in getFarmData():
        sb=sb+"---------------------------------------\n"
        sb=sb+row["name"]+"\n\n"
        
        # Append agriculture to stringbuilder
        for agriculture in row["agriculture"]:
      
            sb=sb+"\t"+agriculture+"\n"
        
    return sb

# Main simply calls on function to print farm data
def main():
    print(FarmsDataPrint())
    
    
    
if __name__ == "__main__":
    main()

                                                               

