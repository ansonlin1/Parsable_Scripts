from Parsable_API import *

# If Python Images Folder doesn't exist create it
if not os.path.isdir(os.path.join(expanduser("~"), "Documents", "Python_Projects_GIT", "Parsable_Scripts", "All_Job_Photos")):
	os.mkdir(os.path.join(expanduser("~"), "Documents", "Python_Projects_GIT", "Parsable_Scripts", "All_Job_Photos"))

# Create Log File
logFile = os.path.join(expanduser("~"), "Documents", "Python_Projects_GIT", "Parsable_Scripts", "All_Job_Log_File.log")
logging.basicConfig(level = logging.DEBUG, filename = logFile, format='%(asctime)s - %(levelname)s - %(message)s')


if __name__ == "__main__":
    try:
        parsable = Parsable()
        parsable.photo_dest = os.path.join(expanduser("~"), "Documents", "Python_Projects_GIT", "Parsable_Scripts", "All_Job_Photos")

        # Days since August 1, 2018
        # TODO: MUST UDPATE DAILY
        days_since = 1070

        for i in range(days_since, 0, -1):
            # Query a list of jobs
            jobs_list = parsable.query_jobs_within_timeframe(i)
            print(i)
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
            logging.info("Empty Job List")

    except Exception as e:
        logging.exception("Exception occurred")
