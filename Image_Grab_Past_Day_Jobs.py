from Parsable_API import *
import threading

# Base Directory
base_path = os.path.join(expanduser("~"), "Downloads")

# If Python Images Folder doesn't exist create it
if not os.path.isdir(os.path.join(base_path, "All_Job_Photos")):
    # Create Folder to hold all images
    os.mkdir(os.path.join(base_path, "All_Job_Photos"))

# If Log Folder doesn't exist create it
if not os.path.isdir(os.path.join(base_path, "All_Job_Photos", "All_Job_Logs")):
    # Create folder to hold all log files
    os.mkdir(os.path.join(base_path, "All_Job_Photos", "All_Job_Logs"))

# Create Log File
local_time = time.localtime()
local_time_tuple = (str(local_time.tm_mon), str(local_time.tm_mday), str(local_time.tm_year), "Log.log")
log_file_name = "_".join(local_time_tuple)
log_file_path = os.path.join(base_path, "All_Job_Photos", "All_Job_Logs", log_file_name)
logging.basicConfig(level = logging.DEBUG, filename = log_file_path, format='%(asctime)s - %(levelname)s - %(message)s')

# Set Photo Destination
parsable = Parsable()
parsable.photo_dest = os.path.join(base_path, "All_Job_Photos")

def get_jobs(start, end):
    jobs_list = parsable.query_jobs_within_timeframe(start, end)
    # Make sure jobs_list is not NoneType (Empty)
    if jobs_list:
        # Go through job list job by job to get job data
        for job in jobs_list:
            # Get job data call
            job_data = parsable.get_job_data(job)
            # Make sure job_data is not NoneType (Empty) (Job not already downloaded) 
            if job_data:
                # Get all document IDs in job
                parsable.get_all_document_ids(job_data, job["lookupId"])
            else:
                logging.info("No Job Data")
    else:
        logging.info("Empty Job List")

if __name__ == "__main__":
    try:
        num_threads = 50
        threads = []

        # Time Frame =24 Hours
        time_frame = 86400
        current_time = int(time.mktime(time.localtime()))
        download_sections = int(time_frame/num_threads)

        for i in range(num_threads):
            since = current_time - ((i+1) * download_sections)
            before = current_time - (i * download_sections)
            t = threading.Thread(target=get_jobs, args=(since, before,))
            threads.append(t)

        for i in range(num_threads):
            threads[i].start()

        for i in range(num_threads):
            threads[i].join()

    except Exception as e:
        logging.exception("Exception occurred")
