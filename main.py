import sys
from logic import calculate_pyramidal_sum

def main():
    print("Pyramidal Number Calculator (Pn = 1+3+6+...)")
    print("Type 'exit' to quit.")
    
    while True:
        user_input = input("\nEnter n: ")
        
        if user_input.lower() == 'exit':
            break
            
        try:
            n = int(user_input)
            result = calculate_pyramidal_sum(n)
            print(f"P({n}) = {result}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()