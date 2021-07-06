from LickLibrary import Buffer, Settings, Logger, DbConnector


class ZooLogger:
    def __init__(self, load_buffer=False, verbose=False, log_actions=False):
        self.table = Settings.table
        self.database = DbConnector.SQLconnector(Settings.database, Settings.table, Settings.omit_fields)
        self.buffer = Buffer.Buffer(load=load_buffer)
        self.log = Logger.Logger()
        self.log.print_comments = verbose
        self.log_actions = log_actions

    def view_log(self):
        self.log.view()

    def write_log(self):
        self.log.write(Settings.database_log)

    def add_data(self, data, flush=True):
        # Add the data to the buffer
        self.log.add_comment(['Adding data to buffer', data])
        self.buffer.append(data)
        # Save a copy of the buffer to disk
        self.log.add_comment('Saving buffer to disk')
        self.buffer.save()
        # if flush, then try to flush the buffer to AWS
        if flush and not self.buffer.empty: self.flush_buffer()
        if self.log_actions: self.write_log()

    def get_data(self):
        data = self.database.read_data()
        return data

    def flush_buffer(self):
        self.log.add_comment('Trying to flush buffer')
        successful_uploads = []
        for i in range(len(self.buffer)):
            self.log.add_comment(['Flushing:', self.buffer[i]])
            try:
                self.database.insert_data(self.buffer[i])
                successful_uploads.append(i)
            except Exception as exception:
                self.log.add_comment(exception, level=2)
        # remove the successfully uploaded data
        self.buffer.remove(successful_uploads)
        self.log.add_comment(['Remaining items in buffer:', len(self.buffer)])
        # save the updated buffer to disk
        self.log.add_comment('Saving buffer to disk')
        self.buffer.save()
        if self.log_actions: self.write_log()


