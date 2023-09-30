from celery import shared_task
import time
import pandas as pd

@shared_task
def handle_timer():
    time.sleep(3000)
    print("The countdown has been done after the task has been done")
    
@shared_task
def to_write():
    print("The data is going to write in csv files")    
    # Create a DataFrame with a single row and specify an index as a list
    data = {"Column_Name": ["hello usama"]}  # Note the use of a list for values
    index = [1]
    
    a = pd.DataFrame(data, index=[None])
    
    # Now, you can write the DataFrame to a CSV file
    a.to_csv('written.csv', index=False)