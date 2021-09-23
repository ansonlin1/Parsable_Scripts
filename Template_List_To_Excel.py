from Parsable_API import *

# Base Directory
base_path = os.path.join(expanduser("~"), "Downloads")

# Create Log File
log_file_path = os.path.join(base_path, "Template_To_Excel_Log_File.log")
logging.basicConfig(level = logging.DEBUG, filename = log_file_path, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    try:
        before_download = time.time()

        parsable = Parsable()
        
        templates = parsable.query_templates(parsable.sandbox_team_id)
        parsable.template_metadata_to_excel(templates)

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
