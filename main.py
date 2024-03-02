import datetime
import time
from aicsimageio import AICSImage


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print("Saving CZI as OME-TIFF")

    # Get current date and time (BEFORE main fn)
    print("Processing START time:", datetime.datetime.now())

    # Get start time for timer
    start = time.time()

    # MAIN FUNCTION STUFF GOES HERE #######################
    # commenting this out for now just to test timer
    # AICSImage("my_file.czi").save("my_file.ome.tiff")

    # Sleep fn to test timer
    time.sleep(5)

    # END OF MAIN FUNCTION STUFF ##########################

    # Print current data and time (AFTER main fn)
    print("Processing END time:", datetime.datetime.now())

    end = time.time()
    elapsed = end - start

    # Printing elapsed time
    if elapsed < 60:
        print("Time elapsed: " + str(round(elapsed, 3)) + " seconds")
    elif elapsed < 3600:
        print("Time elapsed: " + str(round(elapsed / 60, 3)) + " minutes")
    else:
        print("Time elapsed: " + str(round(elapsed / 3600, 3)) + " hours")
