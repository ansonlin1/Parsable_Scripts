from Parsable_API import *
import threading

# If Python Images Folder doesn't exist create it
if not os.path.isdir(os.path.join(expanduser("~"), "Documents", "Python_Projects_GIT", "Parsable_Scripts", "All_Job_Photos")):
	os.mkdir(os.path.join(expanduser("~"), "Documents", "Python_Projects_GIT", "Parsable_Scripts", "All_Job_Photos"))

# Create Log File
logFile = os.path.join(expanduser("~"), "Documents", "Python_Projects_GIT", "Parsable_Scripts", "All_Job_Log_File.log")
logging.basicConfig(level = logging.DEBUG, filename = logFile, format='%(asctime)s - %(levelname)s - %(message)s')

parsable = Parsable()
parsable.photo_dest = os.path.join(expanduser("~"), "Documents", "Python_Projects_GIT", "Parsable_Scripts", "All_Job_Photos")

# Days since August 1, 2018
# TODO: MUST UDPATE DAILY
days_since = 1070

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
            print("Job Done")
    else:
        logging.info("Empty Job List")

if __name__ == "__main__":
    try:
        num_threads = 50
        threads = []

        # Time Frame = Current Time - August 1, 2018 (Time between NOW and Aug 1, 2018)
        time_frame = int(time.mktime(time.localtime())) - 1533099600
        current_time = int(time.mktime(time.localtime()))
        download_sections = int(time_frame/num_threads)

        for i in range(num_threads):
            since = current_time - ((i+1) * download_sections)
            before = current_time - (i * download_sections)
            t = threading.Thread(target=get_jobs, args=(since, before,))
            t.daemon = True
            threads.append(t)

        for i in range(50):
            threads[i].start()

        for i in range(50):
            threads[i].join()

    except Exception as e:
        logging.exception("Exception occurred")
