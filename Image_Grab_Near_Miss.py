from Parsable_API import *

# Base Directory
base_path = os.path.join(expanduser("~"), "Downloads")

# If Python Images Folder doesn't exist create it
if not os.path.isdir(os.path.join(base_path, "Near_Miss_Photos")):
    # Create Folder to hold all images
    os.mkdir(os.path.join(base_path, "Near_Miss_Photos"))

# If Log Folder doesn't exist create it
if not os.path.isdir(os.path.join(base_path, "Near_Miss_Photos", "Near_Miss_Job_Logs")):
    # Create folder to hold all log files
    os.mkdir(os.path.join(base_path, "Near_Miss_Photos", "Near_Miss_Job_Logs"))

# Create Log File
local_time = time.localtime()
local_time_tuple = (str(local_time.tm_mon), str(local_time.tm_mday), str(local_time.tm_year), "Log.log")
log_file_name = "_".join(local_time_tuple)
log_file_path = os.path.join(base_path, "Near_Miss_Photos", "Near_Miss_Job_Logs", log_file_name)
logging.basicConfig(level = logging.DEBUG, filename = log_file_path, format='%(asctime)s - %(levelname)s - %(message)s')


if __name__ == "__main__":
    try:
        before_download = time.time()

        parsable = Parsable()
        parsable.photo_dest = os.path.join(base_path, "Near_Miss_Photos")

        # Query a list of jobs
        jobs_list = parsable.query_jobs_by_template(parsable.template_id_list)
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

        after_download = time.time()
        logging.info("Download Finished: " + str(after_download - before_download) + " seconds")
    except Exception as e:
        logging.exception("Exception occurred")
