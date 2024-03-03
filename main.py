from datetime import datetime
import time
from aicsimageio import AICSImage


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print("Saving CZI as OME-TIFF")

    # Get start time for timer
    start = datetime.now()

    # Get current date and time (BEFORE main fn)
    print("Processing START time:", start)

    # MAIN FUNCTION STUFF GOES HERE #######################
    # commenting this out for now just to test timer
    # AICSImage("my_file.czi").save("my_file.ome.tiff")

    # Sleep fn to test timer
    time.sleep(5)

    # END OF MAIN FUNCTION STUFF ##########################

    end = datetime.now()

    # Print current data and time (AFTER main fn)
    print("Processing END time:", end)

    # Make timedelta object
    elapsed = (end - start)
    print(elapsed)

    # Get the total time change in seconds from timedelta object
    elapsed_seconds = int(elapsed.total_seconds())

    # Printing elapsed time
    if elapsed_seconds < 60:
        print("Time elapsed: " + str(round(elapsed_seconds, 3)) + " seconds")
    elif elapsed_seconds < 3600:
        print("Time elapsed: " + str(round(elapsed_seconds / 60, 3)) + " minutes")
    else:
        print("Time elapsed: " + str(round(elapsed_seconds / 3600, 3)) + " hours")
