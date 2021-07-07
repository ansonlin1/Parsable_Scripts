from Parsable_API import *

# Create Log File
logFile = os.path.join(expanduser("~"), "Documents", "Python_Projects_GIT", "Parsable_Scripts", "Template_To_Excel_Log_File.log")
logging.basicConfig(level = logging.DEBUG, filename = logFile, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    try:
        before_download = time.time()

        parsable = Parsable()
        
        templates = parsable.query_templates()
        parsable.template_metadata_to_excel(templates)

        # with open('parsable_jobs.json', 'w') as json_file:
        # 	json.dump(parsable.query_jobs_before_date(1593583200), json_file)

        """
        Template Version -> ["publicVersion"]
        Last Published -> ["publishedAt"] "Epoch & Unix Timestamp"
        Template Title -> ["title"]
        Template Description -> ["descrip"]
        Region -> "1ca6eba0-7aba-4b68-bb29-c99676450b84"
        Location -> ""02bf6962-5658-442d-b5bf-51b48f5e7062"
        Status = P(Production)
        Department -> "80ac5e3a-3ba2-41f2-8714-2e7e53d2fd12"
        Process -> "5d28ab79-edd9-491b-be10-2d68129eee79"
        Document # -> [""] --> N/A
        Document Owner -> [""] --> N/A
        """
        after_download = time.time()
        logging.info("Execution Finished: " + str(after_download - before_download) + " seconds")
    except Exception as e:
        logging.exception("Exception occurred")
