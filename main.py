from datacleaning import clean as cln        # Library to clean the data for future scalability
from movie_recommendation import recommend   # Library to for recommendation for future scalabilty and improvement of the recommendation algorithm
import random as rd
from time import time

if __name__ == "__main__":
        
    # Get user input
    user_input = input(" \nEnter a short description of your preferred movie: ")
     
    fln = 'movies.csv' # Filename of the the dataset from Kaggle public repository
    
    # Load dataset
    movie_df = cln(fln) # Clean the dataset and return Title and Description

    # Recommend movies
    start_time = time()
    rand_val = rd.randint(3,5)
    results = recommend(user_input, movie_df, rand_val) # Using random listing for dynamic output to users
    print(f"Execution time: {(time() - start_time):.2f} s") # Excution time computation
    # Display results
    print("\nTop recommended movies:")
    
    attempt = 0
    res = results.to_dict()  # Convert the result dataframe to dictionary
    while True:
        
        print(results) # Display the recommendation result to the user
        select_input = input(f"\nSelect any of the recommendations for full description using the S/No. (e.g 1. {res['Title'][0]}), (q to quit): ") # For option to view the description 
        
        # For user to view full description of the recommended titles and make it interactive
        try:
            pick = int(select_input)
        except ValueError:
            if select_input == 'q':
                print('\nExiting!!!\n')
                break
            else:
                attempt += 1
                if attempt > 3:
                    print('\nThe number of attempts (3/3) exceeeded, The program is exiting!!!')
                    break
                else:  
                    print(f'\nWrong option!!!, Pls try again (Attempt: {attempt} out of 3):\n')
        else:
            if pick >= 1 and pick <= rand_val:
                pick -= 1
                print(f'\n{pick+1}. {res['Title'][pick]}: {res['Description'][pick]}\n')
                break
            
            else:
                attempt += 1
                if attempt > 3:
                    print('\nThe number of attempts (3/3) exceeeded, The program is exiting!!!')
                    break
                else:  
                    print(f'\nWrong option!!!, Pls try again (Attempt: {attempt} out of 3):\n')                
        
    