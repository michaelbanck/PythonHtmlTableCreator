import TableCreator
import CreationLoop
import writer

if __name__ == '__main__':

    # delete all generated files from a folder
    writer.delete_all("test")

    table_creator = TableCreator.TableCreator(table_text_alignment=["left"], text_alignment=["left"],
                                              float_alignment=["left"], table_float_alignment=["left"],
                                              head_line_text_alignment=["left"],
                                              table_min_max_rows=(4, 14))

    CreationLoop.start_loop(table_creator=table_creator, folder="test", thread_count=1, files_per_thread=1)
