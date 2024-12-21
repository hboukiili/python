def NULL_not_found(obj: any) -> int:

    try:
        if obj is None:
            print(f"Nothing: {obj} {type(obj)}")
        elif isinstance(obj, float) and obj != obj: 
            print(f"Cheese: {obj} {type(obj)}")
        elif obj == 0 and type(obj) is int:
            print(f"Zero: {obj} {type(obj)}")
        elif obj == "" and type(obj) is str:
            print(f"Empty: {type(obj)}")
        elif obj is False:
            print(f"Fake: {obj} {type(obj)}")
        else:
            print("Type not Found")
            return 1
        return 0  
    except Exception as e:
        print(f"Error: {e}")
        return 1

if __name__ == "__main__":
    Nothing = None
    Garlic = float("NaN")
    Zero = 0
    Empty = ''
    Fake = False

    NULL_not_found(Nothing)  
    NULL_not_found(Garlic)   
    NULL_not_found(Zero)     
    NULL_not_found(Empty)    
    NULL_not_found(Fake)     
    print(NULL_not_found("Brian")) 
